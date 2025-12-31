import time
from eimu import EIMU

port = '/dev/ttyACM0'
eimu = EIMU()

def main():
  r=0.0; p=0.0; y=0.0
  ax=0.0; ay=0.0; az=0.0
  gx=0.0; gy=0.0; gz=0.0

  eimu.connect(port)

  for i in range(4):
    time.sleep(1.0)
    print(i+1, " sec")

  # success = eimu.clearDataBuffer()

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
  sampleTime = 0.01

  while True:
    if time.time() - prevTime > sampleTime:
      success, valx, valy, valz = eimu.readRPY()
      if success:
        r=valx; p=valy; y=valz

      success, valx, valy, valz = eimu.readLinearAcc()
      if success:
        ax=valx; ay=valy; az=valz

      success, valx, valy, valz = eimu.readGyro()
      if success:
        gx=valx; gy=valy; gz=valz

      print(f"r: {r}\tp: {p}\ty: {y}")
      print(f"ax: {ax}\tay: {ay}\taz: {az}")
      print(f"gx: {gx}\tgy: {gy}\tgz: {gz}")
      print()
      prevTime = time.time()

if __name__ == "__main__":
  main()
  