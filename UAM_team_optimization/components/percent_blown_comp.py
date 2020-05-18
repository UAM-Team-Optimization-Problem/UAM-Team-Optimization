from openmdao.api import ExplicitComponent
import numpy as np

class PercentBlownComp(ExplicitComponent):

    def setup(self):
        # Wing
        self.add_input('wing_prop_inner_rad')
        self.add_input('wing_prop_outer_rad')
        self.add_input('wing_span')
        self.add_output('wing_blown_percent')

        self.declare_partials('wing_blown_percent','wing_prop_inner_rad')
        self.declare_partials('wing_blown_percent','wing_prop_outer_rad')
        self.declare_partials('wing_blown_percent','wing_span')
        # Tail 
        self.add_input('tail_prop_rad')
        self.add_input('tail_span')
        self.add_output('tail_blown_percent')

        self.declare_partials('tail_blown_percent','tail_prop_rad')
        self.declare_partials('tail_blown_percent','tail_span')


    def compute(self, inputs, outputs):
        # Wing
        wing_prop_inner_rad = inputs['wing_prop_inner_rad']
        wing_prop_outer_rad = inputs['wing_prop_outer_rad']
        wing_span = inputs['wing_span']
        outputs['wing_blown_percent'] = 2*(2*wing_prop_inner_rad + 2*wing_prop_outer_rad)/wing_span
        # Tail
        tail_prop_rad = inputs['tail_prop_rad']
        tail_span = inputs['tail_span']
        outputs['tail_blown_percent'] = 4*tail_prop_rad/tail_span

    def compute_partials(self, inputs, partials):
        # Wing
        wing_prop_inner_rad = inputs['wing_prop_inner_rad']
        wing_prop_outer_rad = inputs['wing_prop_outer_rad']
        wing_span = inputs['wing_span']
        
        partials['wing_blown_percent', 'wing_prop_inner_rad'] = 4/wing_span
        partials['wing_blown_percent', 'wing_prop_outer_rad'] = 4/wing_span
        partials['wing_blown_percent', 'wing_span'] = -4*(wing_prop_inner_rad + wing_prop_outer_rad)*wing_span**-2

        # Tail
        tail_prop_rad = inputs['tail_prop_rad']
        tail_span = inputs['tail_span']

        partials['tail_blown_percent','tail_prop_rad'] = 4/tail_span
        partials['tail_blown_percent','tail_span'] = -4*tail_prop_rad*tail_span**-2