import numpy as np
from openmdao.api import ExplicitComponent


class ProfitComp(ExplicitComponent):

    def setup(self):
        self.add_input('Fare')
        self.add_input('distance')
        self.add_input('EnergyCost')
        self.add_input('v_inf')
        self.add_input('t_tol')
        self.add_input('cost_km')
        self.add_input('years')
        self.add_input('flthr_yr')
        self.add_input('quantity')
        self.add_input('Ac')
        self.add_input('energy_expenditure_per_trip_kWh')
        self.add_output('Profit')

        self.declare_partials('Profit', 'Fare')
        self.declare_partials('Profit', 'v_inf')
        self.declare_partials('Profit', 'EnergyCost')
        self.declare_partials('Profit', 'distance')
        self.declare_partials('Profit', 't_tol')
        self.declare_partials('Profit', 'cost_km')
        self.declare_partials('Profit', 'years')
        self.declare_partials('Profit', 'flthr_yr')
        self.declare_partials('Profit', 'quantity')
        self.declare_partials('Profit', 'Ac')
        self.declare_partials('Profit', 'energy_expenditure_per_trip_kWh')
    def compute(self, inputs, outputs):
        Fare = inputs['Fare']
        v_inf = inputs['v_inf']*3.6
        distance = inputs['distance']/1000 
        EnergyCost = inputs['EnergyCost']
        t_tol = inputs['t_tol']
        cost_km = inputs['cost_km']
        quantity = inputs['quantity']
        flthr_yr = inputs['flthr_yr']
        years = inputs['years']
        Ac = inputs['Ac']
        energy_expenditure_per_trip_kWh = inputs['energy_expenditure_per_trip_kWh']
        outputs['Profit'] = (years * quantity*flthr_yr)* ( (Fare / ((distance/v_inf)+t_tol)) - (cost_km* distance/ ((distance/v_inf)+t_tol)) -(energy_expenditure_per_trip_kWh*EnergyCost)) - (quantity*Ac)
    def compute_partials(self, inputs, partials):
        Fare = inputs['Fare']
        v_inf = inputs['v_inf']*3.6
        distance = inputs['distance']/1000
        EnergyCost = inputs['EnergyCost']
        t_tol = inputs['t_tol']
        cost_km = inputs['cost_km']
        quantity = inputs['quantity']
        flthr_yr = inputs['flthr_yr']
        years = inputs['years']
        Ac = inputs['Ac']
        energy_expenditure_per_trip_kWh = inputs['energy_expenditure_per_trip_kWh']
        partials['Profit', 'years'] = (quantity*flthr_yr)* ( (Fare / ((distance/v_inf)+t_tol)) - (cost_km* distance/ ((distance/v_inf)+t_tol)) -(energy_expenditure_per_trip_kWh*EnergyCost))
        partials['Profit', 'flthr_yr'] = (years * quantity)* ( (Fare / ((distance/v_inf)+t_tol)) - (cost_km* distance/ ((distance/v_inf)+t_tol)) -(energy_expenditure_per_trip_kWh*EnergyCost))
        partials['Profit', 'energy_expenditure_per_trip_kWh'] = -flthr_yr*EnergyCost*quantity*years
        partials['Profit', 'Fare'] = (flthr_yr*quantity*years)/((distance/v_inf)+t_tol)
        partials['Profit', 'v_inf'] = distance* (Fare-cost_km*distance)*(flthr_yr*quantity*years)/(t_tol*v_inf +distance)**2
        partials['Profit', 'distance'] = (flthr_yr*quantity*years*v_inf*(cost_km*t_tol*v_inf +Fare))/ (t_tol*v_inf +distance)**2
        partials['Profit', 'EnergyCost'] = -flthr_yr*energy_expenditure_per_trip_kWh*quantity*years
        partials['Profit', 't_tol'] = -(Fare- cost_km*distance)*(flthr_yr*quantity*years)*(v_inf**2)/(t_tol*v_inf +distance)**2 
        partials['Profit', 'Ac'] = -quantity
        partials['Profit', 'cost_km'] = - (distance * flthr_yr * quantity *  years ) / ( (distance/v_inf) + (t_tol))   
        partials['Profit', 'quantity'] = flthr_yr * years* ((Fare / ((distance/v_inf)+t_tol)) - (cost_km* distance/ ((distance/v_inf)+t_tol)) -(energy_expenditure_per_trip_kWh*EnergyCost)) - Ac