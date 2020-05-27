from openmdao.api import Group, IndepVarComp

# from lsdo_utils.api import PowerCombinationComp, LinearCombinationComp
from UAM_team_optimization.components.Weights.emptyweight_comp import EmptyWeightComp
from UAM_team_optimization.components.Weights.grossweight_comp import GrossWeightComp
from UAM_team_optimization.components.Weights.wingweight_comp import WingWeightComp
from UAM_team_optimization.components.Weights.xcg_comp import XCGComp
from UAM_team_optimization.components.Weights.xnp_comp import XNPComp



class WeightsGroup(Group):

    def initialize(self):
        self.options.declare('shape', types=tuple)

    def setup(self):
        shape = self.options['shape']
        
        # 
        comp = EmptyWeightComp(rho=1.2)
        self.add_subsystem('emptyweight_comp', comp, promotes = ['*'])
        comp = GrossWeightComp(rho=1.2)
        self.add_subsystem('grossweight_comp', comp, promotes = ['*'])
        comp = WingWeightComp(rho=1.2)
        self.add_subsystem('wingweight_comp', comp, promotes = ['*'])
        comp = XCGComp()
        self.add_subsystem('xcg_comp', comp, promotes = ['*'])
        comp = XNPComp()
        self.add_subsystem('xnp_comp', comp, promotes = ['*'])