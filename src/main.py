import pyglet

from pyglet.window import key
from pyglet.window import mouse

import panel
import webcam

class TextLabel(pyglet.text.Label):
    def __init__(self, content, relative_origin, font_size=36, anchor_x='center', anchor_y='center'):
        super(TextLabel, self).__init__(
            content,
            font_name='Times New Roman', font_size=font_size,
            anchor_x=anchor_x, anchor_y=anchor_y)
        self.name = content
        self.relative_origin = relative_origin

    def PrintOrigin(self):
        print('Label: ', self.name, ' Origin:', (self.x, self.y),
              'Size:', (self.content_width, self.content_height))

class WebCamPanel(panel.Panel):
    def __init__(self, **kwargs):
        super(WebCamPanel, self).__init__(**kwargs)
        self.label = TextLabel('TyCam', relative_origin=(0.5, 0.95))
        self.add_child(self.label)
        self.label.PrintOrigin()

        self.webcam = webcam.WebCam()
        self.webcam.relative_origin = (0.5, 0.58)
        self.add_child(self.webcam)
        print('WebCam image: origin:', (self.webcam.x, self.webcam.y), 'size:',
              (self.webcam.image.width, self.webcam.image.height))

        #self.record_label = TextLabel(
        #    'Record (90s)',
        #    relative_origin=(0.5, 0.1), font_size=18)
        #self.add_child(self.record_label)
        #self.record_label.PrintOrigin()

        self.quit_label = TextLabel(
            'Quit',
            relative_origin=(0.5, 0.1), font_size=18,
            anchor_x='left', anchor_y='bottom')
        self.add_child(self.quit_label)
        self.quit_label.PrintOrigin()
        self.add_click_event_handler(self.quit_label, self.quit_clicked)

    def quit_clicked(self, x, y, button, modifiers):
        print('Quit clicked!')
        pyglet.app.exit()

class LightsPanel(panel.Panel):
    def __init__(self, **kwargs):
        super(LightsPanel, self).__init__(**kwargs)
        self.label = TextLabel('Lights', relative_origin=(0.5, 0.9))
        self.add_child(self.label)
        self.label.PrintOrigin()

class SonosPanel(panel.Panel):
    def __init__(self, **kwargs):
        super(SonosPanel, self).__init__(**kwargs)
        self.label = TextLabel('Sonos', relative_origin=(0.5, 0.9))
        self.add_child(self.label)
        self.label.PrintOrigin()

class VikingHomeWindow(pyglet.window.Window):
    def __init__(self, screen_size=(800, 480)):
        super(VikingHomeWindow, self).__init__(
            caption='VikingHome',
            fullscreen=True,
            width=screen_size[0],
            height=screen_size[1])
        self.batch = pyglet.graphics.Batch()

        self.panels = []
        self.panels.append(WebCamPanel(
            name='WebCamPanel',
            screen_size=screen_size,
            relative_panel_size=(0.64, 1.0),
            relative_origin=(0, 0),
            batch=self.batch))

        #self.panels.append(SonosPanel(
        #    name='SonosPanel',
        #    screen_size=screen_size,
        #    relative_panel_size=(0.36, 0.5),
        #    relative_origin=(0.64, 0),
        #    batch=self.batch))

        #self.panels.append(LightsPanel(
        #    name='LightsPanel',
        #    screen_size=screen_size,
        #    relative_panel_size=(0.36, 0.5),
        #    relative_origin=(0.64, 0.5),
        #    batch=self.batch))

        #self.push_handlers(pyglet.window.event.WindowEventLogger())

    def on_resize(self, width, height):
        print('Window Resize:', (width, height))
        for panel in self.panels:
            panel.on_resize(width, height)
        super(VikingHomeWindow, self).on_resize(width, height)

    def on_draw(self):
        self.clear()
        self.batch.draw()
        for panel in self.panels:
            panel.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.Q:
            print('User requested we exit.')
            pyglet.app.exit()
        elif symbol == key.C:
            print('Updating image')
            webcam.update()

    def on_mouse_press(self, x, y, button, modifiers):
        for panel in self.panels:
            panel.on_mouse_press(x, y, button, modifiers)

if __name__ == '__main__':
    pyglet.resource.path = ['../resources']
    pyglet.resource.reindex()
    window = VikingHomeWindow()
    pyglet.app.run()
