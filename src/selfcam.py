import cv2
import pyglet
import pyzbar.pyzbar as pyzbar

import image_utils

class SelfCam(object):
    def __init__(self):
        self.capture = cv2.VideoCapture(0)
        # TODO: When do I call self.capture.release()?
        self.image = pyglet.resource.image('no_image_available.png')
        image_utils.CenterImage(self.image)
        self.schedule()

    def schedule(self):
        pyglet.clock.schedule_interval(self.update, 0.1)

    def unschedule(self):
        pyglet.clock.unschedule(self.update)

    def update(self, dt):
        retval, self.image = cap.read()
        if not retval or not self.image:
          print('Failed to capture video frame.')
          return
        #decodedObjects = pyzbar.decode(frame)
        #for obj in decodedObjects:
        image_utils.CenterImage(self.image)

    def draw(self):
        self.image.blit(self.x, self.y)
