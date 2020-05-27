import numpy as np

from openmdao.api import Problem, IndepVarComp, Group
from openmdao.api import ExplicitComponent

import numpy as np

from UAM_team_optimization.Aero_group import AeroGroup
from UAM_team_optimization.Geometry_group import GeometryGroup
from UAM_team_optimization.Inputs_group import InputsGroup
from UAM_team_optimization.Propulsion_group import PropulsionGroup
from UAM_team_optimization.Weights_group import WeightsGroup
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

economics_group = EconGroup(
    shape=my_shape,
)
prob.model.add_subsystem('economics_group',economics_group,promotes=['*'])

prob.setup(check=True)
prob['motor_group.mass'] = 120.
prob['motor_group.angular_speed'] = 120.
prob['motor_group.normalized_torque'] = 0.6
prob['preprocess_group.speed'] = 67. * 0.25

prob['wing_left_inner_prop_group.motor_group.mass'] = 120.
prob['wing_left_inner_prop_group.motor_group.angular_speed'] = 100.
prob['wing_left_inner_prop_group.motor_group.normalized_torque'] = 0.5
prob['wing_left_inner_prop_group.preprocess_group.speed'] = 67. * 0.25

prob['tail_left_prop_group.motor_group.mass'] = 100.
prob['tail_left_prop_group.motor_group.angular_speed'] = 50.
prob['tail_left_prop_group.motor_group.normalized_torque'] = 0.5
prob['tail_left_prop_group.preprocess_group.speed'] = 67. * 0.25

prob['wing_right_inner_prop_group.motor_group.mass'] = 120.
prob['wing_right_inner_prop_group.motor_group.angular_speed'] = 100.
prob['wing_right_inner_prop_group.motor_group.normalized_torque'] = 0.5
prob['wing_right_inner_prop_group.preprocess_group.speed'] = 67. * 0.25

prob['wing_right_outer_prop_group.motor_group.mass'] = 120.
prob['wing_right_outer_prop_group.motor_group.angular_speed'] = 100.
prob['wing_right_outer_prop_group.motor_group.normalized_torque'] = 0.5
prob['wing_right_outer_prop_group.preprocess_group.speed'] = 67. * 0.25

prob['tail_right_prop_group.motor_group.mass'] = 100.
prob['tail_right_prop_group.motor_group.angular_speed'] = 50.
prob['tail_right_prop_group.motor_group.normalized_torque'] = 0.5
prob['tail_right_prop_group.preprocess_group.speed'] = 67. * 0.25



prob.run_model()

prob.model.list_outputs(prom_name=True)