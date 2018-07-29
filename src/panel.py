class Panel(object):
    def __init__(self, name, screen_size, relative_panel_size,
                 relative_origin, batch):
        self.name = name
        self.relative_panel_size = relative_panel_size
        self.relative_origin = relative_origin
        self.children = []
        self.click_event_handlers = []
        self.batch = batch
        self.on_resize(screen_size[0], screen_size[1])

    def add_child(self, child):
        child.x = self.origin[0] + int(
            child.relative_origin[0] * self.panel_size[0])
        child.y = self.origin[1] + int(
            child.relative_origin[1] * self.panel_size[1])
        child.batch = self.batch
        self.children.append(child)
        self.click_event_handlers.append(None)

    def add_click_event_handler(self, child, handler):
        i = 0
        for candidate in self.children:
            if candidate is child:
                self.click_event_handlers[i] = handler
                return
            i += 1
        else:
            raise Exception('No such child found.')

    def on_mouse_press(self, x, y, button, modifiers):
        i = 0
        print('Click:', (x,y))
        for child in self.children:
            handler = self.click_event_handlers[i]
            i += 1
            if not handler:
                continue
            bounds = self._get_child_bounds(child)
            if not bounds:
                continue
            print('Child bounds:', bounds)
            if x > bounds[0][0] and x < bounds[1][0] and y > bounds[0][1] and y < bounds[1][1]:
                handler(x, y, button, modifiers)

    def _get_child_bounds(self, child):
        if hasattr(child, 'content_width'):
            return ((child.x, child.y), (child.x + child.content_width, child.y + child.content_height))
        elif hasattr(child, 'width'):
            return ((child.x, child.y), (child.x + child.width, child.y + child.height))
        else:
            return None

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
