#!/usr/bin/env python
"""Provides TestSatSolver with test cases for any SatSolverInterface
"""

import unittest
from InMemoryMetrics import InMemoryMetrics

__author__ = "Meena Alfons"
__copyright__ = "Copyright 2020, Knowledge Representation, SatSolver Project, Group 25"
__credits__ = ["Meena Alfons"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Meena Alfons"
__email__ = "meena.kerolos@gmail.com"
__status__ = "Development"

class TestSatSolver(unittest.TestCase):
    def setSatSolverClass(self, SatSolverClass):
        self.SatSolverClass = SatSolverClass

    def all(self):
        """
        Test All cases for SatSolver
        """
        tests = [{
            "cnf": [[-1],[2]],
            "numOfVars": 2,
            "expectedResult": "SAT",
            "expectDontCare": False
        },{
            "cnf": [[-1,2]],
            "numOfVars": 2,
            "expectedResult": "SAT",
            "expectDontCare": False
        },{
            "cnf": [[1,2,3], [1,-2],[1,-3],[-1,3]],
            "numOfVars": 3,
            "expectedResult": "SAT",
            "expectDontCare": False
        }]

        metrics = InMemoryMetrics()
        for test in tests:
            solver = self.SatSolverClass(test["cnf"], test["numOfVars"], metrics)
            result, model = solver.solve()
            self.assertEqual(result, test["expectedResult"])
            if test["expectedResult"] == "SAT":
                isSat, someDontCare = self.validate(test["cnf"], model)
                self.assertTrue(isSat)
                self.assertEqual(test["expectDontCare"], someDontCare)
        print("Totals: deduce={}".format(metrics.getDeduceCount()))


    def validate(self, cnf, model):
        someDontCare = False

        for clause in cnf:
            clauseIsSat = False
            for literal in clause:
                variable = abs(literal)
                if variable in model:
                    value = model[variable]
                    literalValue = value if literal > 0 else not value
                    if literalValue == True:
                        clauseIsSat = True
                        break
                else:
                    someDontCare = True

            if clauseIsSat == False:
                return False, someDontCare

        return True, someDontCare