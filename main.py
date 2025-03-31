import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from datetime import datetime, timedelta

# Page title
st.set_page_config(page_title='A Guide to Physics Revision', page_icon='🌃')
st.title('🌃 A Guide to Physics Revision')

# audio_file = open("audio/Spotify.mp3", "rb")
# audio_bytes = audio_file.read()
#
# st.audio(audio_bytes, format="audio/mp3")

clmn1, clmn2, clmn3, clmn4, clmn5 = st.columns(5)

with clmn1:
    st.page_link("pages/Vectors.py",
                 label="Vectors",
                 icon="📊",
                 use_container_width=True)

with clmn2:
    st.page_link("pages/Current_Electricity.py",
                 label="Current Electricity",
                 icon="🐛",
                 use_container_width=True)

with clmn3:
    st.page_link("pages/Waves.py",
                 label="Waves",
                 icon="🌊",
                 use_container_width=True)

with clmn4:
    st.page_link("pages/Roadmap.py",
                 label="Roadmap",
                 icon="🧙",
                 use_container_width=True)

with clmn5:
    st.page_link("pages/Rotational_Motion.py",
                 label="Rotational Motion",
                 icon="🌴",
                 use_container_width=True)


st.info('To write a ticket, fill out the form below. Check status or review ticketing analytics using the tabs below.')

# Generate data
## Set seed for reproducibility
np.random.seed(42)


## Function to generate a random issue description
def generate_issue():
    issues = [
        "Dimension of Force",
        "Formula for Momentum",
        "Sign conventions in Kinematics",
        "Sign conventions in Ray Optics",
        "Rope failure",
        "Boat-river centre of mass problems",
        "Unit vector application",
        "Force identification in Free Body diagrams",
        "Magnetic Field on the axis of a circular loop",
        "Poynting Vector",
        "Force on an electron in Electric and Magnetic Fields",
        "Davidson Germer Experiment",
        "Relation of Fringe width, Slit width and wavelength in YDSE",
        "External Work in Thermodynamics",
        "Do photons have mass ?",
        "File server running out of storage space",
        "Intrusion detection system alerts",
        "Inventory management system errors",
        "Customer data not loading in CRM",
        "Collaboration tool not sending notifications"
    ]
    return np.random.choice(issues)


## Function to generate random dates
start_date = datetime(2025, 4, 1)
end_date = datetime(2025, 12, 20)
id_values = ['TICKET-{}'.format(i) for i in range(1000, 1100)]
issue_list = [generate_issue() for _ in range(100)]


def generate_random_dates(start_date, end_date, id_values):
    date_range = pd.date_range(start_date, end_date).strftime('%m-%d-%Y')
    return np.random.choice(date_range, size=len(id_values), replace=False)


## Generate 100 rows of data
data = {'Issue': issue_list,
        'Status': np.random.choice(['Open', 'In Progress', 'Closed'], size=100),
        'Priority': np.random.choice(['High', 'Medium', 'Low'], size=100),
        'Date Submitted': generate_random_dates(start_date, end_date, id_values)
        }
df = pd.DataFrame(data)
df.insert(0, 'ID', id_values)
df = df.sort_values(by=['Status', 'ID'], ascending=[False, False])

## Create DataFrame
if 'df' not in st.session_state:
    st.session_state.df = df


# Sort dataframe
def sort_df():
    st.session_state.df = edited_df.copy().sort_values(by=['Status', 'ID'], ascending=[False, False])


# Tabs for app layout
tabs = st.tabs(['Write a ticket', 'Ticket Status and Analytics'])

recent_ticket_number = int(max(st.session_state.df.ID).split('-')[1])

with tabs[0]:
    with st.form('addition'):
        issue = st.text_area('Description of issue')
        priority = st.selectbox('Priority', ['High', 'Medium', 'Low'])
        submit = st.form_submit_button('Submit')

    if submit:
        today_date = datetime.now().strftime('%m-%d-%Y')
        df2 = pd.DataFrame([{'ID': f'TICKET-{recent_ticket_number + 1}',
                             'Issue': issue,
                             'Status': 'Open',
                             'Priority': priority,
                             'Date Submitted': today_date
                             }])
        st.write('Ticket submitted!')
        st.dataframe(df2, use_container_width=True, hide_index=True)
        st.session_state.df = pd.concat([st.session_state.df, df2], axis=0).sort_values(by=['Status', 'ID'],
                                                                                        ascending=[False, False])

with tabs[1]:
    status_col = st.columns((3, 1))
    with status_col[0]:
        st.subheader('Support Ticket Status')
    with status_col[1]:
        st.write(f'No. of tickets: `{len(st.session_state.df)}`')

    st.markdown('**Things to try:**')
    st.info('1️⃣ Update Ticket **Status** or **Priority** and see how plots are updated in real-time!')
    st.success(
        '2️⃣ Change values in **Status** column from *"Open"* to either *"In Progress"* or *"Closed"*, then click on the **Sort DataFrame by the Status column** button to see the refreshed DataFrame with the sorted **Status** column.')

    edited_df = st.data_editor(st.session_state.df, use_container_width=True, hide_index=True, height=212,
                               column_config={'Status': st.column_config.SelectboxColumn(
                                   'Status',
                                   help='Ticket status',
                                   options=[
                                       'Open',
                                       'In Progress',
                                       'Closed'
                                   ],
                                   required=True,
                               ),
                                   'Priority': st.column_config.SelectboxColumn(
                                       'Priority',
                                       help='Priority',
                                       options=[
                                           'High',
                                           'Medium',
                                           'Low'
                                       ],
                                       required=True,
                                   ),
                               })
    st.button('🔄 Sort DataFrame by the Status column', on_click=sort_df)

    # Status plot
    st.subheader('Support Ticket Analytics')
    col = st.columns((1, 3, 1))

    with col[0]:
        n_tickets_queue = len(st.session_state.df[st.session_state.df.Status == 'Open'])

        st.metric(label='First response time (hr)', value=5.2, delta=-1.5)
        st.metric(label='No. of tickets in the queue', value=n_tickets_queue, delta='')
        st.metric(label='Avg. ticket resolution time (hr)', value=16, delta='')

    with col[1]:
        status_plot = alt.Chart(edited_df).mark_bar().encode(
            x='month(Date Submitted):O',
            y='count():Q',
            xOffset='Status:N',
            color='Status:N'
        ).properties(title='Ticket status in the past 6 months', height=300).configure_legend(orient='bottom',
                                                                                              titleFontSize=14,
                                                                                              labelFontSize=14,
                                                                                              titlePadding=5)
        st.altair_chart(status_plot, use_container_width=True, theme='streamlit')

    with col[2]:
        priority_plot = alt.Chart(edited_df).mark_arc().encode(
            theta="count():Q",
            color="Priority:N"
        ).properties(title='Current ticket priority', height=300).configure_legend(orient='bottom', titleFontSize=14,
                                                                                   labelFontSize=14, titlePadding=5)
        st.altair_chart(priority_plot, use_container_width=True, theme='streamlit')
