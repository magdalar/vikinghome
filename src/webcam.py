import io
import pyglet
import requests

import image_utils


CAM_URL = 'http://192.168.86.34/cam_pic.php'
LOGGING_FREQUENCY_SECS = 300

class WebCam(object):
    def __init__(self):
        super(WebCam, self).__init__()
        self.total_bytes = 0
        self.total_time = 0
        self.last_errors = 0
        self.image = pyglet.resource.image('no_image_available.png')
        image_utils.CenterImage(self.image)
        self.schedule()

    def schedule(self):
        pyglet.clock.schedule_interval(self.update, 0.1)

    def unschedule(self):
        pyglet.clock.unschedule(self.update)

    def update(self, dt):
        self.total_time += dt
        try:
          response = requests.get(CAM_URL)
          if response.status_code != 200:
              if not self.last_errors or self.total_time > LOGGING_FREQUENCY_SECS:
                print('Failed to fetch image from', CAM_URL, 'code was:', response.status_code)
              self.last_errors += 1
              return
          elif self.last_errors > 0:
              print('Success! WebCam has restarted after', self.last_errors, 'errors.')
          self.last_errors = 0
          self.total_bytes += len(response.content)
          image_bytes = io.BytesIO(response.content)
          self.image = pyglet.image.load('cam.jpg', file=image_bytes)
          image_utils.CenterImage(self.image)
        except Exception as e:
            if not self.last_errors or self.total_time > LOGGING_FREQUENCY_SECS:
                print('Failed to fetch WebCam:', e)
            self.last_errors += 1
        else:
            if self.total_time > LOGGING_FREQUENCY_SECS:
                print('WebCam Average KiB/s:', int(self.total_bytes / self.total_time / 1024))
                self.total_bytes = 0
                self.total_time = 0

    def draw(self):
        self.image.blit(self.x, self.y)
