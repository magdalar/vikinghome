import socket
import sys
import pyglet
import requests
from io import BytesIO
from pyglet.window import key
from pyglet.window import mouse

def CenterImage(img):
    img.anchor_x = img.width // 2
    img.anchor_y = img.height // 2

class WebCam:
    def __init__(self, window):
        self.window = window
        self.total_bytes = 0
        self.total_time = 0
        self.image = pyglet.image.load('resources/no_image_available.png')
        CenterImage(self.image)

    def update(self, dt=None):
        cam_url = 'http://192.168.86.24/cam_pic.php'
        response = requests.get(cam_url)
        if response.status_code != 200:
            print('Failed to fetch image from', cam_url, 'code was:', response.status_code)
        size = len(response.content)
        if dt:
            self.total_bytes += size
            self.total_time += dt
            print('Avg KiB/s:', int(self.total_bytes / self.total_time / 1024))
        image_bytes = BytesIO(response.content)
        self.image = pyglet.image.load('cam.jpg', file=image_bytes)
        CenterImage(self.image)

    def draw(self):
        self.image.blit(self.window.width // 2, self.window.height // 2)


#window = pyglet.window.Window(fullscreen=True)
window = pyglet.window.Window()

webcam = WebCam(window)

pyglet.clock.schedule_interval(webcam.update, 0.1)

label = pyglet.text.Label('TyCam',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height-30,
                          anchor_x='center', anchor_y='center')

window.push_handlers(pyglet.window.event.WindowEventLogger())

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.Q:
        print('User requested we exit.')
        pyglet.app.exit()
    elif symbol == key.C:
        print('Updating image')
        webcam.update()

@window.event
def on_draw():
    window.clear()
    label.draw()
    webcam.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('The left mouse button was pressed.')

pyglet.app.run()

