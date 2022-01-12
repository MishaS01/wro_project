import cv2
def print_image_shape(img):
	print("Height:", img.shape[0])
	print("Width:", img.shape[1])
	print("Channels:", img.shape[2])

def resize_img(img, new_width):
	r = float(new_width)/ img.shape[1]
	dim = (new_width, int(new_width * r))

	resize = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	return resize

def show_image(filename, img):
    cv2.imshow(filename, img)

img = cv2.imread('blocks.png')
show_image('original_ima', img)

def cut_image(img):
	cropped = img[10:500, 500:2000]
	return cropped


def load_and_show_image():
	img = cv2.imread('anton1', cv2.IMREAD_COLOR)
	#cv2.imshow('privet', img)
	#cv2.waitKey(0)
	#cv2.imwrite('antonl_gratscale.jpg', img)
	return img

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#green
green_hsv_min = (50,0,0)
green_hsv_max = (60,255,255)

#red
red_hsv_min1 = (0,100,0)
red_hsv_max1 = (10,255,255)

red_hsv_min2 = (170,100,0)
red_hsv_max2 = (170,255,255)

#apply Threshold


color = 'red'
if (color == 'green'):
	thresh = cv2.inRange(hsv, green_hsv_min, green_hsv_max)
	show_image('green', thresh)
if (color == 'red'):
	thresh2 = cv2.inRange(hsv, red_hsv_min1, red_hsv_max1)
	thresh1 = cv2.inRange(hsv, red_hsv_min2, red_hsv_max2)
	thresh = thresh1 + thresh2
	show_image('red1', thresh1)
	show_image('red2', thresh2)
	show_image('red', thresh)

#img = load_and_show_image()

#print_image_shape(img)

#resized = resize_img(img,200)
#cv2.imshow('privet', resized)
#cropped = cut_image(img)
#cv2.imshow('cropped', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
