tail_prop_prob = Problem()
tail_prop_group = PowertrainGroup(
    shape=shape,
    powertrain=powertrain,
)
tail_prop_prob.model.add_subsystem('tail_prop_group', tail_prop_group, promotes=['*'])

tail_prop_prob.setup(check=True)

tail_prop_prob['motor_group.mass'] = 100.
tail_prop_prob['motor_group.angular_speed'] = 100.
tail_prop_prob['motor_group.normalized_torque'] = 0.5
tail_prop_prob['preprocess_group.speed'] = 67. * 0.25

tail_prop_prob.run_model()
tail_prop_prob.model.list_outputs(print_arrays=True, prom_name=True)
tail_thrust_list = tail_prop_prob.model.list_outputs(values=True, includes=['*thrust_coeff*',])
tail_thrust_coeff = tail_thrust_list[0][1]["value"]/7.75
print(tail_thrust_coeff)