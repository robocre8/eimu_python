from eimu import EIMU 
import time


imu = EIMU('/dev/ttyUSB0')


for i in range(10):
  time.sleep(1.0)
  print(i+1, " sec")

prevTime = time.time()
sampleTime = 0.05
while True:

  if time.time() - prevTime > sampleTime:
    try:
      roll, pitch, yaw = imu.getRPY()

      print(f"roll: {roll}, pitch: {pitch}, yaw: {yaw}")
      print("")
    except:
      pass
    
    prevTime = time.time()

