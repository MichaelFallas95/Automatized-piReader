import io
import picamera
import time

my_file = open('/tmp/image.jpg', 'wb')

with picamera.PiCamera() as camera:
	camera.sharpness = 0
	camera.contrast = 0
	camera.brightness = 50
	camera.saturation = 0
	camera.ISO = 0
	camera.video_stabilization = False
	camera.exposure_mode = 'auto'
	camera.meter_mode = 'average'
	camera.awb_mode = 'auto'
	camera.image_effect = 'none'
	camera.color_effects = None
	camera.rotation = 0
	camera.hflip = False
	camera.vflip = False
	camera.start_preview()
	time.sleep(5)
	camera.capture(my_file)

my_file.close() 
