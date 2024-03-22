from picamera2 import Picamera2, Preview
import io
from PIL import Image
import time

class Camera:
    def __init__(self):
        self.camera = Picamera2()
        self.preview_config = self.camera.create_preview_configuration()
        self.capture_config = self.camera.create_still_configuration()
        self.camera.configure(self.preview_config)
        self.camera.start()
        time.sleep(2)

    def take_image(self, path="image.jpg"):
        self.camera.switch_mode_and_capture_file(self.capture_config, path)
        image = Image.open(path)
        return image

if __name__ == "__main__":
    camera = Camera()
    image = camera.take_image()
    # image.show()
