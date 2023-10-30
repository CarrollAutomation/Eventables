class EventTestClass:
    def __init__(self):
        from src.eventables.events import Event
        self.event1 = Event()
        self.test_number = 0

    def increase_test_num(self, num2):
        self.test_number += num2

    def increase_with_index(self, index, number):
        self.test_number += number

    def call_events(self, number):
        self.event1(number)
