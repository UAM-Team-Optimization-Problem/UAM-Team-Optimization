from openmdao.api import ExplicitComponent
import numpy as np


class GeometryComp(ExplicitComponent):
    def setup(self):
        self.add_input('wing_AR')
        self.add_input('wing_area')
        self.add_input('tail_AR')
        self.add_input('tail_area')
        
        self.add_output('wing_span')
        self.add_output('tail_span')

        self.declare_partials('wing_span','wing_AR')
        self.declare_partials('wing_span','wing_area')
        self.declare_partials('tail_span','tail_AR')
        self.declare_partials('tail_span','tail_area')



    def compute(self, inputs, outputs):
        wing_AR = inputs['wing_AR']
        wing_area = inputs['wing_area']
        tail_AR = inputs['tail_AR']
        tail_area = inputs['tail_area']
        
        outputs['wing_span'] = np.sqrt(wing_AR * wing_area)
        outputs['tail_span'] = np.sqrt(tail_AR * tail_area)

    def compute_partials(self, inputs, partials):
        wing_AR = inputs['wing_AR']
        wing_area = inputs['wing_area']
        tail_AR = inputs['tail_AR']
        tail_area = inputs['tail_area']

        partials['wing_span', 'wing_AR'] = 0.5 * wing_area*(np.sqrt(wing_AR*wing_area))**-1
        partials['wing_span', 'wing_area'] = 0.5 * wing_AR*(np.sqrt(wing_AR*wing_area))**-1
        partials['tail_span', 'tail_AR'] = 0.5 * tail_area*(np.sqrt(tail_AR*tail_area))**-1
        partials['tail_span', 'tail_area'] = 0.5 * tail_AR*(np.sqrt(tail_AR*tail_area))**-1