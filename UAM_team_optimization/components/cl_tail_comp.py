from openmdao.api import ExplicitComponent


class CLTailComp(ExplicitComponent):
# cl for section of the tail that is NOT affected by propeller slip stream
    def setup(self):
        self.add_input('tail_alpha')
        self.add_input('tail_CLa')
        self.add_input('tail_CL0')
        self.add_input('axial_int_fac')
        self.add_input('tail_blown_percent')
        
        self.add_output('tail_CL')

        self.declare_partials('tail_CL','tail_alpha')
        self.declare_partials('tail_CL','tail_CLa')
        self.declare_partials('tail_CL','tail_CL0')
        self.declare_partials('tail_CL','axial_int_fac')
        self.declare_partials('tail_CL','tail_blown_percent')
        

    def compute(self, inputs, outputs):
        tail_alpha = inputs['tail_alpha']
        tail_CLa = inputs['tail_CLa']
        tail_CL0 = inputs['tail_CL0']
        axial_int_fac = inputs['axial_int_fac']
        tail_blown_percent = inputs['tail_blown_percent']

        outputs['tail_CL'] = (tail_CLa * tail_alpha + tail_CL0) + (tail_CLa * tail_alpha + tail_CL0)*tail_blown_percent*((1+axial_int_fac)**2 - 1)

    def compute_partials(self, inputs, partials):
        tail_alpha = inputs['tail_alpha']
        tail_CLa = inputs['tail_CLa']
        tail_CL0 = inputs['tail_CL0']
        axial_int_fac = inputs['axial_int_fac']
        tail_blown_percent = inputs['tail_blown_percent']

        partials['tail_CL', 'tail_alpha'] = tail_CLa + tail_CLa*tail_blown_percent*((1+axial_int_fac)**2 - 1)
        partials['tail_CL', 'tail_CLa'] = tail_alpha + tail_alpha*tail_blown_percent*((1+axial_int_fac)**2 - 1)
        partials['tail_CL', 'tail_CL0'] = 1 + tail_blown_percent*((1+axial_int_fac)**2 - 1)
        partials['tail_CL','axial_int_fac'] = 2*(tail_CLa * tail_alpha + tail_CL0)*tail_blown_percent*(1+axial_int_fac)
        partials['tail_CL', 'tail_blown_percent'] = (tail_CLa * tail_alpha + tail_CL0)*((1+axial_int_fac)**2 - 1)