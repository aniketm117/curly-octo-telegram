import streamlit as st

# Current Electricity

"""
### **Experimental Setup to Verify Ohm's Law**

**Ohm's Law** is a fundamental principle in electrical circuits that states:

V = I * R

where:  
- V : Voltage across the resistor (in volts, V)  
- I : Current flowing through the resistor (in amperes, A)  
- R : Resistance of the resistor (in ohms)  

#### **Apparatus Needed:**
1. **Power supply:** Provides a range of voltages (e.g., DC power supply or batteries).
2. **Resistor:** Known resistance value R.
3. **Voltmeter:** Measures the voltage across the resistor.
4. **Ammeter:** Measures the current through the resistor.
5. **Rheostat (optional):** To vary the current in the circuit.
6. **Connecting wires** and **breadboard** (or similar circuit assembly tools).
7. **Switch:** To control the flow of current.

#### **Circuit Diagram:**
- Connect the resistor R in series with the ammeter and power supply.
- The voltmeter is connected in parallel across the resistor to measure the potential difference.


#### **Procedure:**
1. Assemble the circuit as per the diagram.
2. Adjust the power supply to provide a known voltage.
3. Record the readings of the voltmeter **V** and ammeter **I**.
4. Vary the voltage using the power supply or rheostat and repeat the measurements for several values of **V**
 and **I**.
5. Calculate the resistance **R** for each pair of readings using the formula R = V / I.

#### **Expected Result:**
For a given resistor,R should remain constant for all values of V and I, confirming Ohm's Law.

#### **Graphical Verification:**
- Plot a graph of V (y-axis) against I (x-axis). 
- The graph should be a straight line passing through the origin, with the slope equal to R (resistance)."""

### **Questions and Answers**

with st.expander("""**1. Question:** In an experiment to verify Ohm’s Law, a student sets up a circuit with a resistor 
            of 10 ohm. The student measures a current of 0.5 A when the applied voltage is 5 V. Does this
            confirm Ohms Law? Show the calculation."""):

    st.info("""**Answer:**
    
        Ohm's Law states
            
        V = I * R
        
        From the given data:
        
        I = 0.5 , V = 5 , R = ?
        
        Calculate R:
        
        R = {V}/{I} = 5 / 0.5 = 10
                    
        The calculated resistance matches the resistor's given value 10ohm. Thus, the results confirm Ohm's Law.
            """)

with st.expander("""**2. Question:**
                 Why is it important to connect the voltmeter in parallel and the ammeter in series in the circuit
                 during the experiment?"""):
    st.info("""**Answer:**
            The voltmeter measures the potential difference across the resistor. It must be connected
            in parallel so it measures the voltage drop across the resistor without affecting the current flow
            through it. Voltmeters have high resistance, minimizing current flow through them. 
            - The ammeter measures the total current flowing in the circuit. It must be connected in series
            to ensure the same current flows through both the ammeter and the resistor. Ammeters have very low
            resistance to avoid altering
            the circuit's current.""")

with st.expander("""**3. Question:**
                 If a student plots a graph of voltage V versus current I for a resistor and observes a curve
                 instead of a straight line, what might be the reason?
                 ?"""):
    st.info("""The curve indicates that Ohm’s Law is not being followed. Possible reasons include:
            1. **Non-ohmic behavior:** The resistor may not be an ohmic conductor. Examples include diodes or filament
             bulbs, where resistance changes with temperature or voltage.
            2. **Overheating of the resistor:** At higher currents, the resistor might heat up, changing its resistance.
            3. **Faulty apparatus:** Errors in the connections, or a malfunctioning resistor, voltmeter, or ammeter,
             can cause deviations.
            To address this, ensure the resistor is ohmic, the connections are correct, and the apparatus is functioning
             properly.""")
