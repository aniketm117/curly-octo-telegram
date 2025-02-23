import streamlit as st

st.info("Objective: To find the values of distinct variables (A1, A2, A3 etc.) mentioned in various statements, and to"
        " evaluate true / false questions or MSQs.")

st.warning("Suggestion: To attempt the sheets A, B and C, you may give the sheets to your class-mates and discuss the"
           " answers with them.")

st.write("""Sheet A

The dimensional formulae of the universal constant of gravitation G is MA1LA2TA3 and that of the thermal conductivity k is MA4LA5TA6KA7.

The gravitational force exerted by a spherically symmetric body of mass m1 on another such body of mass m2 kept outside the first body is Gm1m2rA3, where r is the distance between the centers of the two bodies. True / False.

Water falling from a 50 m high fall is used for generating electrical energy. If 1.8 * 105 kg of water falls per hour (negligible evaporation) and half the gravitational potential energy can be converted into electric energy, A8 100 W lamps can be lit. [Take g = 9.8 m/s2]

The square of the time period of a planet is proportional to the A2 power of the semi-major axis of the ellipse. True / False.

Velocity of a travelling wave on a string ‘v’ is related to the tension T and the linear mass density ‘m’ as: v2 = T * mA4. True / False.

If two wave pulses, approaching each other, are identical in shape except that one is inverted with respect to the other, at some instant displacement of all particles will be zero. True / False

Equation of a transverse wave travelling in a rope is given by y = 4 sin (5.0 t - 0.01 x), where y and x are expressed in cm and time in seconds. The amplitude and wavelength are A9 and (A10)π cm. And, the maximum transverse speed and maximum acceleration of a particle on the rope are A11 cm/s and A12 cm/s2, respectively.

A fluid has bulk modulus of 4 * 109 Pa and density 103 kg/m3. The speed of sound in that fluid is 10 * (A10) m/s. True / False.

By Newton`s Formula the speed of sound at one atmospheric pressure is nearly 280 m/s. CP/CV for air is 7/4. The actual speed of sound in air is nearly A13 m/s.

The amount of energy which flows perpendicular to a plane per unit area per unit time in a wave is proportional to A14 power of frequency of the wave and A15 power of the amplitude of displacement of particle of the wave.

Radio waves, X-rays; Light waves; Sound waves; Gamma rays. Among those mentioned here A9 waves are non-mechanical. True / False.

Sheet B

The density of the core of a planet is ρ1 and that of the outer shell is ρ2, the radii of the core and that of the planet are R and 2R respectively. The acceleration due to gravity at the surface of the planet is the same as that at a depth R. The ratio of density ρ1/ρ2 is 7/B1.

A planet revolving around a very massive star in a circular orbit of radius R with a period of revolution T. If the gravitational force of attraction between the planet and the star is proportional to R-2.5, then T is proportional to 7/(1+B1). True / False.

A wave is travelling along the X-axis. The disturbance at x = 0 and t = 0 is A/2 and is increasing, where A is amplitude of the wave. If y = A sin (kx - wt + φ), the initial phase φ = π / (A9 + A14). True /False.

A long string of mass per unit length 0.01 kg/m is subject to a tension of 64 N along the x-axis. One end (x=0) of this string is attached to a vibrator moving in a transverse direction at a frequency of 20 Hz. At t = 0; x = 0, the particle is at maximum displacement y = 1.0 cm. The magnitude of velocity of the particle at x = 50 cm, at time t = 0.05s is B2 *2 cm/s.

A travelling wave is given by  Y = 0.8 / (3x2 + 24xt + 48t2 + 4)  where x and y are in metres and t is in second. The wave speed is (A3)2. True / False.

A sky-diver falls with a terminal speed B3 m/s carrying a buzzer emitting a steady tone at 1800 Hz. The speed of sound is 343 m/s. A friend of a skydiver on the ground receives waves of frequency 2150 Hz. The sky-diver also records the frequency of sound reflected by the ground B4 Hz.

Sheet C

Two pulses y1 and y2 travel on the same string.

Y1= 5 / [(3x - 4t)2+2] and Y2 = - 5 / [(3x + 4t - 6)2 + 2]
At time 3 / C1 second the displacement of all particles will be zero i.e. the two pulses cancel everywhere. Position x = C2 metre is a node (permanent).

In the previous Q, Y1 and Y2 pulses travel in the same direction.True / False.

Two waves y1 and y2 superimpose to give the resultant wave, y1 = A sin (kx - wt); y2 = A sin (kx - wt + φ). The resultant of the two waves y1 and y2 has amplitude 2A sin (φ/2). True / False.

In a sono-meter, l1 and l2 are two successive resonance lengths. N0 is the frequency of oscillating sources. The wave velocity is C3 * n0 * (l2 - l1). (l2 > l1)

The fundamental frequency of a sono-meter wire increases by 6 Hz if the tension is increased by 44 %, keeping the length constant. The change in fundamental frequency of the sonometer is | A5 + A6 + A7 | hz when the length of wire is increased by 20 %, keeping the original tension in the wire constant. True / False.

The length of a pipe is l = 85 cm. The speed of sound is 340 m/s. When the pipe is open at both ends the 2nd harmonic frequency is 2 * A10 Hz and the third harmonic frequency is 3 * A12 Hz. True / False.

In the previous question, the sqrt (B4)th harmonic is C4 * 100 hz in an open pipe. The sqrt (B4)th harmonic does not exist for a closed pipe. True / False.

An open pipe 40 cm long and a closed pipe 31 cm long, both having the same diameter, are producing their first overtone, and they are in unison. The end correction of these pipes is C3 cm. True / False.

Answer Key

A1 = -1, A2 = 3, A3 = -2, A4 = 1, A5 = 1, A6 = -3, A7 = -1, A8 = 122

Q 2. True
Q 4. True
Q 5. False
Q 6. True
Q 8. True
Q 11. False

B1 = 3, B2 = 20 π, B3 = 56, B4 = 2501

Q 2. True
Q 3. True
Q 5. True

C1 = 4, C2 = 1, C3 = 2 

Q 2. False
Q 3. False
Q 6. False
Q 7. True
Q 8. True
Q 9. False
""")
