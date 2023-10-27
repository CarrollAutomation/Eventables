import unittest

from simple_events.events import Event
from tests.models import EventTestClass


class EventTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setup(self):
        pass

    def tearDown(self):
        pass

    def test_event_add(self):
        test_event = Event()

    def test_event_remove(self):
        pass

    def test_event_run(self):
        test_class = EventTestClass()
        test_class.call_events(5)
        self.assertEqual(test_class.test_number, 5, f"Test number did not increase during event call")

    def test_event_list(self):
        pass
