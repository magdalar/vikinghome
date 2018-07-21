class DelegatingEventObject(object):
    def __init__(self):
        super(DelegatingEventObject, self).__init__()
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def on_hide(self):
        for child in self.children:
            if hasattr(child, 'on_hide'):
                child.on_hide()

    def on_show(self):
        for child in self.children:
            if hasattr(child, 'on_show'):
                child.on_show()
 
    def draw(self):
        for child in self.children:
            if hasattr(child, 'draw'):
                child.draw()
