import time
from picamera2 import Picamera2

with picamera2.PiCamera2() as camera:
    #camera.resolution = (1280, 720)
    config = camera.create_preview_configuration()
	camera.configure(config)
    camera.start_preview(Preview.QTGL)
    #camera.start_recording('my_video.h264')
    time.sleep(0.5)
    
    x = 0.0
    y = 0.0
    w = 1.0
    h = 1.0
    
    while True:
    	key = input()
    	if key == '+':
    		if x < 0.4:
	    		camera.zoom=(x+0.1, y+0.1, w-0.1, h-0.1)
    			time.sleep(0.1)
    	elif key == '-':
    		if x > 0.0:
				camera.zoom=(x-0.1, y-0.1, w+0.1, h+0.1)
				time.sleep(0.1)
		elif key == 'q':
			camera.stop_preview()
			break
