import cv2
vidcap = cv2.VideoCapture('/Users/ryan/Downloads/test_3.mp4')
success,image = vidcap.read()
count = 0
while success:
	success,image = vidcap.read()
	# print('Read a new frame: ', success)
	if count%10 == 0:
	  cv2.imwrite("frame%d.jpg" % count, image)
	  print('file saved')    # save frame as JPEG file      
	count += 1