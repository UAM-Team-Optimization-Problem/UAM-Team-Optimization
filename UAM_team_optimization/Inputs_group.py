from openmdao.api import Group, IndepVarComp
import numpy as np

# from UAM_team_optimization.components.Propulsion.propulsion_comp import wing_left_outer_prop_thrust_coeff, wing_left_inner_prop_thrust_coeff,tail_left_prop_thrust_coeff
# from UAM_team_optimization.components.Propulsion.propulsion_comp import wing_right_outer_prop_thrust_coeff, wing_right_inner_prop_thrust_coeff,tail_right_prop_thrust_coeff


class InputsGroup(Group):

    def initialize(self):
        self.options.declare('shape', types=tuple)

    def setup(self):
        shape = self.options['shape']
        
        # 
        comp = IndepVarComp()

# Initial values for optimization:
# Adding Input variables which are the outputs of input_comp

# Atmospheric inital values:
        comp.add_output('v_inf' , val= 60)
        comp.add_output('q' , val= 250)

# Wing inital values:
        comp.add_output('wing_alpha', val = 0.1)
        comp.add_output('wing_CLa', val = 2*np.pi)
        comp.add_output('wing_CL0', val = 0.2)
        comp.add_output('wing_CD0', val = 0.015)
        comp.add_output('wing_e', val = 0.85)
        comp.add_output('wing_AR', val = 8 )
        comp.add_output('wing_area', val = 25 )

# Tail inital values:
        comp.add_output('tail_alpha', val = 0)
        comp.add_output('tail_CLa', val = 2*np.pi)
        comp.add_output('tail_CL0', val = 0.2)
        comp.add_output('tail_CD0', val = 0.015)
        comp.add_output('tail_e', val = 0.85)
        comp.add_output('tail_AR', val = 8 )
        comp.add_output('tail_area', val = 4 )

# Propeller inital values:
        comp.add_output('wing_prop_inner_rad',val = 0.8)
        comp.add_output('wing_prop_outer_rad',val = 0.8)
        comp.add_output('tail_prop_rad',val = 0.8)
        # comp.add_output('wing_left_inner_thrust_coeff', val = wing_left_inner_prop_thrust_coeff)
        # comp.add_output('wing_left_outer_thrust_coeff', val = wing_left_outer_prop_thrust_coeff)
        # comp.add_output('tail_left_thrust_coeff', val = tail_left_prop_thrust_coeff)
        # comp.add_output('wing_right_inner_thrust_coeff', val = wing_right_inner_prop_thrust_coeff)
        # comp.add_output('wing_right_outer_thrust_coeff', val = wing_right_outer_prop_thrust_coeff)
        # comp.add_output('tail_right_thrust_coeff', val = tail_right_prop_thrust_coeff)

# Weights initial values:
        comp.add_output('w_design', val=26700.)
        comp.add_output('w_pax', val=900.)
        comp.add_output('w_else', val=18000.) # all empty weight EXCEPT tail, wing, PAX
        comp.add_output('load_factor', val=3.8)
        comp.add_output('x_wingc4', val=1.)
        comp.add_output('x_tailc4', val=2.)
        comp.add_output('x_else', val=3.)
        comp.add_output('x_pax', val=4.)

# Economics initial values:
        comp.add_output('EngRt' , val= 40)
        comp.add_output('MfgRt' , val= 30)
        comp.add_output('ToolRt' , val= 21)
        comp.add_output('QcRt' , val= 37)
        comp.add_output('kwh' , val= 133)
        comp.add_output('kwhcost' , val= 137)
        comp.add_output('num_motor' , val= 12)
        self.add_subsystem('inputs_comp', comp, promotes=['*'])
        # comp = GeometryComp()
        # self.add_subsystem('geometry_comp', comp, promotes = ['*'])


