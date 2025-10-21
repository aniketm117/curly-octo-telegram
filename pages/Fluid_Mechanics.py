import streamlit as st
import sympy as sy
from sympy import symbols as symb

dens, dens_w, r_dens, fo, ar, press = symb('ρ ρ_w ρ_r F A P')

prompt = "Please enter the requisite value"

"""
## Fluid Mechanics

    One of the first things we observe in a fluid is its density. Will the fluid stay above water or below it when 
    is brought together with water ? 
    
    Density of a fluid is defined as the ratio of its mass and volume. However they are other ways of defining densities
    as well like Relative density which tell us whether the fluid is lighter or heavier.
    
    This brings us awareness of the world around us that air is a fluid, lighter than water. Water vapour which 
    compose the clouds are lighter than air.
"""

tabs = st.tabs(['Fluid Statics', 'Streamline & Turbulent Flow', 'Fluid Dynamics',
                'Surface Tension', 'Viscosity & Terminal Velocity'])

with tabs[0]:
    """
    ## Fluid Statics
     
        - Relative Density (ρ_r) = Density of the substance (ρ) / Density of water at triple point (ρ_w)         
    """

    expr = dens / dens_w
    expr2 = r_dens
    eq = sy.Eq(expr, expr2)
    st.latex(f"{expr2}={expr}")

    Fluids = {'Mercury': 13600, 'Water': 1000, 'Kerosene Oil': 800, 'Castor Oil': 650, 'Honey': 2000, 'Blood': 890}

    st.bar_chart(data=Fluids, x_label='Fluids', y_label='Densities')

    """
    #### Pressure
        
        - Pressure exerted by a Force is defined as the **normal** force per unit area of the surface on which 
        the force is acting.
        - When a bomb explodes in relatively open spaces the forces exerted by the particles on its surroundings acts  
        on a larger area.
        - If it explodes in a confined space the forces remaining the same, have a smaller area to contend with
        which results in higher pressure.
        
        A Force 'F_net' whose perpendicular component is 'F' acts on a surface of area 'A' then the Pressure 'P' acting on
        the surface is given by 
    
    """

    expr3 = fo / ar
    expr4 = press
    eq_1 = sy.Eq(expr3, expr4)
    st.latex(f"{expr3}={expr4}")

    """
    #### Units of Pressure
    
        - SI unit of pressure is 1 newton / m^2 which is equal to 1 Pascal.
        
        - A Force 'F' is acting on a surface area of 20 cm^2. F = 50 newton acts at angle of 30 degree to the normal.
        If 25 * sqrt(3) = 43.3, then find the pressure acting on the surface by entering the info below.
        
    """

    Area = 0.1

    clmn1, clmn2 = st.columns(2)

    with clmn1:
        try:
            F1 = float(st.text_input(label='Enter Force',
                                     key='F1',
                                     placeholder='Enter the force in Newton'
                                     ))
        except ValueError:
            F1 = 50

    with clmn2:
        try:
            Area = float(st.text_input(label='Enter Area',
                                       key='A1',
                                       placeholder='Enter the area in SI units'
                                       ))
        except ValueError:
            Area = 0.1

    expr5 = F1 / Area

    st.latex(f" Pressure = {expr5}")

    if expr5 == 43.3 / 0.002:
        st.success("✔️")
    else:
        st.info("Try Again")

    """
        #### Atmospheric Pressure and Barometer

            - The pressure exerted by air on the objects at sea level is defined as atmospheric pressure. It is quiet
            imperceptible as its value is less in comparison to pressures which operate around us like the pressure 
            inside the tyres of an airplane, or pressure exerted by water jet on hydro power plant turbines.

            - Its value is measured in 1 cm of Hg. Barometer is a device used to measure atmospheric measure using a
            sufficiently long transparent tube closed at one end and open at another, dipped in a slurry of Hg. 
            
            - Closed end at the top has vacuum. Hg is drawn inside the tube because of the vacuum and it fills up to a 
            height which balances the atmospheric pressure acting at the bottom of the tube.
    
        ![Q4](https://i.ibb.co/x60vLGT/Q4.jpg "Q4")
            
        ###### Q1. 
            If Mercury (Hg) in a Barometer is replaced with a liquid of lower density then the height of the column of 
            the new liquid would .... in comparison to that of the earlier Hg column.
             
    """
    A_1, A_2, A_3, A_4 = st.columns(4)

    with A_1:
        if st.button("be higher",
                     key=A_1,
                     use_container_width=True):
            st.success("Correct")

    with A_2:
        if st.button("be lower",
                     key=A_2,
                     use_container_width=True):
            st.warning("Try Again")

    with A_3:
        if st.button("remain same",
                     key=A_3,
                     use_container_width=True):
            st.warning("Try Again")

    with A_4:
        if st.button("None",
                     key=A_4,
                     use_container_width=True):
            st.warning("Try Again")

    """
            
        #### Archimede`s Principle
        
            - When a body is immersed in a fluid then the upthrust exerted by the fluid on the the object 
            is equal to the weight of the fluid displaced by the body. 
            
    """

    F_b, V, g = symb('Force Volume g')

    expr6 = V * dens * g
    expr7 = F_b
    eq_2 = sy.Eq(expr6, expr7)
    st.latex(f"{expr6}={expr7}")

with tabs[1]:
    """
    ## Streamline and Turbulent FLow
     
        - Relative Density (ρ_r) = Density of the substance (ρ) / Density of water at triple point (ρ_w)         
    """

    expr = dens / dens_w
    expr2 = r_dens
    g = sy.Eq(expr, expr2)
    st.latex(f"{expr2}={expr}")

    """
    #### Pressure & Atmospheric Pressure
        
        - Pressure exerted by a Force is defined as the **normal** force per unit area of the surface on which 
        the force is acting.
        - When a bomb explodes in relatively open spaces the forces exerted by the particles on its surroundings acts  
        on a larger area.
        - If it explodes in a confined space the forces remaining the same, have a smaller area to contend with
        which results in higher pressure.
        
        A Force 'F_net' whose perpendicular component is 'F' acts on a surface of area 'A' then the Pressure 'P' acting on
        the surface is given by
    
    """

    expr3 = fo / ar
    expr4 = press
    h = sy.Eq(expr3, expr4)
    st.latex(f"{expr3}={expr4}")

    """
    #### Units of Pressure
    
        - SI unit of pressure is 1 newton / m^2 which is equal to 1 Pascal.
        
        - A Force 'F' is acting on a surface area of 20 cm^2. F = 50 newton acts at angle of 30 degree to the normal.
        If 25 * sqrt(3) = 43.3, then find the pressure acting on the surface by entering the info below.
        
    """

    F1 = 50
    Area = 0.002

    try:
        F1 = float(st.text_input(label='Enter Force',
                                 key='F2',
                                 placeholder='in Newton',
                                 disabled=True))
    except ValueError:
        st.info(prompt,
                icon="🙀")

    try:
        Area = float(st.text_input(label='Enter Area',
                                   key='A2',
                                   placeholder='Enter the area in SI units',
                                   disabled=True))
    except ValueError:
        st.info(prompt,
                icon="🙀")

    expr5 = F1 / Area

    st.latex(f" Pressure = {expr5}")

with tabs[2]:
    """
    ## Fluid Dynamics
     
        - Relative Density (ρ_r) = Density of the substance (ρ) / Density of water at triple point (ρ_w)         
    """

    expr = dens / dens_w
    expr2 = r_dens
    g = sy.Eq(expr, expr2)
    st.latex(f"{expr2}={expr}")

    """
    #### Pressure & Atmospheric Pressure
        
        - Pressure exerted by a Force is defined as the **normal** force per unit area of the surface on which 
        the force is acting
        - When a bomb explodes in relatively open spaces the forces exerted by the particles on its surroundings acts  
        on a larger area.
        - If it explodes in a confined space the forces remaining the same, have a smaller area to contend with
        which results in higher pressure.
        
        A Force 'F_net' whose perpendicular component is 'F' acts on a surface of area 'A' then the Pressure 'P' acting on
        the surface is given by 
    
    """

    expr3 = fo / ar
    expr4 = press
    h = sy.Eq(expr3, expr4)
    st.latex(f"{expr3}={expr4}")

    """
    #### Units of Pressure
    
        - SI unit of pressure is 1 newton / m^2 which is equal to 1 Pascal.
        
        - A Force 'F' is acting on a surface area of 20 cm^2. F = 50 newton acts at angle of 30 degree to the normal.
        If 25 * sqrt(3) = 43.3, then find the pressure acting on the surface by entering the info below.
        
    """

    F1 = 50
    Area = 0.002

    clmn1, clmn2 = st.columns(2)

    with clmn1:
        try:
            F1 = float(st.text_input(label='Enter Force',
                                     key='F3',
                                     placeholder='in Newton',
                                     disabled=True))
        except ValueError:
            F1 = 50

    with clmn2:
        try:
            Area = float(st.text_input(label='Enter Area',
                                       key='A3',
                                       placeholder='Enter the area in SI units',
                                       disabled=True
                                       ))
        except ValueError:
            Area = 0.002

    expr5 = F1 / Area

    st.latex(f" Pressure = {expr5}")

with tabs[3]:
    """
    ## Surface Tension
     
        - Relative Density (ρ_r) = Density of the substance (ρ) / Density of water at triple point (ρ_w)         
    """

    expr = dens / dens_w
    expr2 = r_dens
    g = sy.Eq(expr, expr2)
    st.latex(f"{expr2}={expr}")

    """
    #### Pressure & Atmospheric Pressure
        
        - Pressure exerted by a Force is defined as the **normal** force per unit area of the surface on which 
        the force is acting.
        - When a bomb explodes in relatively open spaces the forces exerted by the particles on its surroundings acts  
        on a larger area.
        - If it explodes in a confined space the forces remaining the same, have a smaller area to contend with
        which results in higher pressure.
        
        A Force 'F_net' whose perpendicular component is 'F' acts on a surface of area 'A' then the Pressure 'P' acting on
        the surface is given by 
    
    """

    expr3 = fo / ar
    expr4 = press
    h = sy.Eq(expr3, expr4)
    st.latex(f"{expr3}={expr4}")

    """
    #### Units of Pressure
    
        - SI unit of pressure is 1 newton / m^2 which is equal to 1 Pascal.
        
        - A Force 'F' is acting on a surface area of 20 cm^2. F = 50 newton acts at angle of 30 degree to the normal.
        If 25 * sqrt(3) = 43.3, then find the pressure acting on the surface by entering the info below.
        
    """

    F1 = 50
    Area = 0.002
    try:
        F1 = float(st.text_input(label='Enter Force',
                                 key='F4',
                                 placeholder='in Newton',
                                 disabled=True))
    except ValueError:
        st.info(prompt,
                icon="🙀")

    try:
        Area = float(st.text_input(label='Enter Area',
                                   key='A4',
                                   placeholder='Enter the area in SI units',
                                   disabled=True
                                   ))
    except ValueError:
        st.info(prompt,
                icon="🙀")

    expr5 = F1 / Area

    st.latex(f" Pressure = {expr5}")

with tabs[4]:
    """
    ## Viscosity and Terminal Velocity
     
        - Relative Density (ρ_r) = Density of the substance (ρ) / Density of water at triple point (ρ_w)         
    """

    expr = dens / dens_w
    expr2 = r_dens
    g = sy.Eq(expr, expr2)
    st.latex(f"{expr2}={expr}")

    """
    #### Pressure & Atmospheric Pressure
        
        - Pressure exerted by a Force is defined as the **normal** force per unit area of the surface on which 
        the force is acting.
        - When a bomb explodes in relatively open spaces the forces exerted by the particles on its surroundings acts  
        on a larger area.
        - If it explodes in a confined space the forces remaining the same, have a smaller area to contend with
        which results in higher pressure.
        
        A Force 'F_net' whose perpendicular component is 'F' acts on a surface of area 'A' then the Pressure 'P' acting on
        the surface is given by 
    
    """

    expr3 = fo / ar
    expr4 = press
    h = sy.Eq(expr3, expr4)
    st.latex(f"{expr3}={expr4}")

    """
    #### Units of Pressure
    
        - SI unit of pressure is 1 newton / m^2 which is equal to 1 Pascal.
        
        - A Force 'F' is acting on a surface area of 20 cm^2. F = 50 newton acts at angle of 30 degree to the normal.
        If 25 * sqrt(3) = 43.3, then find the pressure acting on the surface by entering the info below.
        
    """

    F1 = 50
    Area = 0.002
    try:
        F1 = float(st.text_input(label='Enter Force',
                                 key='F5',
                                 placeholder='in Newton',
                                 disabled=True))
    except ValueError:
        st.info(prompt,
                icon="🙀")

    try:
        Area = float(st.text_input(label='Enter Area',
                                   key='A5',
                                   placeholder='Enter the area in SI units',
                                   disabled=True
                                   ))
    except ValueError:
        st.info(prompt,
                icon="🙀")

    expr5 = F1 / Area

    st.latex(f" Pressure = {expr5}")

    data = {'Reynolds Number': [6000, 5000, 4000, 3000, 2000, 1000],
            'Viscosity': [0.166, 0.2, 0.25, 0.333, 0.5, 1]}

    option = st.selectbox("Select the data to be shown on x-axis",
                          ['Reynolds Number', 'Viscosity'])

    if option == 'Reynolds Number':
        option_2 = 'Viscosity'
    else:
        option_2 = 'Reynolds Number'

    st.line_chart(data, x=option, y=option_2)

# Questions and Answers

with st.expander("Q 1. If you had to design pipes used to transport water a boiler in power plant , "
                 "what dimensional and material specifications would you consider ?"):
    st.write('')

with st.expander("Q 2. If a student plots a graph of Reynolds Number versus coefficient of viscosity of a fluid "
                 "for a given density of the fluid, speed of fluid, and diameter of the pipe, what would the graph look"
                 " like ?"):
    st.write('')
