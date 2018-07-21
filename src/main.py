import pyglet

from pyglet.window import key
from pyglet.window import mouse

import webcam

class VikingHomeWindow(pyglet.window.Window):
    def __init__(self):
        super(VikingHomeWindow, self).__init__(caption='VikingHome')
        self.webcam_panel = webcam.WebCamPanel(self)
        #self.push_handlers(pyglet.window.event.WindowEventLogger())

    def on_draw(self):
        self.clear()
        self.webcam_panel.draw()

    def on_hide(self):
        self.webcam_panel.on_hide()

    def on_show(self):
        self.webcam_panel.on_show()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.Q:
            print('User requested we exit.')
            pyglet.app.exit()
        elif symbol == key.C:
            print('Updating image')
            webcam.update()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            print('The left mouse button was pressed.')

if __name__ == '__main__':
    pyglet.resource.path = ['../resources']
    pyglet.resource.reindex()
    window = VikingHomeWindow()
    pyglet.app.run()
