# Maximize Profit w.r.t:
# Describe optimization problem
#
# Model Inputs: ...
# Model Outputs: ...

# Models:
    # Model Inputs:
        # input_comp :   Model inputs (not limited to desgin variables
                        # --> Not all model inputs are design variables)
    # Aerodynamics
        # aero_comp_1 : Equation
        # aero_comp_2 : Equation
        # ...
    # Propulsion
        # prop_comp_1 : Equation
        # prop_copm_2 : Equation
        # ...
    # Weights and Stability
        # weight_comp_1 : Equation
        # weight_comp_2 : Equation
        # ...
    # Economics
        # econ_comp_1 : Equation
        # econ_comp_2 : Equation
        # ...
    # Performance
        # perf_comp_1 : Equation
        # perf_comp_2 : Equation
    # Model Outpu:
        # output_comp : Model Outputs = Profit



from openmdao.api import Problem, Group, IndepVarComp, ExecComp
import numpy as np

from UAM_team_optimization.components.Aero.cl_wing_comp import CLWingComp
from UAM_team_optimization.components.Aero.cl_tail_comp import CLTailComp
from UAM_team_optimization.components.Aero.cdi_wing_comp import CDiWingComp
from UAM_team_optimization.components.Aero.cdi_tail_comp import CDiTailComp
from UAM_team_optimization.components.Geometry.geometry_comp import GeometryComp
from UAM_team_optimization.components.Propulsion.propulsion_comp import wing_outer_prop_thrust_coeff, wing_inner_prop_thrust_coeff,tail_prop_thrust_coeff
from UAM_team_optimization.components.Aero.axial_int_comp import AxialIntComp
from UAM_team_optimization.components.Aero.percent_blown_comp import PercentBlownComp
from UAM_team_optimization.components.weightsandstability.emptyweight_comp import EmptyWeightComp
from UAM_team_optimization.components.weightsandstability.grossweight_comp import GrossWeightComp
from UAM_team_optimization.components.weightsandstability.xcg_comp import XCGComp
from UAM_team_optimization.components.weightsandstability.xnp_comp import XNPComp
from UAM_team_optimization.components.enghr_comp import EngHrComp
from UAM_team_optimization.components.mfghr_comp import MfgHrComp
from UAM_team_optimization.components.toolhr_comp import ToolHrComp
from UAM_team_optimization.components.qchr_comp import QcHrComp
from UAM_team_optimization.components.laborcost_comp import LaborCostComp
from UAM_team_optimization.components.develcost_comp import DevelCostComp
from UAM_team_optimization.components.fltcost_comp import FltCostComp
from UAM_team_optimization.components.mfgcost_comp import MfgCostComp
from UAM_team_optimization.components.batterycost_comp import BatteryCostComp
from UAM_team_optimization.components.motorcost_comp import MotorCostComp
from UAM_team_optimization.components.avionicscost_comp import AvionicsCostComp
from UAM_team_optimization.components.structcost_comp import StructCostComp
from UAM_team_optimization.components.ac_comp import AcComp


prob = Problem()
model = Group()
prob.model = model
prob.setup()

comp = IndepVarComp()
# comp.add_output('EmptyWeight', val=6000)
comp.add_output('v_inf' , val= 240)
comp.add_output('q' , val= 250)
comp.add_output('EngRt' , val= 40)
comp.add_output('MfgRt' , val= 30)
comp.add_output('ToolRt' , val= 21)
comp.add_output('QcRt' , val= 37)
comp.add_output('kwh' , val= 133)
comp.add_output('kwhcost' , val= 137)
comp.add_output('num_motor' , val= 12)
model.add_subsystem('inputs_comp', comp, promotes=['*'])



# prob.check_partials(compact_print=True)
#
# print('EngHr', prob['EngHr'])
# print('MfgHr', prob['MfgHr'])
# print('ToolHr', prob['ToolHr'])
# print('QcHr', prob['QcHr'])
# print('LaborCost', prob['LaborCost'])
# print('DevelCost', prob['DevelCost'])
# print('FltCost', prob['FltCost'])
# print('MfgCost', prob['MfgCost'])
# print('BatteryCost', prob['BatteryCost'])
# print('MotorCost', prob['MotorCost'])
# print('AvionicsCost', prob['AvionicsCost'])
# print('StructCost', prob['StructCost'])
# print('Ac', prob['Ac'])

#Adding Input variables which are the outputs of input_comp
# Wing
comp.add_output('wing_alpha', val = 0.1)
comp.add_output('wing_CLa', val = 2*np.pi)
comp.add_output('wing_CL0', val = 0.2)
comp.add_output('wing_CD0', val = 0.015)
comp.add_output('wing_e', val = 0.85)
comp.add_output('wing_AR', val = 8 )
comp.add_output('wing_area', val = 25 )
# Tail
comp.add_output('tail_alpha', val = 0)
comp.add_output('tail_CLa', val = 2*np.pi)
comp.add_output('tail_CL0', val = 0.2)
comp.add_output('tail_CD0', val = 0.015)
comp.add_output('tail_e', val = 0.85)
comp.add_output('tail_AR', val = 8 )
comp.add_output('tail_area', val = 4 )
# Propeller
comp.add_output('wing_prop_inner_rad',val = 0.8)
comp.add_output('wing_prop_outer_rad',val = 0.8)
comp.add_output('tail_prop_rad',val = 0.8)
comp.add_output('wing_inner_thrust_coeff', val = wing_inner_prop_thrust_coeff)
comp.add_output('wing_outer_thrust_coeff', val = wing_outer_prop_thrust_coeff)
comp.add_output('tail_thrust_coeff', val = tail_prop_thrust_coeff)

comp = GeometryComp()
model.add_subsystem('geometry_comp', comp, promotes = ['*'])
comp = ExecComp('wing_chord = wing_area / wing_span')
model.add_subsystem('wing_chord_comp', comp, promotes = ['*'])
comp = ExecComp('tail_chord = tail_area / tail_span')
model.add_subsystem('tail_chord_comp', comp, promotes = ['*'])
comp = AxialIntComp()
model.add_subsystem('axial_int_comp', comp, promotes = ['*'])
comp = PercentBlownComp()
model.add_subsystem('percent_blown_comp', comp, promotes = ['*'])
comp = CLWingComp()
model.add_subsystem('cl_wing_comp', comp, promotes = ['*'])
comp = CLTailComp()
model.add_subsystem('cl_tail_comp', comp, promotes = ['*'])
comp = CDiWingComp()
model.add_subsystem('cdi_wing_comp', comp, promotes = ['*'])
comp = CDiTailComp()
model.add_subsystem('cdi_tail_comp', comp, promotes = ['*'])
comp = ExecComp('wing_CD = wing_CD0 + wing_CDi')
model.add_subsystem('wing_CD_comp', comp, promotes = ['*'])
comp = ExecComp('tail_CD = tail_CD0 + tail_CDi')
model.add_subsystem('tail_CD_comp', comp, promotes = ['*'])
comp = ExecComp('wing_LD = wing_CL/wing_CD')
model.add_subsystem('wing_ld_comp', comp, promotes = ['*'])
comp = ExecComp('tail_LD = tail_CL/tail_CD')
model.add_subsystem('tail_ld_comp', comp, promotes = ['*'])

# WEIGHTS/STABILITY COMPONENTS

# Gross Weight [N]
comp = GrossWeightComp(rho=1.2)
model.add_subsystem('grossweight_comp', comp, promotes=['*'])

# Empty Weight [N]
comp = EmptyWeightComp(rho=1.5)
model.add_subsystem('emptyweight_comp', comp, promotes=['*'])

# CG Location from nose [m]
# comp = XCGComp()
# model.add_subsystem('xcg_comp', comp, promotes=['*'])

comp=EngHrComp()
model.add_subsystem('enghr_comp', comp, promotes=['*'])

comp=MfgHrComp()
model.add_subsystem('mfghr_comp', comp, promotes=['*'])

comp=ToolHrComp()
model.add_subsystem('toolhr_comp', comp, promotes=['*'])

comp=QcHrComp()
model.add_subsystem('qchr_comp', comp, promotes=['*'])

comp=LaborCostComp()
model.add_subsystem('laborcost_comp', comp, promotes=['*'])

comp=DevelCostComp()
model.add_subsystem('develcost_comp', comp, promotes=['*'])

comp=FltCostComp(fta=6)
model.add_subsystem('fltcost_comp', comp, promotes=['*'])

comp=MfgCostComp()
model.add_subsystem('mfgcost_comp', comp, promotes=['*'])

comp=BatteryCostComp()
model.add_subsystem('batterycost_comp', comp, promotes=['*'])

comp=MotorCostComp()
model.add_subsystem('motorcost_comp', comp, promotes=['*'])

comp=AvionicsCostComp()
model.add_subsystem('avionicscost_comp', comp, promotes=['*'])

comp=StructCostComp()
model.add_subsystem('structcost_comp', comp, promotes=['*'])

comp=AcComp()
model.add_subsystem('ac_comp', comp, promotes=['*'])

prob.setup(check = True)
prob.run_model()
prob.check_partials(compact_print=True)

# print('wing_CL',prob['wing_CL'])
# print('tail_CL',prob['tail_CL'])
# print('wing_span',prob['wing_span'])
# print('tail_span',prob['tail_span'])
# print('thrust_coeff',prob['thrust_coeff'])
# print('axial_int_fac',prob['axial_int_fac'])
# print('wing_blown_percent', prob['wing_blown_percent'])

prob.model.list_outputs()
