import cv2
cap = cv2.VideoCapture('output.avi')

while True:
    ret, frame = cap.read()
    cv2.imshow('video_feed', frame)
    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break

out.release()
cv2.destroyAllWindows()
