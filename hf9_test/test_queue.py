#!/usr/bin/env python3
from unittest import TestCase

from hf9.queue import Sor


class TestSor(TestCase):

    def test_ures(self):
        q = Sor()
        self.assertTrue(q.ures())
        q.betesz(1)
        self.assertFalse(q.ures())

    def test_betesz(self):
        q = Sor()
        self.assertTrue(q.ures())

        q.betesz(5)
        q.betesz(4)
        self.assertFalse(q.ures())
        self.assertEqual(q.meret(), 2)
        q.betesz(3)
        self.assertFalse(q.ures())
        self.assertEqual(q.meret(), 3)

    def test_kivesz(self):
        q = Sor()
        q.betesz(1)
        q.betesz(2)
        q.betesz(3)

        self.assertFalse(q.ures())
        self.assertEqual(q.kivesz(), 1)
        self.assertEqual(q.kivesz(), 2)
        self.assertEqual(q.kivesz(), 3)
        self.assertTrue(q.ures())

    def test_meret(self):
        q = Sor()
        self.assertEqual(q.meret(), 0)
        q.betesz(4)
        q.betesz(4)
        self.assertFalse(q.ures())
        self.assertEqual(q.meret(), 2)
        q.kivesz()
        q.kivesz()
        self.assertTrue(q.ures())
