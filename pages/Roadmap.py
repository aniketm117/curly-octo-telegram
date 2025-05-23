import graphviz
import streamlit as st


st.write("### Roadmap")
st.write("The possible pathways one can take to complete their Physics prep for "
         "whatever goal one may be aspiring to in XI and XII Class.")

# Create a graphlib graph object

graph = graphviz.Digraph()

graph.edge('Start', 'Units and Dimension')
graph.edge('Units and Dimension', 'Vectors')
graph.edge('Units and Dimension', 'Differentiation & Integration')
graph.edge('Vectors', 'Kinematics')
graph.edge('Differentiation & Integration', 'Kinematics')
graph.edge('Vectors', 'Laws of Motion')
graph.edge('Kinematics', 'Laws of Motion')
graph.edge('Laws of Motion', 'Work and Energy')
graph.edge('Work and Energy', 'System of Particles and Rotational Motion')
graph.edge('System of Particles and Rotational Motion', 'Gravitation')
graph.edge('Gravitation', 'Mechanical Properties of Fluids')
graph.edge('Mechanical Properties of Fluids', 'Mechanical Properties of Solids')
graph.edge('Mechanical Properties of Solids', 'Thermal Properties of Matter')
graph.edge('Gravitation', 'Kinetic Theory of Gases')
graph.edge('Thermal Properties of Matter', 'Kinetic Theory of Gases')
graph.edge('Kinetic Theory of Gases', 'Thermodynamics')
graph.edge('Thermodynamics', 'Oscillations')
graph.edge('Oscillations', 'Waves')
graph.edge('Waves', 'Electric Charges and Field')
graph.edge('Gravitation', 'Electric Charges and Field')
graph.edge('Electric Charges and Field', 'Electric Potential and Capacitance')
graph.edge('Electric Potential and Capacitance', 'Current Electricity')
graph.edge('Current Electricity', 'Moving Charges and Magnetism')
graph.edge('Moving Charges and Magnetism', 'Magnetism and Matter')
graph.edge('Moving Charges and Magnetism', 'Electromagnetic Induction')
graph.edge('Electromagnetic Induction', 'Alternating Current')
graph.edge('Alternating Current', 'Electromagnetic Waves')
graph.edge('Waves', 'Electromagnetic Waves')
graph.edge('Electromagnetic Waves', 'Ray Optics')
graph.edge('Ray Optics', 'Wave Optics')
graph.edge('Wave Optics', 'Dual Nature of Matter')
graph.edge('Dual Nature of Matter', 'Atoms')
graph.edge('Atoms', 'Nuclei')
graph.edge('Nuclei', 'SEMICONDUCTOR ELECTRONICS')
graph.edge('SEMICONDUCTOR ELECTRONICS', 'Fin')

st.graphviz_chart(graph)
