import time
from eimu import EIMU

port = '/dev/ttyACM0'
eimu = EIMU(port)

def main():
  for i in range(4):
    time.sleep(1.0)
    print(i+1, " sec")

  success = eimu.clearDataBuffer()

  # change the reference frame to ENU frame (0 - NWU,  1 - ENU,  2 - NED)
  success = eimu.setWorldFrameId(1)

  # check the reference frame the eimu is working in (0 - NWU,  1 - ENU,  2 - NED)
  ref_frame_id = eimu.getWorldFrameId()

  if ref_frame_id == 0:
    print("Reference Frame is North-West-Up (NWU)")
  elif ref_frame_id == 1:
    print("Reference Frame is East-North-Up (ENU)")
  elif ref_frame_id == 2:
    print("Reference Frame is North-East-Down (NED)")

  prevTime = time.time()
  sampleTime = 0.01

  while True:
    if time.time() - prevTime > sampleTime:
      # try:
      r, p, y, ax, ay, az, gx, gy, gz = eimu.readImuData()

      print(f"r: {r}\tp: {p}\ty: {y}")
      print(f"ax: {ax}\tay: {ay}\taz: {az}")
      print(f"gx: {gx}\tgy: {gy}\tgz: {gz}")
      print()
      # except:
      #   pass
      
      prevTime = time.time()

if __name__ == "__main__":
  main()
  