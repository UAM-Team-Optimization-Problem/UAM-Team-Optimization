# OBJECTIVE FUNCTION: MINIMIZE (negative) Profit

# DESIGN VARIABLES (w.r.t) : 
#       wing_alpha - WING AOA
#       wing_ar - WING ASPECT RATIO
#       wing_area - WING SURFACE AREA
#       tail_alpha - TAIL AOA
#       tail_ar - TAIL ASPECT RATIO
#       tail_area - TAIL SURFACE AREA
#       h - ALTITUDE
#       v_inf - SPEED
#       cp - POWER COEFFICIENT
#       j - ADVANCE RATIO
#       r - ROTOR RADIUS
#       rpm - ROTATIONAL SPEED
#       mb - BATTERY MASS
#       numflts - NUMBER OF FLIGHTS

# CONSTRAINTS (subj. to):
#       L - W = 0 -- LEVEL FLIGHT CONDITION (VERTICAL)
#       T - D = 0 -- LEVEL FLIGHT CONDITION (HORIZONTAL)
#       R >= 100e3 m -- MINIMUM RANGE
#       Cm = 0 -- LEVEL FLIGHT CONDITION (MOMENT)
#       SM: [0.06, 0.20] -- STATIC MARGIN

# MODEL INPUTS: wing_alpha, wing_ar, wing_area, tail_alpha, tail_ar, tail_area,
#               h, v_inf, cp, j, r, rpm, mb, numflts
# MODEL OUTPUTS: L, W, T, D, R, M, SM

import numpy as np
from openmdao.api import Problem, Group, IndepVarComp, ExecComp, ScipyOptimizeDriver
from UAM_team_optimization.components.cl_wing_comp import CLWingComp
from UAM_team_optimization.components.cl_tail_comp import CLTailComp
from UAM_team_optimization.components.geometry_comp import GeometryComp
from UAM_team_optimization.components.weightsandstability.emptyweight_comp import EmptyWeightComp
from UAM_team_optimization.components.weightsandstability.grossweight_comp import GrossWeightComp
from UAM_team_optimization.components.weightsandstability.xcg_comp import XCGComp
from UAM_team_optimization.components.weightsandstability.xnp_comp import XNPComp

prob = Problem()
model = Group()

comp = IndepVarComp()

# Initial Weights
comp.add_output('w_design', val=26700.)
comp.add_output('w_pax', val=900.)
comp.add_output('w_else', val=18000.) # all empty weight EXCEPT tail, wing, PAX
comp.add_output('load_factor', val=3.8)

# Wing
comp.add_output('wing_alpha', val = 0.1)
comp.add_output('wing_CLa', val = 2*np.pi)
comp.add_output('wing_CL0', val = 0.2)
comp.add_output('wing_AR', val = 8 )
comp.add_output('wing_area', val = 25.)
comp.add_output('wing_span', val=15.)
comp.add_output('wing_tc', val=0.76)


# Tail
comp.add_output('tail_alpha', val = 0)
comp.add_output('tail_CLa', val = 2*np.pi)
comp.add_output('tail_CL0', val = 0.2)
comp.add_output('tail_AR', val = 8 )
comp.add_output('tail_area', val = 4 )
comp.add_output('tail_span', val=2.)
comp.add_output('tail_tc', val=0.9)


# Propeller
comp.add_output('wing_prop_inner_rad',val = 0.8)
comp.add_output('wing_prop_outer_rad',val = 0.8)
comp.add_output('tail_prop_rad',val = 0.8)

comp.add_output('h', val=0.)
comp.add_output('v_inf', val=58.)
comp.add_output('cp', val=0.)
comp.add_output('j', val=0.)
comp.add_output('r', val=0.)
comp.add_output('rpm', val=1900)
comp.add_output('mb', val=500.)
comp.add_output('nmflts', val=0.)

# List of Design Variables
comp.add_design_var('wing_alpha', lower=-0.05, upper=0.09)
comp.add_design_var('wing_AR', lower=3., upper=13.)
comp.add_design_var('wing_span', lower=15., upper=30.)
comp.add_design_var('tail_alpha', lower=-0.5, upper=0.09)
comp.add_design_var('tail_AR', lower=3., upper=13.)
comp.add_design_var('tail_span', lower=2., upper=4.)
comp.add_design_var('h')
comp.add_design_var('v_inf', lower=58., upper=70.)
comp.add_design_var('cp')
comp.add_design_var('j')
comp.add_design_var('r')
comp.add_design_var('rpm')
comp.add_design_var('mb')
comp.add_design_var('nmflts')

model.add_subsystem('inputs_comp', comp, promotes = ['*'])

# WEIGHTS/STABILITY COMPONENTS

# Gross Weight [N]
comp = GrossWeightComp(rho=1.2)
model.add_subsystem('grossweight_comp', comp, promotes=['*'])

# Empty Weight [N]
comp = EmptyWeightComp(rho=1.2)
model.add_subsystem('emptyweight_comp', comp, promotes=['*'])

# CG Location from nose [m]
# comp = XCGComp()
# model.add_subsystem('xcg_comp', comp, promotes=['*'])

# NP Location from nose [m]
# comp = XNPComp()
# model.add_subsystem('xnp_comp', comp, promotes=['*'])

# Static Margin [%]
# comp = ExecComp('SM = (XNP - XAC) / MAC')
# comp.add_constraint('SM', lower=0.06., upper=0.20.)
# model.add_subsystem('sm_comp', comp, promotes=['*'])

# Pitching Moment [N.m]
# comp = ExecComp('M = (wing_lift * XCG) - tail_lift * (tail_arm - XCG)')
# comp.add_constraint('M', equals=0.)
# model.add_subsystem('m_comp', comp, promotes=['*'])


prob.model = model

# prob.driver = ScipyOptimizeDriver()
# prob.driver.options['optimizer'] = 'SLSQP'
# prob.driver.options['tol'] = 1e-15
# prob.driver.options['disp'] = True

prob.setup()
prob.run_model()
# prob.run_driver()

prob.check_partials(compact_print=True)

print('GrossWeight', prob['GrossWeight'])
print('EmptyWeight', prob['EmptyWeight'])
