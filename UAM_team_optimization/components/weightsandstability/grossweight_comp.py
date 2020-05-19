from openmdao.api import ExplicitComponent


class GrossWeightComp(ExplicitComponent):
    def initialize(self):
        self.options.declare('rho', types=float)

    def setup(self):
        self.add_input('wing_area')
        self.add_input('wing_tc')
        self.add_input('wing_AR')
        self.add_input('wing_span')
        self.add_input('tail_area')
        self.add_input('tail_tc')
        self.add_input('tail_AR')
        self.add_input('tail_span')
        self.add_input('load_factor')
        self.add_input('w_design')
        self.add_input('w_else')
        self.add_input('v_inf')
        self.add_input('w_pax')
        # self.add_output('w_wing')
        # self.add_output('w_tail')
        self.add_output('GrossWeight')

        self.declare_partials('GrossWeight', 'wing_area')
        self.declare_partials('GrossWeight', 'wing_tc')
        self.declare_partials('GrossWeight', 'wing_AR')
        self.declare_partials('GrossWeight', 'tail_area')
        self.declare_partials('GrossWeight', 'tail_tc')
        self.declare_partials('GrossWeight', 'tail_AR')
        self.declare_partials('GrossWeight', 'load_factor')
        self.declare_partials('GrossWeight', 'w_design')
        self.declare_partials('GrossWeight', 'w_else')
        self.declare_partials('GrossWeight', 'w_pax')
        self.declare_partials('GrossWeight', 'v_inf')

    def compute(self, inputs, outputs):
        rho = self.options['rho']

        wing_area = inputs['wing_area']
        wing_tc = inputs['wing_tc']
        wing_AR = inputs['wing_AR']
        wing_span = inputs['wing_span']
        tail_area = inputs['tail_area']
        tail_tc = inputs['tail_tc']
        tail_AR = inputs['tail_AR']
        tail_span = inputs['tail_span']
        w_design = inputs['w_design']
        load_factor = inputs['load_factor']
        w_pax = inputs['w_pax']
        w_else = inputs['w_else']
        v_inf = inputs['v_inf']

        # outputs['w_wing'] = 0.036* \
        #                     (wing_area**0.758)* \
        #                     (wing_AR**0.6)* \
        #                     ((0.5*rho*v_inf*v_inf)**0.006)* \
        #                     ((100*wing_tc)**-0.3)* \
        #                     ((load_factor*w_design)**0.49)
        #
        # outputs['w_tail'] = 0.016* \
        #                     ((load_factor*w_design)**0.414)* \
        #                     ((0.5*rho*v_inf*v_inf)**0.168)* \
        #                     (tail_area**0.896)* \
        #                     ((100*tail_tc)**-0.12)* \
        #                     (tail_AR**0.043)

        # w_wing = outputs['w_wing']
        # w_tail = outputs['w_tail']

        # outputs['GrossWeight'] = w_wing + w_tail + w_else + w_pax

        outputs['GrossWeight'] = 0.036* \
                            (wing_area**0.758)* \
                            (wing_AR**0.6)* \
                            ((0.5*rho*v_inf*v_inf)**0.006)* \
                            ((100*wing_tc)**-0.3)* \
                            ((load_factor*w_design)**0.49) + \
                            0.016* \
                            ((load_factor*w_design)**0.414)* \
                            ((0.5*rho*v_inf*v_inf)**0.168)* \
                            (tail_area**0.896)* \
                            ((100*tail_tc)**-0.12)* \
                            (tail_AR**0.043) + \
                            w_else + w_pax

    def compute_partials(self, inputs, partials):
        rho = self.options['rho']

        wing_area = inputs['wing_area']
        wing_tc = inputs['wing_tc']
        wing_AR = inputs['wing_AR']
        wing_span = inputs['wing_span']
        tail_area = inputs['tail_area']
        tail_tc = inputs['tail_tc']
        tail_AR = inputs['tail_AR']
        tail_span = inputs['tail_span']
        w_design = inputs['w_design']
        load_factor = inputs['load_factor']
        w_pax = inputs['w_pax']
        w_else = inputs['w_else']
        v_inf = inputs['v_inf']

        partials['GrossWeight', 'wing_area'] = 0.036* \
                                               0.758*(wing_area**(1-0.758))* \
                                               (wing_AR**0.6)* \
                                               ((0.5*rho*v_inf*v_inf)**0.006)* \
                                               ((100*wing_tc)**-0.3)* \
                                               ((load_factor*w_design)**0.49)

        partials['GrossWeight', 'wing_tc'] = 0.036* \
                                             (wing_area**0.758)* \
                                             (wing_AR**0.6)* \
                                             ((0.5*rho*v_inf*v_inf)**0.006)* \
                                             100*(-0.3)*((100*wing_tc)**(-0.3-1))* \
                                             ((load_factor*w_design)**0.49)

        partials['GrossWeight', 'wing_AR'] = 0.6*0.036* \
                                             (wing_area**0.758)* \
                                             (wing_AR**-0.4)* \
                                             ((0.5*rho*v_inf*v_inf)**0.006)* \
                                             ((100*wing_tc)**-0.3)* \
                                             ((load_factor*w_design)**0.49)

        partials['GrossWeight', 'tail_area'] = 0.016* \
                                               ((load_factor*w_design)**0.414)* \
                                               ((0.5*rho*v_inf*v_inf)**0.168)* \
                                               0.896*(tail_area**(1-0.896))* \
                                               ((100*tail_tc)**-0.12)* \
                                               (tail_AR**0.043)

        partials['GrossWeight', 'tail_tc'] = 0.016* \
                                             ((load_factor*w_design)**0.414)* \
                                             ((0.5*rho*v_inf*v_inf)**0.168)* \
                                             (tail_area**0.896)* \
                                             100*(-0.12)*((100*tail_tc)**(-0.12-1))* \
                                             (tail_AR**0.043)

        partials['GrossWeight', 'tail_AR'] = 0.043*0.016* \
                                             ((load_factor*w_design)**0.414)* \
                                             ((0.5*rho*v_inf*v_inf)**0.168)* \
                                             (tail_area**0.896)* \
                                             ((100*tail_tc)**-0.12)* \
                                             (tail_AR**-0.957)

        partials['GrossWeight', 'load_factor'] = 0.036* \
                                                 (wing_area**0.758)* \
                                                 (wing_AR**0.6)* \
                                                 ((0.5*rho*v_inf*v_inf)**0.006)* \
                                                 ((100*wing_tc)**-0.3)* \
                                                 w_design*0.49*((load_factor*w_design)**(1-0.49)) + \
                                                 0.016* \
                                                 w_design*0.414*((load_factor*w_design)**(1-0.414))* \
                                                 ((0.5*rho*v_inf*v_inf)**0.168)* \
                                                 (tail_area**0.896)* \
                                                 ((100*tail_tc)**-0.12)* \
                                                 (tail_AR**0.043)

        partials['GrossWeight', 'w_design'] = 0.036* \
                                              (wing_area**0.758)* \
                                              (wing_AR**0.6)* \
                                              ((0.5*rho*v_inf*v_inf)**0.006)* \
                                              ((100*wing_tc)**-0.3)* \
                                              load_factor*0.49*((load_factor*w_design)**(1-0.49)) + \
                                              0.016* \
                                              load_factor*0.414*((load_factor*w_design)**(1-0.414))* \
                                              ((0.5*rho*v_inf*v_inf)**0.168)* \
                                              (tail_area**0.896)* \
                                              ((100*tail_tc)**-0.12)* \
                                              (tail_AR**0.043)

        partials['GrossWeight', 'w_else'] = 1.

        partials['GrossWeight', 'w_pax'] = 1.

        partials['GrossWeight', 'v_inf'] = 0.036* \
                                           (wing_area**0.758)* \
                                           (wing_AR**0.6)* \
                                           ((100*wing_tc)**-0.3)* \
                                           ((load_factor*w_design)**0.49)* \
                                           ((0.5*rho)**0.006)* \
                                           (0.012)* \
                                           (v_inf**(0.012 - 1)) + 0.016* \
                                           ((load_factor*w_design)**0.414)* \
                                           (tail_area**0.896)* \
                                           ((100*tail_tc)**-0.12)* \
                                           (tail_AR**0.043)* \
                                           ((0.5*rho)**0.168)* \
                                           (2*0.168)* \
                                           (v_inf**(2*0.168 - 1))
