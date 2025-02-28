import streamlit as st

st.info("Objective: To find the values of distinct variables (A1, A2, A3 etc.) mentioned in various statements, and to"
        " evaluate true / false questions or MSQs.")

st.warning("Suggestion: To attempt the sections A, B and C, you may share this page with your class-mates and discuss "
           "the answers with them.")

"""### **Section A** 

1. The dimensional formulae of the universal constant of gravitation G is MA1LA2TA3 and that of the thermal conductivity k is MA4LA5TA6KA7. 

2. The gravitational force exerted by a spherically symmetric body of mass m1 on another such body of mass m2 kept outside the first body is Gm1m2r^A3, where r is the distance between the centers of the two bodies."""

A_2, A_3 = st.columns(2)

with A_2:
    if st.button("True", key=A_2):
        st.balloons()
with A_3:
    if st.button("False", key=A_3):
        st.write("NOIDONTTHINKSO")

"""
3. Water falling from a 50 m high fall is used for generating electrical energy. If 1.8 * 105 kg of water falls per hour (negligible evaporation) and half the gravitational potential energy can be converted into electric energy, A8 100 W lamps can be lit. [Take g = 9.8 m/s2] 

4. The square of the time period of a planet is proportional to the A2 power of the semi-major axis of the ellipse.
"""

A_4, A_5 = st.columns(2)

with A_4:
    if st.button("True", key=A_4):
        st.balloons()
with A_5:
    if st.button("False", key=A_5):
        st.write("NOIDONTTHINKSO")

"""
5. Velocity of a travelling wave on a string ‘v’ is related to the tension T and the linear mass density ‘m’ as: v2 = T * m^A4.
"""

A_6, A_7 = st.columns(2)

with A_6:
    if st.button("True", key=A_6):
        st.write("NOIDONTTHINKSO")
with A_7:
    if st.button("False", key=A_7):
        st.balloons()

"""
6. Equation of a transverse wave travelling in a rope is given by y = 4 sin (5.0 t - 0.01 x), where y and x are expressed in cm and time in seconds. The amplitude and wavelength are A9 and (A10)π cm. And, the maximum transverse speed and maximum acceleration of a particle on the rope are A11 cm/s and A12 cm/s2, respectively.

7. A fluid has bulk modulus of 4 * 109 Pa and density 103 kg/m3. The speed of sound in that fluid is 10 * (A10) m/s. True / False.
"""
A_8, A_9 = st.columns(2)

with A_8:
    if st.button("True", key=A_8):
        st.balloons()
with A_9:
    if st.button("False", key=A_9):
        st.write("NOIDONTTHINKSO")

"""
8. By Newton`s Formula the speed of sound at one atmospheric pressure is nearly 280 m/s. CP/CV for air is 7/4. The actual speed of sound in air is nearly A13 m/s.

9. The amount of energy which flows perpendicular to a plane per unit area per unit time in a wave is proportional to A14 power of frequency of the wave and A15 power of the amplitude of displacement of particle of the wave.

10. Radio waves, X-rays; Light waves; Sound waves; Gamma rays. Among those mentioned here A9 waves are non-mechanical."""

A_10, A_11 = st.columns(2)

with A_10:
    if st.button("True", key=A_10):
        st.write("NOIDONTTHINKSO")
with A_11:
    if st.button("False", key=A_11):
        st.balloons()

st.write("-------------------------------------------------")

A1, A2, A3, A4, A5, A6, A7, A8 = st.columns(8)

with A1:
    with st.popover("A1"):
        st.write("-1")

with A2:
    with st.popover("A2"):
        st.write("3")

with A3:
    with st.popover("A3"):
        st.write("-2")

with A4:
    with st.popover("A4"):
        st.write("1")

with A5:
    with st.popover("A5"):
        st.write("1")

with A6:
    with st.popover("A6"):
        st.write("-3")

with A7:
    with st.popover("A7"):
        st.write("-1")

with A8:
    with st.popover("A8"):
        st.write("122")

"""
### **Section B**

1. The density of the core of a planet is ρ1 and that of the outer shell is ρ2, the radii of the core and that of the planet are R and 2R respectively. The acceleration due to gravity at the surface of the planet is the same as that at a depth R. The ratio of density ρ1/ρ2 is 7/B1.

2. A planet revolving around a very massive star in a circular orbit of radius R with a period of revolution T. If the gravitational force of attraction between the planet and the star is proportional to R-2.5, then T is proportional to 7/(1+B1). True / False.

3. A wave is travelling along the X-axis. The disturbance at x = 0 and t = 0 is A/2 and is increasing, where A is amplitude of the wave. If y = A sin (kx - wt + φ), the initial phase φ = π / (A9 + A14). True /False.

4. A long string of mass per unit length 0.01 kg/m is subject to a tension of 64 N along the x-axis. One end (x=0) of this string is attached to a vibrator moving in a transverse direction at a frequency of 20 Hz. At t = 0; x = 0, the particle is at maximum displacement y = 1.0 cm. The magnitude of velocity of the particle at x = 50 cm, at time t = 0.05s is B2 *2 cm/s.

5. A travelling wave is given by  Y = 0.8 / (3x2 + 24xt + 48t2 + 4)  where x and y are in metres and t is in second. The wave speed is (A3)2. True / False.

6. A sky-diver falls with a terminal speed B3 m/s carrying a buzzer emitting a steady tone at 1800 Hz. The speed of sound is 343 m/s. A friend of a skydiver on the ground receives waves of frequency 2150 Hz. The sky-diver also records the frequency of sound reflected by the ground B4 Hz."""

B1, B2, B3, B4 = st.columns(4)

with B1:
    with st.popover("B1"):
        st.write("3")

with B2:
    with st.popover("B2"):
        st.write("20 π")

with B3:
    with st.popover("B3"):
        st.write("56")

with B4:
    with st.popover("B4"):
        st.write("2501")

"""
### **Section C**

1. Two pulses y1 and y2 travel on the same string.

Y1= 5 / [(3x - 4t)2+2] and Y2 = - 5 / [(3x + 4t - 6)2 + 2]

At time 3 / C1 second the displacement of all particles will be zero i.e. the two pulses cancel everywhere. Position x = C2 metre is a node (permanent).

2. In the previous Q, Y1 and Y2 pulses travel in the same direction.True / False.

3. Two waves y1 and y2 superimpose to give the resultant wave, y1 = A sin (kx - wt); y2 = A sin (kx - wt + φ). The resultant of the two waves y1 and y2 has amplitude 2A sin (φ/2). True / False.

4. In a sono-meter, l1 and l2 are two successive resonance lengths. N0 is the frequency of oscillating sources. The wave velocity is C3 * n0 * (l2 - l1). (l2 > l1)

5. The fundamental frequency of a sono-meter wire increases by 6 Hz if the tension is increased by 44 %, keeping the length constant. The change in fundamental frequency of the sonometer is | A5 + A6 + A7 | hz when the length of wire is increased by 20 %, keeping the original tension in the wire constant. True / False.

6. The length of a pipe is l = 85 cm. The speed of sound is 340 m/s. When the pipe is open at both ends the 2nd harmonic frequency is 2 * A10 Hz and the third harmonic frequency is 3 * A12 Hz. True / False.

7. In the previous question, the sqrt (B4)th harmonic is C4 * 100 hz in an open pipe. The sqrt (B4)th harmonic does not exist for a closed pipe. True / False.

8. An open pipe 40 cm long and a closed pipe 31 cm long, both having the same diameter, are producing their first overtone, and they are in unison. The end correction of these pipes is C3 cm. True / False."""

C1, C2, C3 = st.columns(3)

with C1:
    with st.popover("C1"):
        st.write("4")

with C2:
    with st.popover("C2"):
        st.write("1")

with C3:
    with st.popover("C3"):
        st.write("2")

# sentiment_mapping = [0, 1]
# selected = st.feedback("thumbs")
# if selected is not None:
#     st.markdown("Thanks for your feedback!")
