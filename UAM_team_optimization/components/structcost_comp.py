import numpy as np
from openmdao.api import ExplicitComponent


class StructCostComp(ExplicitComponent):

    def setup(self):
        self.add_input('DevelCost')
        self.add_input('FltCost')
        self.add_input('MfgCost')
        self.add_input('BatteryCost')
        self.add_input('MotorCost')
        self.add_input('AvionicsCost')
               
        self.add_output('StructCost')


    def compute(self, inputs, outputs):
        
        DevelCost = inputs['DevelCost']
        FltCost = inputs['FltCost']
        MfgCost = inputs['MfgCost']
        BatteryCost = inputs['BatteryCost']
        MotorCost = inputs['MotorCost']
        AvionicsCost = inputs['AvionicsCost']


        outputs['StructCost'] = DevelCost + FltCost + MfgCost + BatteryCost + MotorCost + AvionicsCost
