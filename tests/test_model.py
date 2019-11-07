#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for the model subpackage
"""

import unittest
import pyrsa.model as model
import numpy as np

class test_Model(unittest.TestCase):
    """ Tests for the Model superclass
    """
    def test_creation(self):
        m = model.Model('Test Model')


class test_ModelFixed(unittest.TestCase):
    """ Tests for the fixed model class
    """
    def test_creation(self):
        rdm = np.array(np.ones(6))
        m = model.ModelFixed('Test Model',rdm)
        m.fit([])
        pred = m.predict()
        assert np.all(pred == rdm)
        