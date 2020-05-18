import unittest

from UAM_team_optimization.components.geometry_comp import GeometryComp
from openmdao.api import Problem
from openmdao.utils.assert_utils import assert_check_partials 


class TestGeometryComp(unittest.TestCase):

    def test_component_and_derivatives(self):
        prob = Problem()
        prob.model = GeometryComp()
        prob.setup()
        prob.run_model()

        data = prob.check_partials(out_stream = None)
        assert_check_partials(data, atol = 1.e-3, rtol = 1.e-3)

if __name__ == '__main__':
    unittest.main()
         
