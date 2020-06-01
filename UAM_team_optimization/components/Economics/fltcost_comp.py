import numpy as np
from openmdao.api import ExplicitComponent


class FltCostComp(ExplicitComponent):

    def initialize(self):
        self.options.declare('fta', types=int)

    def setup(self):
        self.add_input('EmptyWeight')
        self.add_input('v_inf')
        
        self.add_output('FltCost')

        self.declare_partials('FltCost', 'EmptyWeight')
        self.declare_partials('FltCost', 'v_inf')

    def compute(self, inputs, outputs):
        fta = self.options['fta']

        EmptyWeight = inputs['EmptyWeight']/9.8
        v_inf = inputs['v_inf']*3.6

        outputs['FltCost'] = 1.1236 * 1947 * EmptyWeight**.325 * v_inf**.822 * fta**1.21

    def compute_partials(self, inputs, partials):
        fta = self.options['fta']

        EmptyWeight = inputs['EmptyWeight']/9.8
        v_inf = inputs['v_inf']*3.6

        partials['FltCost', 'EmptyWeight'] = 1.1236 * 632.775 * EmptyWeight**-.675 * v_inf**.822 * fta**1.21
        partials['FltCost', 'v_inf'] = 1.1236 * 1600.434 * EmptyWeight**.325 * v_inf**-.178 * fta**1.21