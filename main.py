import streamlit as st

st.title('🏗️ Q&A on Vectors ')

disclaimer = "Answer"

with st.expander("Q 1.	At what angle three forces of equal magnitude may act so that their resultant is equal to zero."):
    st.info("120 degrees")

with st.expander("Q 2.	Can the resultant of three unequal forces be equal to zero ?"):
    st.info("Yes, if they can form a triangle.")

with st.expander("Q 3.	There are three forces 4N, 5N and 10 N, can their resultant be equal to zero?"):
    st.info("No, these forces cannot form a triangle.")

with st.expander("Q 4.	There are three forces 4N, 6N and 8 N can their resultant be equal to zero."):
    st.info("Yes")

with st.expander("Q 5.	Can the resultant of two unequal forces be equal to zero."):
    st.info("No")

with st.expander("Q 6.	Can a east – ward directed force be balanced by a north – ward directed force."):
    st.info("No")

with st.expander("Q 7.	Can the resultant of two forces 10 N and 6 N be equal to"
                 "(a) 3N 	(b) 4N 	(c) 8N 	(d) 16 N   (e) 18 N"):
    st.info("The resultant of 10 N and 6 N would lie between (10 + 6) N and (10 - 6) N so it can be"
             " 4 N, 8 N, and 16 N.")

with st.expander("Q 8.	In the above problem what will be the minimum and maximum value of the resultant."):
    st.info("4 N and 16 N")

with st.expander("Q 9.	The maximum and minimum numerical value of the resultant of two forces are"
                 " respectively 16N and 4N, then calculate the numerical value of the individual forces."):
    st.info("10 N and 6 N")

with st.expander("Q 10.	In the above problem what would be the numerical value of the resultant, if the"
                 " two forces acts at right angle to each other."):
    st.info("sqrt(136)")

with st.expander("Q 11.	The magnitudes of the three vectors A, B and C are respectively 12N, 5N and 13 N"
                 " and if A + B = C, then what is the angle between vectors A and B ?"):
    st.info("90 degrees")

with st.expander("Q 12.	The magnitude of three vector A, B and C are respectively 3N, 4N and 5N and if"
                 " A + B = C, then what is the angle between A and C ?"):
    st.info("37 degrees")

with st.expander("Q 13.	In the above problem what could be the angle between vector A and B."):
    st.info("90 degrees")

with st.expander("Q 14.	A particle is displaced by 4 m in the south west direction and then by 5 m east"
                 " and the lastly through 6 m in a direction 60o north of east Calculate the total"
                 " displacement from the starting point."):
    st.info("The total displacement is approximately 5.69 m in a direction 25° north of east")

with st.expander("Q 15.	A cricket ball is bowled on a 22 yard pitch along the pitch,"
                 " in a straight line. Afterwards it is hit back in the direction which it came from."
                 " The bowler stops the ball at the initial starting point. The displacement vector for "
                 "the whole motion is"):
    st.info("Zero vector")

with st.expander("Q 16.	A golfer dips the ball into the hole in three successive strokes. His first"
                 " stroke displaces the ball 4m north, the second stroke 2 m south east, and the last"
                 " stoke 1 m south west. Calculate what displacement was needed to put the ball into"
                 " the hole on the 1st stroke."):
    st.info("The displacement needed to put the ball into the hole on the first stroke is approximately"
            " 2.00 m in a direction 69° north of east")

with st.expander("Q 17.	A man ran 2.0 kilometer towards east, then making a perpendicular left "
                 "turn he ran 500 m and then he ran 4.0 km. after making perpendicular right turn."
                 " Calculate his total displacement."):
    st.info("The man's total displacement is approximately 6.02 km in a direction 4.8° north of east")

with st.expander("Q 18.	The co-ordinates of the initial and final point of a given vector are respectively (2, 3) and (10, 6). Then calculate the magnitude of the vector."):
    st.write(disclaimer)

with st.expander("Q 19.	There are two vectors whose magnitude are respectively 2m and 4m the angle between them is 30o. Calculate (1) scalar product of the two vectors and (2) the magnitude of their vector products."):
    st.write(disclaimer)

with st.expander("Q 20.	Find the components of a vector A which makes equal angles with the x, y and z axis. "):
    st.write(disclaimer)

with st.expander("Q 21.	A body of mass 5 kg moves from position 1 metre to a position 8 metre due to a force 10 Newton. Calculate the work done."):
    st.write(disclaimer)

with st.expander("Q 22.	Three equal forces each of value 1 newton acts along the side BC, CD and DE of a regular hexagon ABCDEF. Calculate the magnitude of their resultant."):
    st.write(disclaimer)

with st.expander("Q 23.	If the co-ordinate of a moving particle are given by x = at2, and y = bt2, the calculate the speed of the particle."):
    st.write(disclaimer)

with st.expander("Q 24.	Calculate the displacement, when we finally lie down on our bed in the night since the time we rose form the same bed in the morning."):
    st.write(disclaimer)

with st.expander("Q 25.	M and N are two sites few kilometers apart on a perfectly flat plane road. A girl takes off from M in a helicopter circles around, and then lands at N; while on the other hand a man walks from M to N; compare their displacements."):
    st.write(disclaimer)

with st.expander("Q 26.	Is it correct that, “the magnitude of the sum of two vectors must be greater than the magnitude of either vectors ?"):
    st.write(disclaimer)

with st.expander("Q 27.	Is it correct that the component of a vector is a vector ? "):
    st.write(disclaimer)

with st.expander("Q 28.	Is it correct to say that if a vector is zero then each of its rectangular components must be zero?"):
    st.write(disclaimer)

st.balloons()
