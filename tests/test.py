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
        test_class = EventTestClass()
        test_class.event1 += test_class.increase_test_num
        self.assertEqual(len(test_class.event1._event_listeners), 1, "Event not successfully added")

    def test_event_remove(self):
        test_class = EventTestClass()
        test_class.event1 += test_class.increase_test_num
        test_class.event1 -= test_class.increase_test_num
        self.assertEqual(len(test_class.event1._event_listeners), 0, "Event not successfully removed")

    def test_event_run(self):
        test_class = EventTestClass()
        test_class.event1 += test_class.increase_test_num
        test_class.call_events(5)
        self.assertEqual(test_class.test_number, 5, f"Test number did not increase during event call")

    def test_event_sub_events(self):
        test_event = Event()
        self.assertEqual(type(test_event.on_event_added), Event, "Event sub event on_event_added not created")
        self.assertEqual(type(test_event.on_event_removed), Event, "Event sub event on_event_removed not created")
        self.assertEqual(getattr(test_event.on_event_added, "on_event_added", None), None,
                         "Event sub sub event on_event_added is not None")
        self.assertEqual(getattr(test_event.on_event_added, "on_event_removed", None), None,
                         "Event sub sub event on_event_removed is not None")

    def test_event_list(self):
        pass
