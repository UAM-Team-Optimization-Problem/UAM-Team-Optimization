# Glauert 
from openmdao.api import Problem, IndepVarComp

from lsdo_aircraft.api import Preprocess, Atmosphere, Powertrain, PowertrainGroup, AtmosphereGroup
from lsdo_aircraft.api import SimpleRotor, SimpleMotor
#from lsdo_aircraft.preprocess.preprocess_group import PreprocessGroup
# from lsdo_aircraft.api import SimpleRotorGroup
from openmdao.api import ExplicitComponent

import numpy as np

n = 1
shape = (n, n)

powertrain = Powertrain()

preprocess_name = 'preprocess'
atmosphere_name = 'atmosphere'
simple_motor_name = 'motor'
simple_rotor_name = 'rotor'


powertrain.add_module(Preprocess(
    name=preprocess_name,
))
powertrain.add_module(Atmosphere(
    name=atmosphere_name,
))
powertrain.add_module(SimpleMotor(
    name=simple_motor_name,
))
powertrain.add_module(SimpleRotor(
    name=simple_rotor_name,
))

powertrain.add_link(
    preprocess_name, 'altitude',
    atmosphere_name, 'altitude',
)
powertrain.add_link(
    preprocess_name, 'speed',
    atmosphere_name, 'speed',
)
powertrain.add_link(
    preprocess_name, 'speed',
    simple_rotor_name, 'speed',
)
powertrain.add_link(
    atmosphere_name, ['density', 'sonic_speed'],
    simple_rotor_name, ['density', 'sonic_speed'],
)
powertrain.add_link(
    simple_motor_name, ['angular_speed', 'shaft_power'],
    simple_rotor_name, ['angular_speed', 'shaft_power'],
)

prop_prob = Problem()


# atmosphere_group = AtmosphereGroup(
#     shape=shape,
#     atmosphere = atmosphere,
# )
# prop_prob.model.add_subsystem('atmosphere_group',atmosphere_group, promotes=['*'])

wing_outer_prop_group = PowertrainGroup(
    shape=shape,
    powertrain=powertrain,
)
prop_prob.model.add_subsystem('wing_outer_prop_group', wing_outer_prop_group, promotes=['*'])

wing_inner_prop_group = PowertrainGroup(
    shape=shape,
    powertrain=powertrain,
)
prop_prob.model.add_subsystem('wing_inner_prop_group', wing_inner_prop_group)

tail_prop_group = PowertrainGroup(
    shape=shape,
    powertrain=powertrain,
)
prop_prob.model.add_subsystem('tail_prop_group', tail_prop_group)


prop_prob.setup(check=True)

prop_prob['motor_group.mass'] = 120.
prop_prob['motor_group.angular_speed'] = 120.
prop_prob['motor_group.normalized_torque'] = 0.6
prop_prob['preprocess_group.speed'] = 67. * 0.25

prop_prob['wing_inner_prop_group.motor_group.mass'] = 120.
prop_prob['wing_inner_prop_group.motor_group.angular_speed'] = 100.
prop_prob['wing_inner_prop_group.motor_group.normalized_torque'] = 0.5
prop_prob['wing_inner_prop_group.preprocess_group.speed'] = 67. * 0.25

prop_prob['tail_prop_group.motor_group.mass'] = 100.
prop_prob['tail_prop_group.motor_group.angular_speed'] = 50.
prop_prob['tail_prop_group.motor_group.normalized_torque'] = 0.5
prop_prob['tail_prop_group.preprocess_group.speed'] = 67. * 0.25



prop_prob.run_model()
# prop_prob.model.list_outputs(print_arrays=True, prom_name=True)
wing_outer_prop_thrust_coeff = prop_prob['wing_outer_prop_group.rotor_group.thrust_coeff_comp.thrust_coeff']/7.75
wing_inner_prop_thrust_coeff = prop_prob['wing_inner_prop_group.rotor_group.thrust_coeff_comp.thrust_coeff']/7.75
tail_prop_thrust_coeff = prop_prob['tail_prop_group.rotor_group.thrust_coeff_comp.thrust_coeff']/7.75

thrust_list = prop_prob.model.list_outputs(values=True, includes=['*thrust_coeff*',])
thrust_coeff = thrust_list[0][1]["value"]/7.75
print(thrust_coeff)
print(wing_outer_prop_thrust_coeff)
print(wing_inner_prop_thrust_coeff)
print(tail_prop_thrust_coeff)
# print(prob.model.group.PreprocessGroup.altitude)
