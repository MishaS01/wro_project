import cv2
cap = cv2.VideoCapture(0)

def show_image(filename, img):
    cv2.imshow(filename, img)

green_hsv_min = (30,50,0)
green_hsv_max = (60,255,255)

color = 'green'


while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    if (color == 'green'):
    	thresh = cv2.inRange(hsv, green_hsv_min, green_hsv_max)
    contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours, -1, (255,255,0), 3, cv2.LINE_AA, hierarchy, 1)
    for cnt in contours:
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        x, y, w, h = cv2.boundingRect(cnt)

    show_image('green', thresh)
    cv2.imshow('video_feed', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


out.release()
cv2.destroyAllWindows()
