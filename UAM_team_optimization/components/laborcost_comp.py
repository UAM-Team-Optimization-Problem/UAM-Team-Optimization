import numpy as np
from openmdao.api import ExplicitComponent


class LaborCostComp(ExplicitComponent):

    def setup(self):
        self.add_input('EngHr')
        self.add_input('EngRt')
        self.add_input('ToolHr')
        self.add_input('ToolRt')
        self.add_input('MfgHr')
        self.add_input('MfgRt')
        self.add_input('QcHr')
        self.add_input('QcRt')
        
        self.add_output('LaborCost')



        
    def compute(self, inputs, outputs):
        
        EngHr = inputs['EngHr']
        EngRt = inputs['EngRt']
        ToolHr = inputs['ToolHr']
        ToolRt = inputs['ToolRt']
        MfgHr = inputs['MfgHr']
        MfgRt = inputs['MfgRt']
        QcHr = inputs['QcHr']
        QcRt = inputs['QcRt']

        outputs['LaborCost'] = EngHr * EngRt + ToolHr * ToolRt + MfgHr * MfgRt + QcHr * QcRt
