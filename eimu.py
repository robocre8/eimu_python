import serial
import time

# Serial Protocol Command IDs -------------
READ_RPY = 10
READ_RPY_VAR = 11
WRITE_RPY_VAR = 12

READ_GYRO = 13
READ_GYRO_RAW = 14
READ_GYRO_OFF = 15
WRITE_GYRO_OFF = 16
READ_GYRO_VAR = 17
WRITE_GYRO_VAR = 18

READ_ACC = 19
READ_ACC_RAW = 20
READ_ACC_OFF = 21
WRITE_ACC_OFF = 22
READ_ACC_VAR = 23
WRITE_ACC_VAR = 24
READ_LIN_ACC_RAW = 25
READ_LIN_ACC = 26
SET_ACC_LPF_CUT_FREQ = 27
GET_ACC_LPF_CUT_FREQ = 28

READ_MAG = 29
READ_MAG_RAW = 30
READ_MAG_H_OFF = 31
WRITE_MAG_H_OFF = 32
READ_MAG_S_OFF0 = 33
WRITE_MAG_S_OFF0 = 34
READ_MAG_S_OFF1 = 35
WRITE_MAG_S_OFF1 = 36
READ_MAG_S_OFF2 = 37
WRITE_MAG_S_OFF2 = 38

SET_I2C_ADDR = 39
GET_I2C_ADDR = 40
SET_FILTER_GAIN = 41
GET_FILTER_GAIN = 42
SET_FRAME_ID = 43
GET_FRAME_ID = 44
RESET = 45
CLEAR = 46
#---------------------------------------------



class EIMU:
    def __init__(self):
        pass

    def connect(self, port, baud=115200, timeOut=0.1):
        self.ser = serial.Serial(port, baud, timeout=timeOut)
        time.sleep(0.1)
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
    
    def disconnect(self):
        if self.ser.is_open:
            self.ser.close()

    #------------------------------------------------------------------------
    def send(self, cmd, arg1=0.0, arg2=0.0, arg3=0.0):
        send_str = str(round(float(cmd),6))+" "+str(round(float(arg1),6))+" "+str(round(float(arg2),6))+" "+str(round(float(arg3),6))+"\r"
        self.ser.write(send_str.encode())

    def recv(self, cmd, arg1=0):
        try:
            self.send(cmd, arg1)
            data = self.ser.readline().decode().strip().split(' ')
            return True, round(float(data[0]),6), round(float(data[1]),6), round(float(data[2]),6)
        except:
            # self.ser.reset_input_buffer()
            # self.ser.reset_output_buffer()
            return False, 0.0, 0.0, 0.0
    
    #---------------------------------------------------------------------
        
    def clearDataBuffer(self):
        success, _, _, _ = self.recv(CLEAR)
        return success
    
    def setWorldFrameId(self, frame_id):
        self.send(SET_FRAME_ID, 0.0, frame_id)
    
    def getWorldFrameId(self):
        success, frame_id, _, _ = self.recv(GET_FRAME_ID)
        return success, int(frame_id)
    
    def setFilterGain(self, gain):
        self.send(SET_FILTER_GAIN, 0.0, gain)

    def getFilterGain(self):
        success, gain, _, _ = self.recv(GET_FILTER_GAIN)
        return success, round(gain, 3)
    
    def setAccFilterCF(self, cf):
        self.send(SET_ACC_LPF_CUT_FREQ, 0.0, cf)
    
    def getAccFilterCF(self):
        success, cf, _, _ = self.recv(GET_ACC_LPF_CUT_FREQ)
        return success, round(cf, 3)
    
    def readRPY(self):
        success, r, p, y = self.recv(READ_RPY)
        return success, r, p, y
    
    def readRPYVariance(self):
        success, r, p, y = self.recv(READ_RPY_VAR)
        return success, r, p, y
    
    def readLinearAcc(self):
        success, ax, ay, az = self.recv(READ_LIN_ACC)
        return success, ax, ay, az
    
    def readAccVariance(self):
        success, ax, ay, az = self.recv(READ_ACC_VAR)
        return success, ax, ay, az
    
    def readGyro(self):
        success, gx, gy, gz = self.recv(READ_GYRO)
        return success, gx, gy, gz
    
    def readGyroVariance(self):
        success, gx, gy, gz = self.recv(READ_GYRO_VAR)
        return success, gx, gy, gz
    
    #---------------------------------------------------------------------