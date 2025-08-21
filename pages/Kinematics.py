import streamlit as st

st.info("🎯 All Questions mentioned are Multiple choices Single correct type")

tabs = st.tabs(['Section A', 'Section B', 'Section C'])

with tabs[0]:
    """
    **Differentiation**
    
    The term '\u0394y/\u0394t represented the average velocity of the particle between the time instants x\u2081 and 
    x\u2082. At the instant x\u2081 itself the term becomes dy/dx, which implies we have determined the instantaneous 
    velocity of the particle at that instant. 
    
    dy/dx refers to differentiation of y wrt x or derivative of y wrt x.
    
    Q1. d(x)/dx =  
    """

    A_1, A_2, A_3, A_4 = st.columns(4)

    with A_1:
        if st.button("1", key=A_1, use_container_width=True):
            st.success("✔️")
    with A_2:
        if st.button("2", key=A_2, use_container_width=True):
            st.warning("Try Again")
    with A_3:
        if st.button("x", key=A_3, use_container_width=True):
            st.warning("Try Again")
    with A_4:
        if st.button("None", key=A_4, use_container_width=True):
            st.warning("Try Again")

    """
    Q2. d(x\u207F)/dx =
    """

    A_5, A_6, A_7, A_8 = st.columns(4)

    with A_5:
        if st.button("x", key=A_5, use_container_width=True):
            st.success("Try Again")
    with A_6:
        if st.button("n * x ^ (n-1)", key=A_6, use_container_width=True):
            st.success("✔️")
    with A_7:
        if st.button("n * x\u207F", key=A_7, use_container_width=True):
            st.warning("Try Again")
    with A_8:
        if st.button("None", key=A_8, use_container_width=True):
            st.warning("Try Again")

    """
    Q3. d(cos(x))/dx =  
    """

    A_9, A_10, A_11, A_12 = st.columns(4)

    with A_9:
        if st.button("tan (x)", key=A_9, use_container_width=True):
            st.success("Try Again")
    with A_10:
        if st.button("sin (x)", key=A_10, use_container_width=True):
            st.warning("Try Again")
    with A_11:
        if st.button(" (-1) * sin (x)", key=A_11, use_container_width=True):
            st.success("Correct")
    with A_12:
        if st.button("cosec ^2 (x)", key=A_12, use_container_width=True):
            st.warning("Try Again")

    """
    Q4. If 'A' is a constant then, d(sin(A*x))/dx =   
    """

    A_13, A_14, A_15, A_16 = st.columns(4)

    with A_13:
        if st.button("A * sin(A*x)", key=A_13, use_container_width=True):
            st.success("Try Again")
    with A_14:
        if st.button("A + sin(A*x)", key=A_14, use_container_width=True):
            st.warning("Try Again")
    with A_15:
        if st.button("A * cos(A*x)", key=A_15, use_container_width=True):
            st.success("Correct")
    with A_16:
        if st.button("A * cosec(A*x)", key=A_16, use_container_width=True):
            st.warning("Try Again")

    A1, A2, A3 = st.columns(3)


with tabs[1]:
    ""

with tabs[2]:
    ""

    # sentiment_mapping = [0, 1]
    # selected = st.feedback("thumbs")
    # if selected is not None:
    #     st.markdown("Thanks for your feedback!")
