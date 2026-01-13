import time
from eimu import EIMU

port = '/dev/ttyACM0'
eimu = EIMU()

def main():
  # 50Hz comm setup
  serial_port = '/dev/ttyACM0'
  serial_baudrate = 115200
  serial_timeout = 0.018 #value < 0.02 (for 50Hz comm)

  eimu.connect(serial_port, serial_baudrate, serial_timeout)

  for i in range(4):
    time.sleep(1.0)
    print(i+1, " sec")

  success = eimu.clearDataBuffer()

  # change the reference frame to ENU frame (0 - NWU,  1 - ENU,  2 - NED)
  eimu.setWorldFrameId(1)

  # check the reference frame the eimu is working in (0 - NWU,  1 - ENU,  2 - NED)
  success, ref_frame_id = eimu.getWorldFrameId()
  if success:
    if ref_frame_id == 0:
      print("Reference Frame is North-West-Up (NWU)")
    elif ref_frame_id == 1:
      print("Reference Frame is East-North-Up (ENU)")
    elif ref_frame_id == 2:
      print("Reference Frame is North-East-Down (NED)")
  else:
    print("Could not get world frame ID")

  prevTime = time.time()
  sampleTime = 0.02

  while True:
    if time.time() - prevTime > sampleTime:
      success, r, p, y, ax, ay, az, gx, gy, gz = eimu.readImuData()

      if success:
        print(f"r: {r}\tp: {p}\ty: {y}")
        print(f"ax: {ax}\tay: {ay}\taz: {az}")
        print(f"gx: {gx}\tgy: {gy}\tgz: {gz}")
        print()
      else:
        print("Error reading IMU data")
      prevTime = time.time()

if __name__ == "__main__":
  main()
  