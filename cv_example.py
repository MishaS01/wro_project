import cv2
cap = cv2.VideoCapture(0)
out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*"MJPG"), 20.0, (640,480))

while True:

  ret, frame = cap.read()

  if (ret ==True):

    ret, frame = cap.read()
    cv2.imshow('video_feed', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  else:
     break


cap.release()
out.release()

cv2.destroyAllWindows()
