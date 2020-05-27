from openmdao.api import Group, IndepVarComp


from UAM_team_optimization.components.Aero.cl_wing_comp import CLWingComp
from UAM_team_optimization.components.Aero.cl_tail_comp import CLTailComp
from UAM_team_optimization.components.Aero.cdi_wing_comp import CDiWingComp
from UAM_team_optimization.components.Aero.cdi_tail_comp import CDiTailComp
from UAM_team_optimization.components.Aero.percent_blown_comp import PercentBlownComp
from UAM_team_optimization.components.Aero.axial_int_comp import AxialIntComp
# from UAM_team_optimization.components.Aero.test_cl_wing_comp import TestCLWingComp
# from UAM_team_optimization.components.Aero.test_cl_tail_comp import TestCLTailComp
# from UAM_team_optimization.components.Aero.test_cdi_wing_comp import TestCDiWingComp
# from UAM_team_optimization.components.Aero.test_cdi_tail_comp import TestCDiTailComp
# from UAM_team_optimization.components.Aero.test_percent_blown_comp import TestPercentBlownComp
# from UAM_team_optimization.components.Aero.test_axial_int_comp import TestAxialIntComp



class AeroGroup(Group):

    def initialize(self):
        self.options.declare('shape', types=tuple)

    def setup(self):
        shape = self.options['shape']
        
        # 
        comp = CLWingComp()
        self.add_subsystem('cl_wing_comp', comp, promotes=['*'])
        comp = CLTailComp()
        self.add_subsystem('cl_tail_comp', comp, promotes=['*'])
        comp = CDiWingComp()
        self.add_subsystem('cdi_wing_comp', comp, promotes=['*'])
        comp = CDiTailComp()
        self.add_subsystem('cdi_tail_comp', comp, promotes=['*'])
        comp = PercentBlownComp()
        self.add_subsystem('percent_blown_comp', comp, promotes=['*'])
        comp = AxialIntComp()
        self.add_subsystem('axial_int_comp', comp, promotes=['*'])
        # comp = TestCLWingComp()
        # self.add_subsystem('test_cl_wing_comp', comp)
        # comp = TestCLTailComp()
        # self.add_subsystem('test_cl_tail_comp', comp)
        # comp = TestCDiWingComp()
        # self.add_subsystem('test_cdi_wing_comp', comp)
        # comp = TestCDiTailComp()
        # self.add_subsystem('test_cdi_tail_comp', comp)
        # comp = TestPercentBlownComp()
        # self.add_subsystem('test_percent_blown_comp', comp)
        # comp = TestAxialIntComp()
        # self.add_subsystem('test_axial_int_comp', comp)
        # model.add_subsystem('cl_wing_comp', comp, promotes = ['*'])
        # # L = CL^1 0.5 rho^1 V^2 S^1
        # comp = PowerCombinationComp(
        #     shape=shape,
        #     out_name='L_w',
        #     coeff=0.5,
        #     powers_dict=dict(
        #         C_L=1.,
        #         density=1.,
        #         speed=2.,
        #         area=1.,
        #     )
        # )
        # self.add_subsystem('wing_lift_comp', comp, promotes=['*'])

        # # L = 1. x L_w + 1. x L_t
        # comp = LinearCombinationComp(
        #     shape=shape,
        #     out_name='L',
        #     constant=0.,
        #     coeffs_dict=dict(
        #         L_w=1.,
        #         L_t=1.,
        #     )
        # )
        # self.add_subsystem('total_lift_comp', comp, promotes=['*'])