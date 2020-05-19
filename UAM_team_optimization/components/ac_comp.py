import numpy as np
from openmdao.api import ExplicitComponent


class AcComp(ExplicitComponent):

    def setup(self):
        self.add_input('LaborCost')
        self.add_input('StructCost')
        self.add_input('q')
               
        self.add_output('Ac')


    def compute(self, inputs, outputs):
        
        LaborCost = inputs['LaborCost']
        StructCost = inputs['StructCost']
        q = inputs['q']


        outputs['Ac'] = (StructCost + LaborCost) / q
