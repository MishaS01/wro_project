import cv2
cap = cv2.VideoCapture(0)

def show_image(filename, img):
    cv2.imshow(filename, img)

# green color
green_hsv_min = (30,50,50)
green_hsv_max = (60,255,255)

# red
red_hsv_min1 = (0,100,0)
red_hsv_max1 = (10,255,255)

red_hsv_min2 = (170,100,0)
red_hsv_max2 = (170,255,255)

color = 'red'


while True:
    ret, frame = cap.read()

    #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    if (color == 'green'):
    	thresh = cv2.inRange(hsv, green_hsv_min, green_hsv_max)
    elif (color == 'red'):
        thresh1 = cv2.inRange(hsv, red_hsv_min1, red_hsv_max1)
        thresh2 = cv2.inRange(hsv, red_hsv_min2, red_hsv_max2)
        thresh=thresh1+thresh2

    # filtering
    erode_img = cv2.erode(thresh, (31,31), iterations=1)
    dilate_img = cv2.dilate(erode_img, (31,31), iterations=1)

    contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours, -1, (0,0,255), 3, cv2.LINE_AA, hierarchy, 1)
    for cnt in contours:
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        x, y, w, h = cv2.boundingRect(cnt)

    show_image('green', thresh)
    cv2.imshow('video_feed', erode_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


out.release()
cv2.destroyAllWindows()
