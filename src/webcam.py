import io
import pyglet
import requests

import event_object
import image_utils

class WebCam(object):
    def __init__(self, window):
        super(WebCam, self).__init__()
        self.window = window
        self.total_bytes = 0
        self.total_time = 0
        self.image = pyglet.resource.image('no_image_available.png')
        image_utils.CenterImage(self.image)
        self.schedule()

    def schedule(self):
        pyglet.clock.schedule_interval(self.update, 0.1)

    def unschedule(self):
        pyglet.clock.unschedule(self.update)

    def on_hide(self):
        self.unschedule()

    def on_show(self):
        self.schedule()

    def update(self, dt=None):
        cam_url = 'http://192.168.86.24/cam_pic.php'
        response = requests.get(cam_url)
        if response.status_code != 200:
            print('Failed to fetch image from', cam_url, 'code was:', response.status_code)
        size = len(response.content)
        if dt:
            self.total_bytes += size
            self.total_time += dt
            #print('Avg KiB/s:', int(self.total_bytes / self.total_time / 1024))
        image_bytes = io.BytesIO(response.content)
        self.image = pyglet.image.load('cam.jpg', file=image_bytes)
        image_utils.CenterImage(self.image)

    def draw(self):
        self.image.blit(self.window.width // 2, self.window.height // 2)

class WebCamPanel(event_object.DelegatingEventObject):
    def __init__(self, window):
        super(WebCamPanel, self).__init__()
        self.webcam = WebCam(window)
        self.label = pyglet.text.Label(
            'TyCam',
            font_name='Times New Roman', font_size=36,
            x=window.width//2, y=window.height-30,
            anchor_x='center',
            anchor_y='center')
        self.add_child(self.webcam)
        self.add_child(self.label)
