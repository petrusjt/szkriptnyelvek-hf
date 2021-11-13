#!/usr/bin/env python3
from unittest import TestCase

from hf9.sor_ket_veremmel import SorKetVeremmel


# currently doesn't work because of the way Verem is imported in sor_ket_veremmel.py
class TestSorKetVeremmel(TestCase):
    def test_append(self):
        q = SorKetVeremmel()
        self.assertTrue(q.is_empty())

        q.append(5)
        q.append(4)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.size(), 2)
        q.append(3)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.size(), 3)

    def test_popleft(self):
        q = SorKetVeremmel()
        q.append(1)
        q.append(2)
        q.append(3)

        self.assertFalse(q.is_empty())
        self.assertEqual(q.popleft(), 1)
        self.assertEqual(q.popleft(), 2)
        self.assertEqual(q.popleft(), 3)
        self.assertTrue(q.is_empty())

    def test_is_empty(self):
        q = SorKetVeremmel()
        self.assertTrue(q.is_empty())
        q.append(1)
        self.assertFalse(q.is_empty())

    def test_size(self):
        q = SorKetVeremmel()
        self.assertEqual(q.size(), 0)
        q.append(4)
        q.append(4)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.size(), 2)
        q.popleft()
        q.popleft()
        self.assertTrue(q.is_empty())
