
import serial
import time


class EIMU:
  
  def __init__(self, port, baud=115200, timeOut=0.1):
    self.ser = serial.Serial(port, baud, timeout=timeOut)

  def send_msg(self, msg_to_send):
    data = ""
    prev_time = time.time()
    while data=="":
      try:
        self.ser.write(msg_to_send.encode())   # send a single or multiple byte    
        data = self.ser.readline().decode().strip()
        if time.time()-prev_time > 2.0:
          raise Exception("Error getting response from arduino nano, wasted much time \n")
      except:
        raise Exception("Error getting response from arduino nano, wasted much time \n")
    return data

  
  def send(self, cmd_route, val1=0, val2=0, val3=0):
    cmd_str = cmd_route+","+str(val1)+","+str(val2)+","+str(val3)
    data = self.send_msg(cmd_str)
    if data == "1":
      return True
    else:
      return False
  
  
  def get(self, cmd_route):
    data = self.send_msg(cmd_route).split(',')
    # return float(data[0]), float(data[1]), float(data[2])
    if len(data)==1:
      return float(data[0])
    elif len(data)==2:
      return float(data[0]), float(data[1])
    elif len(data)==3:
      return float(data[0]), float(data[1]), float(data[2])
    elif len(data)==4:
      return float(data[0]), float(data[1]), float(data[2]), float(data[3])
    
    
  def getRPY(self):
    roll, pitch, yaw = self.get("/rpy")
    return roll, pitch, yaw
  
  def getQuat(self):
    qw, qx, qy, qz = self.get("/quat")
    return qw, qx, qy, qz
  
  def getGyro(self):
    gx, gy, gz = self.get("/gyro-cal")
    return gx, gy, gz
  
  def getAcc(self):
    ax, ay, az = self.get("/acc-cal")
    return ax, ay, az

  def getRPYvariance(self):
    r, p, y = self.get("/rpy-var")
    return r, p, y
  
  def getGyroVariance(self):
    gx, gy, gz = self.get("/gyro-var")
    return gx, gy, gz
  
  def getAccVariance(self):
    ax, ay, az = self.get("/acc-var")
    return ax, ay, az
  
  def getGain(self):
    gain = self.get("/gain")
    return gain
  
  def getRefFrame(self):
    frame_id = int(self.get("/frame-id"))
    if frame_id == 0:
      return "NWU"
    elif frame_id == 1:
      return "ENU"
    elif frame_id == 2:
      return "NED"