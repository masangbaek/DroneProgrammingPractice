from djitellopy import tello
import cv2

sang = tello.Tello()
sang.connect()
print(sang.get_battery())

sang.streamon()

while True:
    img = sang.get_frame_read().frame
    img = cv2.cvtColor(img, cv2. COLOR_BGR2RGB) # RGB 구현성공    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)