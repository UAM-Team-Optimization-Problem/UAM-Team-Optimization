from openmdao.api import Group, IndepVarComp

# from lsdo_utils.api import PowerCombinationComp, LinearCombinationComp
from UAM_team_optimization.components.Economics.ac_comp import AcComp
from UAM_team_optimization.components.Economics.avionicscost_comp import AvionicsCostComp
from UAM_team_optimization.components.Economics.batterycost_comp import BatteryCostComp
from UAM_team_optimization.components.Economics.develcost_comp import DevelCostComp
from UAM_team_optimization.components.Economics.enghr_comp import EngHrComp
from UAM_team_optimization.components.Economics.fltcost_comp import FltCostComp
from UAM_team_optimization.components.Economics.laborcost_comp import LaborCostComp
from UAM_team_optimization.components.Economics.mfgcost_comp import MfgCostComp
from UAM_team_optimization.components.Economics.mfghr_comp import MfgHrComp
from UAM_team_optimization.components.Economics.motorcost_comp import MotorCostComp
from UAM_team_optimization.components.Economics.qchr_comp import QcHrComp
from UAM_team_optimization.components.Economics.structcost_comp import StructCostComp
from UAM_team_optimization.components.Economics.toolhr_comp import ToolHrComp
from UAM_team_optimization.components.Economics.fare_comp import FareComp
from UAM_team_optimization.components.Economics.profit_comp import ProfitComp


class EconGroup(Group):

    def initialize(self):
        self.options.declare('shape', types=tuple)

    def setup(self):
        shape = self.options['shape']

        #
        comp = AcComp()
        self.add_subsystem('ac_comp', comp, promotes = ['*'])
        comp = AvionicsCostComp()
        self.add_subsystem('avionicscost_comp', comp, promotes = ['*'])
        comp = BatteryCostComp()
        self.add_subsystem('batterycost_comp', comp, promotes = ['*'])
        comp = DevelCostComp()
        self.add_subsystem('develcost_comp', comp, promotes = ['*'])
        comp = EngHrComp()
        self.add_subsystem('enghr_comp', comp, promotes = ['*'])
        comp = FltCostComp(fta=6)
        self.add_subsystem('fltcost_comp', comp, promotes = ['*'])
        comp = LaborCostComp()
        self.add_subsystem('laborcost_comp', comp, promotes = ['*'])
        comp = MfgCostComp()
        self.add_subsystem('mfgcost_comp', comp, promotes = ['*'])
        comp = MfgHrComp()
        self.add_subsystem('mfghr_comp', comp, promotes = ['*'])
        comp = MotorCostComp()
        self.add_subsystem('motorcost_comp', comp, promotes = ['*'])
        comp = QcHrComp()
        self.add_subsystem('qchr_comp', comp, promotes = ['*'])
        comp = StructCostComp()
        self.add_subsystem('structcost_comp', comp, promotes = ['*'])
        comp = ToolHrComp()
        self.add_subsystem('toolhr_comp', comp, promotes = ['*'])
        comp = FareComp()
        self.add_subsystem('fare_comp', comp, promotes = ['*'])
        comp = ProfitComp()
        self.add_subsystem('profit_comp', comp, promotes = ['*'])
