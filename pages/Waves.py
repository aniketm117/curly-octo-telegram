import streamlit as st

st.info("🎯 Find the values of distinct variables (A1, A2, A3 etc.) mentioned in various statements, and to"
        " evaluate true / false questions.🪥 Brush some concepts of Gravitation before proceeding as some Q"
        "s on that topic are included.")

tabs = st.tabs(['Section A', 'Section B', 'Section C'])

with tabs[0]:
    """
    1. The dimensional formulae of the universal constant of gravitation G is M^A1 L^A2 T^A3 and that of the thermal 
    conductivity k is M^A4 L^A5 T^A6 K^A7.
    
    2. A travelling wave is given by  Y = 0.8 / (3x^2 + 24xt + 48t^2 + 4)  where x and y are in metres and t is in second. 
    The wave speed is (A3)^2.
    """

    A_1, A_2 = st.columns(2)

    with A_1:
        if st.button("True", key=A_1, use_container_width=True):
            st.balloons()
    with A_2:
        if st.button("False", key=A_2, use_container_width=True):
            st.write("Try Again")

#     """
#     3. The gravitational force exerted by a spherically symmetric body of mass m1 on another such body of mass m2 kept
#     outside the first body is G m1 m2 r^A3, where r is the distance between the centers of the two bodies.
#     """
#
#     A_3, A_4 = st.columns(2)
#
#     with A_3:
#         if st.button("True", key=A_3, use_container_width=True):
#             st.balloons()
#     with A_4:
#         if st.button("False", key=A_4, use_container_width=True):
#             st.write("Try Again")
#
#     """
#     4. The fundamental frequency of a sono-meter wire increases by 6 Hz if the tension is increased by 44 %, keeping the
#     length constant. The change in fundamental frequency of the sono-meter is | A5 + A6 + A7 | hz when the length of wire is
#     increased by 20 %, keeping the original tension in the wire constant.
#     """
#
#     A_5, A_6 = st.columns(2)
#
#     with A_5:
#         if st.button("True", key=A_5, use_container_width=True):
#             st.warning("Try Again")
#     with A_6:
#         if st.button("False", key=A_6, use_container_width=True):
#             st.success("✔️")
#     """
#     5. Water falling from a 50 m high fall is used for generating electrical energy. If 1.8 * 10^5 kg of water falls per
#     hour (negligible evaporation) and half the gravitational potential energy can be converted into electric energy, A8
#     100 W lamps can be lit. [Take g = 9.8 m/s2]
#
#     6. The square of the time period of a planet is proportional to the A2 power of the semi-major axis of the ellipse.
#     """
#
#     A_7, A_8 = st.columns(2)
#
#     with A_7:
#         if st.button("True", key=A_7, use_container_width=True):
#             st.balloons()
#     with A_8:
#         if st.button("False", key=A_8, use_container_width=True):
#             st.write("Try Again")
#
#     """
#     7. Velocity of a travelling wave on a string ‘v’ is related to the tension T and the linear mass density ‘m’ as:
#     v^2 = T * m^A4.
#     """
#
#     A_9, A_10 = st.columns(2)
#
#     with A_9:
#         if st.button("True", key=A_9, use_container_width=True):
#             st.write("Try Again")
#     with A_10:
#         if st.button("False", key=A_10, use_container_width=True):
#             st.success("✔️")
#
#     """
#     8. Equation of a transverse wave travelling in a rope is given by y = 4 sin (5.0 t - 0.01 x), where y and x are
#     expressed in cm and time in seconds. The amplitude and wavelength are A9 and (A10)π cm. And, the maximum transverse
#     speed and maximum acceleration of a particle on the rope are A11 cm/s and A12 cm/s2, respectively.
#
#     9. A fluid has bulk modulus of 4 * 10^9 Pa and density 10^3 kg/m3. The speed of sound in that fluid is 10 * (A10) m/s.
#     """
#     A_11, A_12 = st.columns(2)
#
#     with A_11:
#         if st.button("True", key=A_11, use_container_width=True):
#             st.success("✔️")
#     with A_12:
#         if st.button("False", key=A_12, use_container_width=True):
#             st.write("Try Again")
#
#     """
#     10. The length of a pipe is l = 85 cm. The speed of sound is 340 m/s. When the pipe is open at both ends the 2nd harmonic
#      frequency is 2 * A10 Hz and the third harmonic frequency is 3 * A12 Hz. True / False.
#     """
#     A_13, A_14 = st.columns(2)
#
#     with A_13:
#         if st.button("True", key=A_13, use_container_width=True):
#             st.success("✔️")
#     with A_14:
#         if st.button("False", key=A_14, use_container_width=True):
#             st.warning("Try Again")
#     """
#     11. By Newton`s Formula the speed of sound at one atmospheric pressure is nearly 280 m/s. CP/CV for air is 7/4. The
#     actual speed of sound in air is nearly A13 m/s.
#
#     12. The amount of energy which flows perpendicular to a plane per unit area per unit time in a wave is proportional to
#     A14 power of frequency of the wave and A15 power of the amplitude of displacement of particle of the wave.
#
#     12. A wave is travelling along the X-axis. The disturbance at x = 0 and t = 0 is A/2 and is increasing, where A is
#     amplitude of the wave. If y = A sin (kx - wt + φ), the initial phase φ = π / (A9 + A14). True /False.
#     """
#
#     A_15, A_16 = st.columns(2)
#
#     with A_15:
#         if st.button("True", key=A_15, use_container_width=True):
#             st.balloons()
#     with A_16:
#         if st.button("False", key=A_16, use_container_width=True):
#             st.write("Try Again")
#
#     A1, A2, A3, A4, A5, A6, A7, A8 = st.columns(8)
#     A9, A10, A11, A12, A13, A14, A15 = st.columns(7)
#
#     with A1:
#         with st.popover("A1", use_container_width=True):
#             st.write("-1")
#
#     with A2:
#         with st.popover("A2", use_container_width=True):
#             st.write("3")
#
#     with A3:
#         with st.popover("A3", use_container_width=True):
#             st.write("-2")
#
#     with A4:
#         with st.popover("A4", use_container_width=True):
#             st.write("1")
#
#     with A5:
#         with st.popover("A5", use_container_width=True):
#             st.write("1")
#
#     with A6:
#         with st.popover("A6", use_container_width=True):
#             st.write("-3")
#
#     with A7:
#         with st.popover("A7", use_container_width=True):
#             st.write("-1")
#
#     with A8:
#         with st.popover("A8", use_container_width=True):
#             st.write("122")
#
#     with A9:
#         with st.popover("A9", use_container_width=True):
#             st.write("4")
#
#     with A10:
#         with st.popover("A10", use_container_width=True):
#             st.write("200")
#
#     with A11:
#         with st.popover("A11", use_container_width=True):
#             st.write("20")
#
#     with A12:
#         with st.popover("A12", use_container_width=True):
#             st.write("100")
#
#     with A13:
#         with st.popover("A13", use_container_width=True):
#             st.write("370")
#
#     with A14:
#         with st.popover("A14", use_container_width=True):
#             st.write("2")
#
#     with A15:
#         with st.popover("A15", use_container_width=True):
#             st.write("2")
#
# with tabs[1]:
#     """
#     1. The density of the core of a planet is ρ1 and that of the outer shell is ρ2, the radii of the core and that of the
#     planet are R and 2R respectively. The acceleration due to gravity at the surface of the planet is the same as that at a
#     depth R. The ratio of density ρ1/ρ2 is 7/B1.
#
#     2. A planet revolving around a very massive star in a circular orbit of radius R with a period of revolution T. If the
#     gravitational force of attraction between the planet and the star is proportional to R^-2.5, then T is proportional to
#     7/(1+B1)."""
#
#     B_1, B_2 = st.columns(2)
#
#     with B_1:
#         if st.button("True", key=B_1, use_container_width=True):
#             st.balloons()
#     with B_2:
#         if st.button("False", key=B_2, use_container_width=True):
#             st.write("Try Again")
#
#     """
#
#     3. A long string of mass per unit length 0.01 kg/m is subject to a tension of 64 N along the x-axis. One end (x=0) of
#     this string is attached to a vibrator moving in a transverse direction at a frequency of 20 Hz. At t = 0; x = 0, the
#     particle is at maximum displacement y = 1.0 cm. The magnitude of velocity of the particle at x = 50 cm, at time
#     t = 0.05s is B2 *2 cm/s.
#
#     4. A sky-diver falls with a terminal speed B3 m/s carrying a buzzer emitting a steady tone at 1800 Hz. The speed of
#     sound is 343 m/s. A friend of a skydiver on the ground receives waves of frequency 2150 Hz. The sky-diver also records
#     the frequency of sound reflected by the ground B4 Hz."""
#
#     B1, B2, B3, B4 = st.columns(4)
#
#     with B1:
#         with st.popover("B1", use_container_width=True):
#             st.write("3")
#
#     with B2:
#         with st.popover("B2", use_container_width=True):
#             st.write("20 π")
#
#     with B3:
#         with st.popover("B3", use_container_width=True):
#             st.write("56")
#
#     with B4:
#         with st.popover("B4", use_container_width=True):
#             st.write("2501")
#
# with tabs[2]:
#     """
#     1. Two pulses y1 and y2 travel on the same string.
#     Y1= 5 / [(3x - 4t)^2+2] and Y2 = - 5 / [(3x + 4t - 6)^2 + 2]
#     At time 3 / C1 second the displacement of all particles will be zero i.e. the two pulses cancel everywhere. Position x =
#      C2 metre is a node (permanent).
#
#     2. In the previous Q, Y1 and Y2 pulses travel in the same direction.
#     """
#     C_1, C_2 = st.columns(2)
#
#     with C_1:
#         if st.button("True", key=C_1, use_container_width=True):
#             st.warning("Try Again")
#     with C_2:
#         if st.button("False", key=C_2, use_container_width=True):
#             st.write("Success")
#
#     """
#     3. Two waves y1 and y2 superimpose to give the resultant wave, y1 = A sin (kx - wt); y2 = A sin (kx - wt + φ). The
#     resultant of the two waves y1 and y2 has amplitude 2A sin (φ/2). True / False.
#     """
#
#     C_3, C_4 = st.columns(2)
#
#     with C_3:
#         if st.button("True", key=C_3, use_container_width=True):
#             st.warning("Try Again")
#     with C_4:
#         if st.button("False", key=C_4, use_container_width=True):
#             st.write("Success")
#
#     """
#     4. In a sono-meter, l1 and l2 are two successive resonance lengths. N0 is the frequency of oscillating sources.
#     The wave velocity is C3 * n0 * (l2 - l1). (l2 > l1)
#
#     5. In the previous question, the sqrt (B4)th harmonic is C4 * 100 hz in an open pipe. The sqrt (B4)th harmonic does not
#     exist for a closed pipe.
#     """
#     C_5, C_6 = st.columns(2)
#
#     with C_5:
#         if st.button("True", key=C_5, use_container_width=True):
#             st.write("Success")
#     with C_6:
#         if st.button("False", key=C_6, use_container_width=True):
#             st.warning("Try Again")
#
#     """
#
#     6. An open pipe 40 cm long and a closed pipe 31 cm long, both having the same diameter, are producing their first
#     overtone, and they are in unison. The end correction of these pipes is C3 cm. True / False."""
#
#     C_7, C_8 = st.columns(2)
#
#     with C_7:
#         if st.button("True", key=C_7, use_container_width=True):
#             st.write("Success")
#     with C_8:
#         if st.button("False", key=C_8, use_container_width=True):
#             st.warning("Try Again")
#
#     C1, C2, C3 = st.columns(3)
#
#     with C1:
#         with st.popover("C1", use_container_width=True):
#             st.write("4")
#
#     with C2:
#         with st.popover("C2", use_container_width=True):
#             st.write("1")
#
#     with C3:
#         with st.popover("C3", use_container_width=True):
#             st.write("2")
