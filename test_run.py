

import numpy as np

from openmdao.api import Problem, IndepVarComp, Group
from openmdao.api import ExplicitComponent
from lsdo_aircraft.api import SimpleRotor, SimpleMotor, Powertrain, PowertrainGroup

import numpy as np
from openmdao.utils.options_dictionary import OptionsDictionary
from UAM_team_optimization.Aero_group import AeroGroup
from UAM_team_optimization.Aero import Aero
from UAM_team_optimization.Geometry_group import GeometryGroup
from UAM_team_optimization.Inputs_group import InputsGroup
from UAM_team_optimization.Propulsion_group import PropulsionGroup
from UAM_team_optimization.Weights_group import WeightsGroup
from UAM_team_optimization.motion_equations_group import MotionEquationsGroup
from UAM_team_optimization.energy_group import EnergyGroup
from UAM_team_optimization.Econ_group import EconGroup


my_shape = (1,)

prob = Problem()

inputs_group = InputsGroup(
    shape = my_shape
)
prob.model.add_subsystem('inputs_group', inputs_group,promotes=['*'])

geometry_group = GeometryGroup(
    shape = my_shape
)
prob.model.add_subsystem('geometry_group',  geometry_group,promotes=['*'])

propulsion_group = PropulsionGroup(
    shape = my_shape
)
prob.model.add_subsystem('propulsion_group', propulsion_group,promotes = ['*'])

aero_group = AeroGroup(
    shape=my_shape,
)
prob.model.add_subsystem('aero_group',aero_group,promotes=['*'])

weights_group = WeightsGroup(
    shape=my_shape,
)
prob.model.add_subsystem('weights_group',weights_group,promotes=['*'])

motion_equations_group = MotionEquationsGroup(
    shape=my_shape,
)
prob.model.add_subsystem('motion_equations_group',motion_equations_group,promotes=['*'])

energy_group = EnergyGroup(
    shape=my_shape,
)
prob.model.add_subsystem('energy_group',energy_group,promotes=['*'])

economics_group = EconGroup(
    shape=my_shape,
)
prob.model.add_subsystem('economics_group',economics_group,promotes=['*'])

# ---- ---- ---- ---- CRUISE CONNECTIONS ---- ---- ---- ---- #
prob.model.connect('rotor_group.thrust_coeff','wing_left_outer_thrust_coeff')
prob.model.connect('wing_left_inner_prop_group.rotor_group.thrust_coeff','wing_left_inner_thrust_coeff')
prob.model.connect('wing_right_outer_prop_group.rotor_group.thrust_coeff','wing_right_outer_thrust_coeff')
prob.model.connect('wing_right_inner_prop_group.rotor_group.thrust_coeff','wing_right_inner_thrust_coeff')
prob.model.connect('tail_right_prop_group.rotor_group.thrust_coeff','tail_right_thrust_coeff')
prob.model.connect('tail_left_prop_group.rotor_group.thrust_coeff','tail_left_thrust_coeff')

prob.model.connect('atmosphere_group.density','density')
prob.model.connect('atmosphere_group.dynamic_viscosity','dynamic_viscosity')
prob.model.connect('atmosphere_group.sonic_speed','sonic_speed')

prob.model.connect('tail_left_prop_group.rotor_group.thrust','cruise_tail_left_thrust')
prob.model.connect('tail_right_prop_group.rotor_group.thrust','cruise_tail_right_thrust')
prob.model.connect('wing_left_inner_prop_group.rotor_group.thrust','cruise_wing_left_inner_thrust')
prob.model.connect('rotor_group.thrust','cruise_wing_left_outer_thrust')
prob.model.connect('wing_right_inner_prop_group.rotor_group.thrust','cruise_wing_right_inner_thrust')
prob.model.connect('wing_right_outer_prop_group.rotor_group.thrust','cruise_wing_right_outer_thrust')

prob.model.connect('tail_left_prop_group.rotor_group.efficiency', 'cruise_tail_left_eff')
prob.model.connect('tail_right_prop_group.rotor_group.efficiency', 'cruise_tail_right_eff')
prob.model.connect('wing_left_inner_prop_group.rotor_group.efficiency', 'cruise_wing_left_inner_eff')
prob.model.connect('rotor_group.efficiency', 'cruise_wing_left_outer_eff')
prob.model.connect('wing_right_inner_prop_group.rotor_group.efficiency', 'cruise_wing_right_inner_eff')
prob.model.connect('wing_right_outer_prop_group.rotor_group.efficiency', 'cruise_wing_right_outer_eff')

prob.model.connect('tail_left_prop_group.motor_group.input_power', 'cruise_tail_left_power')
prob.model.connect('tail_right_prop_group.motor_group.input_power', 'cruise_tail_right_power')
prob.model.connect('wing_left_inner_prop_group.motor_group.input_power', 'cruise_wing_left_inner_power')
prob.model.connect('motor_group.input_power', 'cruise_wing_left_outer_power')
prob.model.connect('wing_right_inner_prop_group.motor_group.input_power', 'cruise_wing_right_inner_power')
prob.model.connect('wing_right_outer_prop_group.motor_group.input_power', 'cruise_wing_right_outer_power')

# ---- ---- ---- ---- HOVER CONNECTIONS ---- ---- ---- ---- #
prob.model.connect('hover_tail_left_prop_group.rotor_group.thrust','hover_tail_left_thrust')
prob.model.connect('hover_tail_right_prop_group.rotor_group.thrust','hover_tail_right_thrust')
prob.model.connect('hover_wing_left_inner_prop_group.rotor_group.thrust','hover_wing_left_inner_thrust')
prob.model.connect('hover_wing_left_outer_prop_group.rotor_group.thrust','hover_wing_left_outer_thrust')
prob.model.connect('hover_wing_right_inner_prop_group.rotor_group.thrust','hover_wing_right_inner_thrust')
prob.model.connect('hover_wing_right_outer_prop_group.rotor_group.thrust','hover_wing_right_outer_thrust')

prob.model.connect('hover_tail_left_prop_group.rotor_group.efficiency', 'hover_tail_left_eff')
prob.model.connect('hover_tail_right_prop_group.rotor_group.efficiency', 'hover_tail_right_eff')
prob.model.connect('hover_wing_left_inner_prop_group.rotor_group.efficiency', 'hover_wing_left_inner_eff')
prob.model.connect('hover_wing_left_outer_prop_group.rotor_group.efficiency', 'hover_wing_left_outer_eff')
prob.model.connect('hover_wing_right_inner_prop_group.rotor_group.efficiency', 'hover_wing_right_inner_eff')
prob.model.connect('hover_wing_right_outer_prop_group.rotor_group.efficiency', 'hover_wing_right_outer_eff')

prob.model.connect('hover_tail_left_prop_group.motor_group.input_power', 'hover_tail_left_power')
prob.model.connect('hover_tail_right_prop_group.motor_group.input_power', 'hover_tail_right_power')
prob.model.connect('hover_wing_left_inner_prop_group.motor_group.input_power', 'hover_wing_left_inner_power')
prob.model.connect('hover_wing_left_outer_prop_group.motor_group.input_power', 'hover_wing_left_outer_power')
prob.model.connect('hover_wing_right_inner_prop_group.motor_group.input_power', 'hover_wing_right_inner_power')
prob.model.connect('hover_wing_right_outer_prop_group.motor_group.input_power', 'hover_wing_right_outer_power')

# prob.model.connect('wing_left_inner_thrust_coeff','tail_right_prop_group.rotor_group.thrust')#    'model.aero_group.axial_int_comp.wing_left_outer_axial_int_fac')

prob.setup(check=True)
# ---- ---- ---- ---- CRUISE SETUP ---- ---- ---- ---- #
prob['motor_group.mass'] = 69.
prob['motor_group.angular_speed'] = 30.
prob['motor_group.normalized_torque'] = 0.4
prob['preprocess_group.speed'] = 67.

prob['wing_left_inner_prop_group.motor_group.mass'] = 69.
prob['wing_left_inner_prop_group.motor_group.angular_speed'] = 30.
prob['wing_left_inner_prop_group.motor_group.normalized_torque'] = 0.4
prob['wing_left_inner_prop_group.preprocess_group.speed'] = 67.

prob['tail_left_prop_group.motor_group.mass'] = 69.
prob['tail_left_prop_group.motor_group.angular_speed'] = 30.
prob['tail_left_prop_group.motor_group.normalized_torque'] = 0.4
prob['tail_left_prop_group.preprocess_group.speed'] = 67.

prob['wing_right_inner_prop_group.motor_group.mass'] = 69.
prob['wing_right_inner_prop_group.motor_group.angular_speed'] = 30.
prob['wing_right_inner_prop_group.motor_group.normalized_torque'] = 0.4
prob['wing_right_inner_prop_group.preprocess_group.speed'] = 67. 

prob['wing_right_outer_prop_group.motor_group.mass'] = 69.
prob['wing_right_outer_prop_group.motor_group.angular_speed'] = 30.
prob['wing_right_outer_prop_group.motor_group.normalized_torque'] = 0.4
prob['wing_right_outer_prop_group.preprocess_group.speed'] = 67. 

prob['tail_right_prop_group.motor_group.mass'] = 69.
prob['tail_right_prop_group.motor_group.angular_speed'] = 30.
prob['tail_right_prop_group.motor_group.normalized_torque'] = 0.4
prob['tail_right_prop_group.preprocess_group.speed'] = 67

# ---- ---- ---- ---- HOEVER SETUP ---- ---- ---- ---- #
prob['hover_wing_left_outer_prop_group.motor_group.mass'] = 69.
prob['hover_wing_left_outer_prop_group.motor_group.angular_speed'] = 140.
prob['hover_wing_left_outer_prop_group.motor_group.normalized_torque'] = 0.5
prob['hover_wing_left_outer_prop_group.preprocess_group.speed'] = 0.2*67.

prob['hover_wing_left_inner_prop_group.motor_group.mass'] = 69.
prob['hover_wing_left_inner_prop_group.motor_group.angular_speed'] = 140.
prob['hover_wing_left_inner_prop_group.motor_group.normalized_torque'] = 0.5
prob['hover_wing_left_inner_prop_group.preprocess_group.speed'] = 0.2*67.

prob['hover_tail_left_prop_group.motor_group.mass'] = 69.
prob['hover_tail_left_prop_group.motor_group.angular_speed'] = 140.
prob['hover_tail_left_prop_group.motor_group.normalized_torque'] = 0.5
prob['hover_tail_left_prop_group.preprocess_group.speed'] = 0.2*67.

prob['hover_wing_right_inner_prop_group.motor_group.mass'] = 69.
prob['hover_wing_right_inner_prop_group.motor_group.angular_speed'] = 140.
prob['hover_wing_right_inner_prop_group.motor_group.normalized_torque'] = 0.5
prob['hover_wing_right_inner_prop_group.preprocess_group.speed'] = 0.2*67. 

prob['hover_wing_right_outer_prop_group.motor_group.mass'] = 69.
prob['hover_wing_right_outer_prop_group.motor_group.angular_speed'] = 140.
prob['hover_wing_right_outer_prop_group.motor_group.normalized_torque'] = 0.5
prob['hover_wing_right_outer_prop_group.preprocess_group.speed'] = 0.2*67. 

prob['hover_tail_right_prop_group.motor_group.mass'] = 69.
prob['hover_tail_right_prop_group.motor_group.angular_speed'] = 140.
prob['hover_tail_right_prop_group.motor_group.normalized_torque'] = 0.5
prob['hover_tail_right_prop_group.preprocess_group.speed'] = 0.2*67

prob.run_model()
# prob.check_partials(compact_print=True)

prob.model.list_outputs(prom_name=True)

# print('tail_right_thrust_coeff',prob['tail_right_prop_group.rotor_group.thrust_coeff']/7.75)
# print('tail_left_thrust_coeff',prob['tail_left_prop_group.rotor_group.thrust_coeff']/7.75)
# print('wing_left_inner_thrust_coeff',prob['wing_left_inner_prop_group.rotor_group.thrust_coeff']/7.75)
# print('wing_left_outer_thrust_coeff',prob['rotor_group.thrust_coeff']/7.75)
# print('wing_right_inner_thrust_coeff',prob['wing_right_inner_prop_group.rotor_group.thrust_coeff']/7.75)
# print('wing_right_outer_thrust_coeff',prob['wing_right_outer_prop_group.rotor_group.thrust_coeff']/7.75)

# print('average_wing_axial_int_fac',prob['average_wing_axial_int_fac'])
