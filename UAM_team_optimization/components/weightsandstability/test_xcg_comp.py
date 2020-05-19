from openmdao.api import ExplicitComponent
import numpy as np

class XCGComp(ExplicitComponent):

    def setup(self):
        self.add_input('l')
        self.add_input('w')
        self.add_output('A')

        self.declare_partials('A', 'l')
        self.declare_partials('A', 'w')

    def compute(self, inputs, outputs):
        l = inputs['l']
        w = inputs['w']

        outputs['A'] = l * w

    def compute_partials(self, inputs, partials):
        l = inputs['l']
        w = inputs['w']

        partials['A', 'l'] = w
        partials['A', 'w'] = l
