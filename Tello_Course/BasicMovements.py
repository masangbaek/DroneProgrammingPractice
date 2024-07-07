from djitellopy import tello
from time import sleep

sang = tello.Tello() # 객체생성
sang.connect()
print(sang.get_battery())

sang.takeoff()
sang.send_rc_control(0, 5,0, 0)
sleep(2)
sang.send_rc_control(5, 0,0, 0)
sleep(2)
sang.send_rc_control(0, 0,5, 0)
sleep(2)
sang.send_rc_control(0, 0,0,0)
sang.land()