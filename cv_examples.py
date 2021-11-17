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


def load_and_show_image():
	img = cv2.imread('anton1.jpg', cv2.IMREAD_COLOR)
	#cv2.imshow('privet', img)
	#cv2.waitKey(0)
	#cv2.imwrite('antonl_gratscale.jpg', img)
	return img


img = load_and_show_image()

print_image_shape(img)

resized = resize_img(img,200)
cv2.imshow('privet', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
