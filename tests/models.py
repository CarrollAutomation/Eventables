class EventTestClass:
    def __init__(self):
        from simple_events.events import Event
        self.event1 = Event()
        self.test_number = 0

    def increase_test_num(self, num2):
        self.test_number += num2

    def call_events(self, number):
        self.event1(number)
