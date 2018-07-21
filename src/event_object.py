class EventObject(object):
    def __init__(self):
        pass

    def on_hide(self):
        pass

    def on_show(self):
        pass
 
    def draw(self):
        pass

class DelegatingEventObject(EventObject):
    def __init__(self):
        super(DelegatingEventObject, self).__init__()
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def on_hide(self):
        for child in self.children:
            child.on_hide()

    def on_show(self):
        for child in self.children:
            child.on_show()
 
    def draw(self):
        for child in self.children:
            child.draw()
