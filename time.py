import time



import cv2
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if (ret == True):
        start_time = time.process_time()
        cv2.imshow('video_feed', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): #ожидает нажатие кномпки
            break #закрывает программу
        print(1 / (time.process_time() - start_time), 'FPS')



cap.release()
cv2.destroyAllWindows()

#print(time.process_time() - start_time)
