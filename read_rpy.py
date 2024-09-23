from eimu import EIMU 
import time


imu = EIMU('/dev/ttyUSB0')

def main():
  for i in range(6):
    time.sleep(1.0)
    print(i+1, " sec")

  # change the reference frame to ENU frame (0 - NWU,  1 - ENU,  2 - NED)
  imu.setRefFrame(1)

  # check the reference frame the IMU is working in (0 - NWU,  1 - ENU,  2 - NED)
  ref_frame_id = imu.getRefFrame()

  if ref_frame_id == 0:
    print("Reference Frame is North-West-Up (NWU)")
  elif ref_frame_id == 1:
    print("Reference Frame is East-North-Up (ENU)")
  elif ref_frame_id == 2:
    print("Reference Frame is North-East-Down (NED)")

  for i in range(4):
    time.sleep(1.0)
    print(i+1, " sec")

  prevTime = time.time()
  sampleTime = 0.05

  while True:
    if time.time() - prevTime > sampleTime:
      try:
        roll, pitch, yaw = imu.getRPY()
        print(f"roll: {roll}\npitch: {pitch}\nyaw: {yaw}\n")
      except:
        pass
      
      prevTime = time.time()

if __name__ == "__main__":
  main()