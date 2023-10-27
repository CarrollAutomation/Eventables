import logging

logger = logging.getLogger(__name__)


class Event(object):
    """
    Basic event processor/handler

    :_root:
        Parameter to signify if the Event should have sub Events for "on_event" changes.
        Default is False. If True the generated sub events will not have further sub events.
    """
    def __init__(self, _root=False):
        self._event_listeners = []
        self._root = _root
        if _root:
            self.on_event_added = Event(_root=False)
            self.on_event_removed = Event(_root=False)

    def __iadd__(self, func):
        self._event_listeners.append(func)
        if self._root:
            self.on_event_added(event=func)
        return self

    def __isub__(self, func):
        if func in self._event_listeners:
            self._event_listeners.remove(func)
            if self._root:
                self.on_event_removed(event=func)
            return self

    def __call__(self, *args, **kwargs):
        for listener in self._event_listeners:
            listener(*args, **kwargs)


class EventList(list):
    """
    Modified mutable sequence with Events for responding to change

    on_entry_changed (value)
        Runs when += or .append is called
        value = value/object that was added to the list
    on_entry_removed (index, value)
        Runs when -= or .remove is called
        index = index of removed item
        value = object/value that was removed
    on_entries_cleared ()
        Runs when object is
    """
    def __init__(self):
        test = list
        super().__init__()
        self.on_entry_changed = Event()
        self.on_entry_added = Event()
        self.on_entry_removed = Event()
        self.on_entries_cleared = Event()

    def __setitem__(self, key, value):
        super(EventList, self).__setitem__(key, value)
        self.on_entry_changed(value)
        return self

    def __delitem__(self, value):
        index = self.index(value)
        super(EventList, self).__delitem__(value)
        self.on_entry_added(index)
        return self

    def __add__(self, value):
        super(EventList, self).__add__(value)
        self.on_entry_removed(value)
        return self

    def __iadd__(self, value):
        super(EventList, self).__iadd__(value)
        self.on_entry_removed(value)
        return self

    def append(self, value):
        super(EventList, self).append(value)
        self.on_entry_removed(value)

    def remove(self, value):
        index = self.index(value)
        super(EventList, self).remove(value)
        self.on_entry_added(index)

    def clear(self):
        super(EventList, self).clear()
        self.on_entries_cleared()