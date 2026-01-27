import streamlit as st
import sympy as sy
from sympy import symbols as symb

dens, dens_w, r_dens, fo, ar, press = symb('ρ ρ_w ρ_r F A P')

prompt = "Please enter the requisite value"

"""
## Fluid Mechanics

    One of the first things we observe in a fluid is its density. Will the fluid stay above water or below it when 
    is brought together with water ?
    
    Density of a fluid is defined as the ratio of its mass and volume. However there are other ways of defining densities
    as well like Relative density which tell us whether the fluid is lighter or heavier.
    
    This brings us awareness of the world around us that air is a fluid, lighter than water. Water vapour which 
    compose the clouds are lighter than air.
"""

tabs = st.tabs(['Fluid Statics', 'Streamline & Turbulent Flow', 'Fluid Dynamics', 'Surface Tension',
                'Viscosity & Terminal Velocity'])

with tabs[0]:
    """
    ### Fluid Statics
    
        - Relative Density (ρ_r) = Density of the substance (ρ) / Density of water at triple point (ρ_w)         
    """

    expr = dens / dens_w
    expr2 = r_dens
    eq = sy.Eq(expr, expr2)
    st.latex(f"{expr2}={expr}")

    Fluids = {'Mercury': 13600, 'Water': 1000, 'Kerosene Oil': 800, 'Castor Oil': 915, 'Honey': 1415, 'Blood': 1060}
    st.bar_chart(data=Fluids, x_label='Fluids', y_label='Densities')

    """
    #### Pressure
        
        - Pressure exerted by a Force is defined as the normal force per unit area of the surface on which 
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
    #### Pressure at a depth in a fluid 

        - The pressure at any depth 'h' inside a fluid of density ρ_1 is given by:

    """
    P, h, g, density = symb('P h g ρ_1')

    expr10 = h * density * g
    expr11 = P
    eq_2 = sy.Eq(expr10, expr11)
    st.latex(f"{expr10}={expr11}")

    """
    #### Example
    
        Try to evaluate the pressure at a depth of 'h' metre from one of the fluids in the selection box.
          
    """

    clmn3, clmn4 = st.columns(2)

    with clmn3:
        fluid_key = st.selectbox("Select the fluid",
                                 options=Fluids)

    with clmn4:
        h = st.slider("Select the height in metres", min_value=0, max_value=1000)

    st.latex("Pressure (in Pascal) = " + str(Fluids[fluid_key] * 10 * h))

    """
    #### Atmospheric Pressure and Barometer

        - The pressure exerted by air on the objects at sea level is defined as atmospheric pressure. It is quiet
        imperceptible as its value is less in comparison to pressures which operate around us like the pressure 
        inside the tyres of an airplane, or pressure exerted by water jet on hydro power plant turbines.

        - Its value is measured in 1 cm of Hg. Barometer is a device used to measure atmospheric measure using a
        sufficiently long transparent tube closed at one end and open at another, dipped in a slurry of Hg.
        
        - Closed end at the top has vacuum. Hg is drawn inside the tube because of the vacuum and it fills up to a 
        height which balances the atmospheric pressure acting at the bottom of the tube.
    """

    st.image("img/Mercury Barometer Display.png",
             caption='AI Image - Mercury Barometer',
             width=300
             )

    """        
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
    #### Pressure in U-tube columns
        
        -   Pressure difference between two points situated at a height difference 'h' inside the same fluid can be 
        calculated using the expression given below.
    """

    ht, P = symb('height ΔP')

    expr13 = ht * density * g
    expr14 = P
    eq_2 = sy.Eq(expr13, expr14)
    st.latex(f"{expr13}={expr14}=GaugePressure")

    """
    #### Absolute Pressure and Pressure at interface of two fluids

        -   In a U-tube manometer open on both sides as shown in the figure below.
        
        -   The pressure exerted by the fluid 1 at point A is P_A, it is the sum of atmospheric pressure of the 
        air above the fluid and the gauge pressure due to the fluid 1.
        
        -   The pressure exerted by the fluid 2 at point B is P_B.
        
        -   When considering pressure at the common surface of the two fluids say 1 and 2. The
         pressure exerted by the two fluids i.e. 1 and 2 equalize.
         
        -   Pressure exerted by fluid 2 at points A (common surface) and B is same because they lie at the same 
        horizontal level. Pressure inside a fluid at the same horizontal level is equal.           
    
    """

    st.image('img/Fluid Dynamics in U-Tube.png',
             caption='AI Image - Fluids in a U-tube',
             width=300)

    ht_1, ht_2, P_A, P_B, dens_1, dens_2, P_atm = symb('h_1 h_2 P_A P_B ρ_1 ρ_2 P_0')

    expr15 = P_atm + dens_1 * g * ht_1
    expr16 = P_atm + dens_2 * g * ht_2
    eq_3 = sy.Eq(expr15, expr16)
    st.latex(f"AbsolutePressure_A ={expr15}={P_A}")
    st.latex(f"AbsolutePressure_B ={expr16}={P_B}")
    st.latex(f"{expr15}={expr16}")

    """
    ###### Q2.
        In a U-tube water is poured to a certain level, then an unknown fluid (say X) whose density is 0.6 times the
        the density of water is filled in one of the arms. The height difference in the column of water and that of 
        unknown fluid is 5 cm. Then find the length of column 'X' poured over water.
    """

    try:
        length = float(st.text_input(label='Height of fluid X',
                                     placeholder='Enter the height in centimetre until a single decimal place'))
    except ValueError:
        length = 0

    if length == 12.5:
        st.success("Correct")
    else:
        st.info("Try Again")

    """
    ###### Q3.
        As per ideal gas law, P = k * T for a gas if it is maintained at constant volume (k is a positive constant). A 
        manometer contains Hg to a height 10 cm above the level in the other column. Find the change in temperature 'T' 
        of the gas if the height increases to 20 cm above the other column, consider the atmospheric pressure to be 
        negligible. [Initial Temperature = 273 K] 
    """

    try:
        T_1 = float(st.text_input(label='Change in temperature of the gas',
                                  placeholder='Enter the change in temperature in Kelvin'))
    except ValueError:
        T_1 = 100

    if T_1 == 273:
        st.success("Correct")
    else:
        st.info("Try Again")

    """            
    #### Archimede`s Principle
    
        - When a body is immersed in a fluid then the upthrust exerted by the fluid on the the object 
        is equal to the weight of the fluid displaced by the body.
        
        - We can understand this idea by thinking in a way that if the submerged part of the body was replaced by 
        the fluid itself which it is displacing then the fluid beneath the submerged body would "balance" the weight
        of the fluid.
        
        - So if the displaced fluid is replaced by the object then the fluid beneath should act no differently.
        
        - The upthrust or buoyant force acting on the body would be the same as the one acting on the fluid in its place which 
        is equal to the weight of the fluid.
            
    """

    F_b, V, g = symb('F_b Volume g')

    expr6 = V * dens * g
    expr7 = F_b
    eq_3 = sy.Eq(expr6, expr7)
    st.latex(f"{expr6}={expr7}")

    """        
        ###### Q4.
            
            Evaluate the buoyant force on a block of wood immersed in water if 200 cm^3 of its volume is 
            submerged in water. Density of water = 1000 kg / m^3, g = 10 m/s^2.

    """

    A_5, A_6, A_7, A_8 = st.columns(4)

    with A_5:
        if st.button("4 N",
                     key=A_5,
                     use_container_width=True):
            st.warning("Try Again")

    with A_6:
        if st.button("2 N",
                     key=A_6,
                     use_container_width=True):
            st.success("Correct")

    with A_7:
        if st.button("20 N",
                     key=A_7,
                     use_container_width=True):
            st.warning("Try Again")

    with A_8:
        if st.button("40 N",
                     key=A_8,
                     use_container_width=True):
            st.warning("Try Again")

    """
        #### Buoyant Forces on bodies with cavities & impurities

            - Upthrust forces exerted on the body by the fluids surrounding it is called the buoyant force.

            - For bodies composed of different materials or those having cavities within them, we can apply 
            this principle to evaluate the ratio of masses of the materials or the volume of the cavity.
            
            - Say an object is composed of two materials M_1 and M_2 of densities ρ_1 and ρ_2 , respectively
            then the total buoyant force exerted by water if it was completely submerged in water would be equal to 
    
    """

    F_b, ρ_1, ρ_2, V_1, V_2, g = symb('F_b ρ_1 ρ_2 V_1 V_2 g')

    expr8 = V_1 * dens_w * g + V_2 * dens_w * g
    expr9 = F_b
    eq_4 = sy.Eq(expr8, expr9)
    st.latex(f"{expr8}={expr9}")

    """
        #### Buoyant Forces on bodies with cavities & impurities 2
            
            - Note that we are not saying that the buoyant force would balance the weight of the object rather it exerts 
            a certain force equal to the weight of the fluid displaced which depends on the volume displaced by M_1 and
            M_2 combined. The oft used condition of flotation may cause this confusion.
            
    """

    """
        #### Pressure in vertically accelerated fluids

            - When a container is accelerated vertically if we imagine a hypothetical cylinder inside the fluid within 
            the container

            - For bodies composed of different materials or those having cavities within them, we can apply 
            this principle to evaluate the ratio of masses of the materials or the volume of the cavity.

            - Say an object is composed of two materials M_1 and M_2 of densities ρ_1 and ρ_2 , respectively
            then the total buoyant force exerted by water if it was completely submerged in water would be equal to 

        """

with tabs[1]:
    """
    ## Streamline and Turbulent FLow
     
        - Relative Density (ρ_r) = Density of the substance (ρ) / Density of water at triple point (ρ_w)         
    """

    data = {'Reynolds Number': [6000, 5000, 4000, 3000, 2000, 1000],
            'Viscosity': [0.166, 0.2, 0.25, 0.333, 0.5, 1]}

    option = st.selectbox("Graphs of Re and Viscosity if the product of speed of flow, density of fluid and diameter of"
                          " pipe is kept constant.",
                          ['Reynolds Number', 'Viscosity'])

    if option == 'Reynolds Number':
        option_2 = 'Viscosity'
    else:
        option_2 = 'Reynolds Number'

    st.line_chart(data, x=option, y=option_2)

with tabs[2]:
    """
    ## Fluid Dynamics
     
        - Relative Density (ρ_r) = Density of the substance (ρ) / Density of water at triple point (ρ_w)         
    """

with tabs[3]:
    """
    ## Surface Tension
     
        - Relative Density (ρ_r) = Density of the substance (ρ) / Density of water at triple point (ρ_w)         
    """

# Questions and Answers
    accl, dist = symb('distance acceleration')
    expr12 = dist * dens_w * accl

with st.expander("Q 1. What is the pressure difference in water which is horizontally accelerating, between two "
                 "points at the same horizontal level?"):
    st.latex(f"{expr12}={expr11}")

sentiment_mapping = [0, 1]
selected = st.feedback("thumbs")
if selected is not None:
    st.markdown("Thanks for your feedback!")

