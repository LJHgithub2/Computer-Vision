import cv2
face_detector = cv2.CascadeClassifier('C:\\code\\temp\\haarcascade_frontalface_default.xml')
# cv2.Videocapture은 현재 컴퓨터에서 사용될 수 있는 카매라를 불러오는것이다
# 일반적으로 0은 웹캠이다.
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame (ret = 반환 성공여부, frame(numpy배열 형태인 이미지))
    ret, frame = video_capture.read()

    image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    detections = face_detector.detectMultiScale(image_gray, minSize=(100,100))

    # Draw a rectangle around the faces
    for (x, y, w, h) in detections:
        print(w, h)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()