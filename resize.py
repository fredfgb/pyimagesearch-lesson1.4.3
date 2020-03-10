# import the necessary packages
import argparse
import imutils
import cv2
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
 
# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
 
# # we need to keep in mind aspect ratio so the image does not look skewed
# # or distorted -- therefore, we calculate the ratio of the new image to
# # the old image. Let's make our new image have a width of 150 pixels
# r = 150.0 / image.shape[1]
# dim = (150, int(image.shape[0] * r))
 
# # perform the actual resizing of the image
# resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
# cv2.imshow("Resized (Width)", resized)

# # what if we wanted to adjust the height of the image? We can apply
# # the same concept, again keeping in mind the aspect ratio, but instead
# # calculating the ratio based on height -- let's make the height of the
# # resized image 50 pixels
# r = 50.0 / image.shape[0]
# dim = (int(image.shape[1] * r), 50)
 
# # perform the resizing
# resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
# cv2.imshow("Resized (Height)", resized)

# # of course, calculating the ratio each and every time we want to resize
# # an image is a real pain -- let's create a  function where we can specify
# # our target width or height, and have it take care of the rest for us.
# resized = imutils.resize(image, width=100)
# cv2.imshow("Resized via Function (width)", resized)

# resized = imutils.resize(image, height=50)
# cv2.imshow("Resized via Function (height)", resized)

# # construct the list of interpolation methods
# methods = [
# 	("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
# 	("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
# 	("cv2.INTER_AREA", cv2.INTER_AREA),
# 	("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
# 	("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)]
 
# # loop over the interpolation methods
# for (name, method) in methods:
# 	# increase the size of the image by 3x using the current interpolation
# 	# method
# 	resized = imutils.resize(image, width=image.shape[1] * 3, inter=method)
# 	cv2.imshow("Method: {}".format(name), resized)	

# 2. Question
# Download the source code to this lesson and use the florida_trip_small.png small image to answer the following question.
# Resize the image to have a width of 100px using the cv2.INTER_NEAREST interpolation method. What is (approximately) the pixel value located at x=20, y=74?  
resized = imutils.resize(image, width=100, inter=cv2.INTER_NEAREST)
cv2.imshow("2. Question", resized)
(b, g, r) = resized[74, 20]
print("Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))

# 3. Question
# Now, use the same image to make the image twice it’s original size using cv2.INTER_CUBIC interpolation.
# What is the value of the pixel located at x=170, y=367 in our resized image?
resized = imutils.resize(image, width=image.shape[1] * 2, height=image.shape[0] * 2, inter=cv2.INTER_CUBIC)
cv2.imshow("3. Question", resized)
(b, g, r) = resized[367, 170]
print("Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))

cv2.waitKey(0)