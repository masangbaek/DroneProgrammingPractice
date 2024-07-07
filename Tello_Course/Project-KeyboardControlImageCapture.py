from djitellopy import tello
import KeyPressModule as kp
import time
import cv2 # image처리를 위한 cv2
kp.init()

sang = tello.Tello()
sang.connect()
print(sang.get_battery())
global img

sang.streamon() # image

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"): ud = speed
    elif kp.getKey("s"): ud = -speed

    if kp.getKey("a"): yv = speed
    elif kp.getKey("d"): yv = -speed

    if kp.getKey("q"):
        sang.land()
        time.sleep(5)
    if kp.getKey("e"):
        sang.takeoff()
        time.sleep(5)

    if kp.getKey("z"):
        cv2.imwrite(f"Resources/Images/{time.time()}.jpg", img)
        time.sleep(0.3)

    return [lr, fb, ud, yv]


while True:
    vals = getKeyboardInput()
    sang.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    # imageCapture 에서 가져온 부분
    img = sang.get_frame_read().frame
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # RGB 구현성공
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    # sleep(0.05) cv2.waitkey(1)랑 동일한 역할