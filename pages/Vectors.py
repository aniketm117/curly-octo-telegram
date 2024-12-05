import streamlit as st

# Vectors

"""## Vectors

Many quantities we think about daily can be described by a single number: temperature, speed
, mass, weight and height. There are also many other concepts we encounter daily that cannot be
 described with just one number. For instance, a weather forecaster often describes wind with
  its speed and its direction. 

When applying a force, we are concerned with both the magnitude and direction of that force.
 In both of these examples, direction is important. Because of this, we study vectors,
  mathematical objects that convey both magnitude and direction information.

One "bare--bones'' definition of a vector is based on what we wrote above: "a vector
is a mathematical object with magnitude and direction parameters.'' This definition
 leaves much to be desired, as it gives no indication as to how such an object is to 
 be used."""

with st.expander("Q 1.	At what angle three forces of equal magnitude may act so that their"
                 " resultant is equal to zero."):

    st.info("""**Symmetry:**
    
            We can see by symmetry that if the forces are inclined to each other at
            120 degrees then their sum would be null vector.""")

with st.expander("Q 2.	Can the resultant of three unequal forces be equal to zero ?"):
    st.info("""**Triangle Law of Vector Addition:**
            
            Yes, if they can form a triangle.""")

with st.expander("Q 3.	There are three forces 4N, 5N and 10 N, can their resultant be equal to zero?"):
    st.info("""**Triangle Law of Vector Addition:**
            
             No, these forces cannot form a triangle.""")
