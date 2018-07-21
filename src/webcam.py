import io
import pyglet
import requests

import image_utils

class WebCam(object):
    def __init__(self):
        super(WebCam, self).__init__()
        self.total_bytes = 0
        self.total_time = 0
        self.image = pyglet.resource.image('no_image_available.png')
        image_utils.CenterImage(self.image)
        self.schedule()

    def schedule(self):
        pyglet.clock.schedule_interval(self.update, 0.1)

    def unschedule(self):
        pyglet.clock.unschedule(self.update)

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
        #print('WebCam image: origin:', (self.x, self.y), 'size:',
        #      (self.image.width, self.image.height))

    def draw(self):
        self.image.blit(self.x, self.y)
