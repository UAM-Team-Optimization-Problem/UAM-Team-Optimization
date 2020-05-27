from openmdao.api import Group, IndepVarComp

from lsdo_utils.api import PowerCombinationComp, LinearCombinationComp
from UAM_team_optimization.components.Geometry.geometry_comp import GeometryComp



class GeometryGroup(Group):

    def initialize(self):
        self.options.declare('shape', types=tuple)

    def setup(self):
        shape = self.options['shape']
        
        # 
        comp = GeometryComp()
        self.add_subsystem('geometry_comp', comp, promotes = ['*'])