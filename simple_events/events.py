import logging

logger = logging.getLogger(__name__)


class Event(object):
    """
    Basic event processor/handler
    """
    def __init__(self, _root=True):
        self._event_listeners = []
        self._root = _root
        if _root:
            self.on_event_added = Event(_root=False)
            self.on_event_removed = Event(_root=False)

    def __iadd__(self, handler):
        self._event_listeners.append(handler)
        if self._root:
            self.on_event_added(event=handler)
        return self

    def __isub__(self, handler):
        if handler in self._event_listeners:
            self._event_listeners.remove(handler)
            if self._root:
                self.on_event_removed(event=handler)
            return self

    def __call__(self, *args, **kwargs):
        for listener in self._event_listeners:
            listener(*args, **kwargs)


class ReactiveList(list):
    """
    List with Events for responding to change
    """
    def __init__(self):
        super().__init__()
        self.on_entry_changed = Event()
        self.on_removed_item = Event()
        self.on_added_item = Event()
        self.on_list_cleared = Event()

    def __setitem__(self, key, value):
        super(ReactiveList, self).__setitem__(key, value)
        self.on_entry_changed(value)
        return self

    def __delitem__(self, value):
        index = self.index(value)
        super(ReactiveList, self).__delitem__(value)
        self.on_removed_item(index)
        return self

    def __add__(self, value):
        super(ReactiveList, self).__add__(value)
        self.on_added_item(value)
        return self

    def __iadd__(self, value):
        super(ReactiveList, self).__iadd__(value)
        self.on_added_item(value)
        return self

    def append(self, value):
        super(ReactiveList, self).append(value)
        self.on_added_item(value)

    def remove(self, value):
        index = self.index(value)
        super(ReactiveList, self).remove(value)
        self.on_removed_item(index)

    def clear(self):
        super(ReactiveList, self).clear()
        self.on_list_cleared()