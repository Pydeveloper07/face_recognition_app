
def takePhoto():
	"""
	@return: returns tuple depending on the case"
	@case 1: If there is a problem with opening camera returns (False, Problem)
	@case 2: If user chooses to close the camera returns (False, Problem)
	@case 3: If everything is succesfull return (True, filename)
	@actions: There are two actions which can be done
	@action 1: Escape key exits the camera without taking photo
	@action 2: Space key takes photo and exits the camera
	"""
	import cv2
	import time

	cap = cv2.VideoCapture(0)

	while True:
		
		# Taking frame
		ret, frame = cap.read()
		
		# If there is a problem with a camera returns
		if not ret:
			return False, 'Problem with camera occurred'

		# Showing the frame
		cv2.imshow('Press "Space" key to take a photo', frame)

		# Expects keyboard press
		k = cv2.waitKey(1)
		
		# Pressing Escape key closes the camera
		if k % 256 == 27:
			return False, 'User refused to take photo'

		# Pressing the Space key takes photo
		elif k % 256 == 32:
			# Taking current time in seconds
			sec = str(time.time()).replace('.', '')
			# Getting image name ready
			img_name = f'{sec}.jpg'
			# Saving image
			cv2.imwrite(img_name, frame)
			# Exiting
			cap.release()
			cv2.destroyAllWindows()
			return True, img_name
