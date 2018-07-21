class Panel(object):
    def __init__(self, name, screen_size, relative_panel_size,
                 relative_origin, batch):
        self.name = name
        self.relative_panel_size = relative_panel_size
        self.relative_origin = relative_origin
        self.children = []
        self.batch = batch
        self.on_resize(screen_size[0], screen_size[1])

    def add_child(self, child):
        child.x = self.origin[0] + int(
            child.relative_origin[0] * self.panel_size[0])
        child.y = self.origin[1] + int(
            child.relative_origin[1] * self.panel_size[1])
        child.batch = self.batch
        self.children.append(child)

    def on_resize(self, width, height):
        self.screen_size = (width, height)
        origin_x = int(width * self.relative_origin[0])
        origin_y = int(height * self.relative_origin[1])
        self.origin = (origin_x, origin_y)

        panel_width = int(width * self.relative_panel_size[0])
        panel_height = int(height * self.relative_panel_size[1])
        self.panel_size = (panel_width, panel_height)
        print("Panel:", self.name, "Origin:", self.origin,
              "Size:", self.panel_size)

        for child in self.children:
            child.x = self.origin[0] + int(
                child.relative_origin[0] * self.panel_size[0])
            child.y = self.origin[1] + int(
                child.relative_origin[1] * self.panel_size[1])

    def draw(self):
        for child in self.children:
            if hasattr(child, 'draw'):
                child.draw()
