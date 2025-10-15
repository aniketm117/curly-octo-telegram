import streamlit as st
import sympy as sy
from sympy import symbols as symb

st.info("🎯 All Questions mentioned are Multiple choices Single correct type")

tabs = st.tabs(['Section A', 'Section B', 'Section C'])

with tabs[0]:
    """
    ## Intro to Kinematics
      
        Natural and Imaginary world is full of amazing phenomena. The concepts which we are going to learn can be applied in
        
        - Prediction of trajectory of a Space X Rocket successfully returning to Earth
    
    [Space X Rocket](https://www.youtube.com/watch?v=lEr9cPpuAx8)
    
        - Estimation of maximum velocity of water particles arising from geyser shooting periodically
        
    [Geyser shooting up in Iceland](https://youtu.be/JagzNA2oG20)
    
        Prerequisites for the lesson: If you are beginner in **vectors** you can jump ahead, otherwise you
        can watch my lecture on vectors linked below. Watch the lecture on 1.5X speed as I construct ideas rather slowly.
        
    [Vectors Playlist]("https://www.youtube.com/playlist?list=PLW8MJVksa5J_ZVghf9v7eB-xN_dUgzVcj)
    
    ### Frame of Reference
    
        - A frame of reference is a set of three mutually perpendicular axes which intersect at origin (named O), 
        along with a clock to measure time. 
        
        - For Competitive examinations or Boards, we commonly use the same coordinate system which you might have 
        studied in Class X. 
        
        - The frame of reference can be attached to a particle or to a rigid body or fixed in space 
        and therefore provide an "absolute" point of view when studying motion of other objects.
        
    ![coordinate system](https://i.ibb.co/CQfRd7r/coordinate-system.jpg "coordinate-system")
        
    #### Position
    
        - The coordinates of the particle (x,y,z) relative to the origin (O) is the position of the particle.
     
        - The values x, y and z represent the distance to be moved from the origin along the respective axis to reach the 
          particle. For example, (2,3,9) m represents the particle can be found by moving 2m along x axis, 3m along y axis, and 9m along z 
          axis, in no particular order (i.e. any order). 
    
        - Position of a particle can be represented as **a vector**, where if (x,y,z) is the position of the particle then the corresponding vector is,
    
    ![position](https://i.ibb.co/sKFzGwk/position.jpg "position")
    
        Say the position vector or (simply) the position of an imaginary star at (2,3,9)ly (ly=light year) as seen
        by the Sun is,
        
    ![pos1](https://i.ibb.co/j5Cz9z8/pos1.jpg "pos1")
    
        The Position of a particle moving on a straight line can be represented by x, where x > 0 represents the particle 
        existing on the positive side and x < 0 represents the particle existing on the negative side of the origin ( x = 0 
        ).
        
    ![Star_Wars](https://i.ibb.co/2Pvr87S/Star-Wars.jpg "Star_Wars")

        The position of the particle can be a "function" of time, which is a fancy (or mathematical) way of saying that the position of the particle depends on / varies with time.
    
    ![pos2](https://i.ibb.co/sCZs74r/pos2.jpg "pos2")
    
        In the above equation, if we use t=1 then we will get the position of the particle at that time.
    
    ![pos3](https://i.ibb.co/bm6MySh/pos3.jpg "pos3")
    
        - We can substitute any other value of t to get the the corresponding position of the particle. 
        
        - Try to find the time at which the particle whose position is given below crosses origin.
    

    ![Q1](https://i.ibb.co/8cThJy8/Q1.jpg "Q1")
    
        - Using guesswork, we can say that the particle would cross the origin at t=1. Perhaps their is some other way to do 
        this exercise without just guessing. 
    

    ![A1](https://i.ibb.co/gRhBckS/A1.jpg "A1")
    
        - Next, try to find the time at which the particle whose position is given below <i>crosses origin</i>.
    
    ![Q2](https://i.ibb.co/Fm4sWRV/Q2.jpg "Q2")
        
        - At first we observe that the unit vectors in the expression are not grouped. So the first step should be to group them to reach an intermediate stage. 
    
    ![A2](https://i.ibb.co/8NVYfh6/A2.jpg "A2")
    
        - Now each expression within the bracket can be equated with the corresponding coordinate to get the time(s) at which the value of expression would be equal to the coordinate.
    
    ![A2A](https://i.ibb.co/cgTyK3t/A2A.jpg "A2A")
    
        - We can see that even though the motion of the particle is not easy to imagine we can find the time at which the particle can reach a certain position, if at all.
    
    ## Distance
    
        - The total path length of the path traversed by a particle in going from initial to final position is called the Distance covered by the particle.
        
        - Find the distance covered by the particle in going from P to Q along the circle. And, find the distance covered by the particle by the particle in going from P to Q along the diameter.
    
    ![Q3](https://i.ibb.co/37JH3qT/Q3.jpg "Q3")
        
    ## Displacement
    
        - Displacement of a particle is defined as <i>the shortest distance</i> between initial and final position, alongwith a direction from the initial to final position. Displacement of a particle in going from initial to final position is <i>independent</i> of the path taken, which is beacuse of the way it is defined. In the example drawn below a particle goes from r1 to r2, and the displacement is equal to r2 - r1. 
    
    ![Disp](https://i.ibb.co/h79Zj8t/Disp.jpg "Disp")
    
        -  For example, if the position of a particle is x = 2t unit, where t is time (in second) then the displacement of the particle between 2s and 4s is x(final) - x(initial) = 2 * 4 - 2 * 2 = 4 unit. Akin to position, displacement of a particle moving in straight line can be either positive or negetive. Generalization of displacement in two dimensions,
    
    ![Disp2](https://i.ibb.co/8rNxXKC/Disp2.jpg "Disp2")
    
        Take an example,
    
    ![Disp3](https://i.ibb.co/Y8QyB87/Disp3.jpg "Disp3")
    
        The displacement of a particle is made up of two components, the magnitude and the direction. The direction of the
         displacement could simply be something like North, 30° East of South etc., or it can be represented as follows,
        
    ![Direction](https://i.ibb.co/2KZTj05/Direction.jpg "Direction")
    
    #### A twist in subjective IIT-JEE Question
    
        Find the ratio of the magnitude of the displacement and the distance covered by the particle as it goes along the
         path ABC from A to C.
        
    ![Q4](https://i.ibb.co/x60vLGT/Q4.jpg "Q4")
    """
    st.page_link("https://aniketm117.github.io/github-pages-with-jekyll/2023/02/09/long-time-no-post.html",
                 label="Is this a Question of Kinematics ?"
                 )

with tabs[1]:
    """  
    ## Differentiation

        - '\u0394y' represents the displacement of a particle at an instant then the term '\u0394y/\u0394x' represents the average 
        velocity of the particle om the time interval \u0394x. 
        
        - Time interval \u0394x = x\u2082 - x\u2081.
        
        - In the limiting case x\u2081 and x\u2082 are infinitesimally close to each other '\u0394y/\u0394x' becomes dy/dx,
        which implies we have determined the instantaneous velocity of the particle at an instant.
    
        - Refer to section A for an explainer on displacement of a particle.
    
        - dy/dx refers to differentiation of y wrt x or derivative of y wrt x.
    
    """
    st.latex("Q1. d(x)/dx =")

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

    st.latex("Q2. d(x\u207F)/dx =")

    A_5, A_6, A_7, A_8 = st.columns(4)

    with A_5:
        if st.button("x", key=A_5, use_container_width=True):
            st.warning("Try Again")
    with A_6:
        if st.button("n * x ^ (n-1)", key=A_6, use_container_width=True):
            st.success("✔️")
    with A_7:
        if st.button("n * x\u207F", key=A_7, use_container_width=True):
            st.warning("Try Again")
    with A_8:
        if st.button("None", key=A_8, use_container_width=True):
            st.warning("Try Again")

    st.latex("Q3. d(cos(x))/dx =")

    A_9, A_10, A_11, A_12 = st.columns(4)

    with A_9:
        if st.button("tan (x)", key=A_9, use_container_width=True):
            st.warning("Try Again")
    with A_10:
        if st.button("sin (x)", key=A_10, use_container_width=True):
            st.warning("Try Again")
    with A_11:
        if st.button(" (-1) * sin (x)", key=A_11, use_container_width=True):
            st.success("✔️")
    with A_12:
        if st.button("cosec ^2 (x)", key=A_12, use_container_width=True):
            st.warning("Try Again")

    st.latex("Q4. d(sin(A*x))/dx = ")

    A_13, A_14, A_15, A_16 = st.columns(4)

    with A_13:
        if st.button("A * sin(A*x)", key=A_13, use_container_width=True):
            st.warning("Try Again")
    with A_14:
        if st.button("A + sin(A*x)", key=A_14, use_container_width=True):
            st.warning("Try Again")
    with A_15:
        if st.button("A * cos(A*x)", key=A_15, use_container_width=True):
            st.success("✔️")
    with A_16:
        if st.button("A * cosec(A*x)", key=A_16, use_container_width=True):
            st.warning("Try Again")

    A1, A2, A3 = st.columns(3)

with tabs[2]:
    ""

sentiment_mapping = [0, 1]
selected = st.feedback("thumbs")
if selected is not None:
    st.markdown("Thanks for your feedback!")
