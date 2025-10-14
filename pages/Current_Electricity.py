import streamlit as st

# Current Electricity

"""
## Experimental Setup to Verify Ohm's Law   

    Ohm's Law is a fundamental principle in electrical circuits that states:
    
        V = I * R
        
        where:  
        - V : Voltage across the resistor (in volts, V)  
        - I : Current flowing through the resistor (in amperes, A)  
        - R : Resistance of the resistor (in ohms)  
"""

tabs = st.tabs(['Apparatus Needed', 'Circuit Scheme', 'Procedure',
                'Expected Result', 'Graphical Verification'])

with tabs[0]:
    """
    - **Power supply:** Provides a range of voltages (e.g., Cells or batteries).
    - **Resistor:** Known resistance value R.
    - **Voltmeter:** Measures the voltage across the resistor.
    - **Ammeter:** Measures the current through the resistor.
    - **Rheostat (optional):** To vary the current in the circuit.
    - **Connecting wires** and **breadboard** (or similar circuit assembly tools).
    - **Switch:** To control the flow of current.
    """
with tabs[1]:
    """
    - Connect the resistor R in series with the ammeter and battery.
    - The voltmeter is connected in parallel across the resistor.
    """

with tabs[2]:
    """
    - Assemble the circuit as per the scheme.
    - Adjust the power supply to provide a known voltage.
    - Record the readings of the voltmeter **V** and ammeter **I**.
    - Vary the voltage using the power supply or rheostat and repeat the measurements for several values of **V**
    and **I**.
    - Calculate the resistance **R** for each pair of readings using the formula R = V / I.
    """

with tabs[3]:
    """
    - The ratio V / I should remain constant throughout the observations.
    """
with tabs[4]:
    """
    - Plot a graph of voltage against current. 
    - The graph should be a straight line passing through the origin, with the slope equal to R (resistance).
    """

    data = {'Current': [1, 2, 3, 4, 5, 6],
            'Voltage': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]}

    option = st.selectbox("Select the data to be shown on x-axis",
                          ['Voltage', 'Current'])

    if option == 'Voltage':
        option_2 = 'Current'
    else:
        option_2 = 'Voltage'

    st.line_chart(data, x=option, y=option_2)

# Questions and Answers

with st.expander("Q 1. Why is it important to connect the voltmeter in parallel and ammeter in series in the circuit"
                 "during the experiment?"):
    st.write("""
            - The voltmeter measures the potential difference across the resistor. 
            - It must be connected in parallel so it measures the voltage drop across the resistor without affecting the
            current flow through it. 
            - Voltmeters have high resistance, minimizing current flow through them. The ammeter measures the total 
            current flowing in the circuit. 
            - Ammeter must be connected in series to ensure the same current flows through both the ammeter and 
            the resistor. 
            - Ammeters have very low resistance to avoid altering the circuit's current.""")

with st.expander("Q 2. If a student plots a graph of voltage V versus current I for a resistor and observes a curve"
                 "instead of a straight line, what might be the reason?"):
    st.write("""
        The curve indicates that Ohm’s Law is not being followed. Possible reasons include:
    
        - Non-ohmic behavior: The resistor may not be an ohmic conductor. Examples include diodes or filament
          bulbs, where resistance changes with temperature or voltage.
             
        - Overheating of the resistor: At higher currents, the resistor might heat up, changing its resistance.
            
        - Faulty apparatus: Errors in the connections, or a malfunctioning resistor, voltmeter, or ammeter,
             can cause deviations.
             
        To address this, ensure the resistor is ohmic, the connections are correct, and the apparatus is functioning
        properly.""")
