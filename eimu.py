import serial
import struct

class EIMUSerialError(Exception):
    """Custom exception for for EIMU Comm failure"""
    pass

START_BYTE = 0xBB
READ_QUAT = 0x01
READ_RPY = 0x02
READ_RPY_VAR = 0x03
READ_ACC = 0x05
READ_ACC_VAR = 0x09
READ_GYRO = 0x0B
READ_GYRO_VAR = 0x0F
READ_MAG = 0x11
SET_FILTER_GAIN = 0x1D
GET_FILTER_GAIN = 0x1E
SET_FRAME_ID = 0x1F
GET_FRAME_ID = 0x20
READ_QUAT_RPY = 0x22
READ_ACC_GYRO = 0x23
CLEAR_DATA_BUFFER = 0x27
READ_IMU_DATA = 0x28
READ_LIN_ACC_RAW = 0x2B
READ_LIN_ACC = 0x2C



class EIMU:
    def __init__(self):
        pass

    def connect(self, port, baud=115200, timeOut=0.1):
        self.ser = serial.Serial(port, baud, timeout=timeOut)

    def disconnect(self):
        if self.ser.is_open:
            self.ser.close()
    
    #------------------------------------------------------------------------
    def send_packet_without_payload(self, cmd):
        length = 0
        packet = bytearray([START_BYTE, cmd, length])
        checksum = sum(packet) & 0xFF
        packet.append(checksum)
        self.ser.write(packet)
        self.ser.flush()

    def send_packet_with_payload(self, cmd, payload_bytes):
        length = len(payload_bytes)
        packet = bytearray([START_BYTE, cmd, length]) + payload_bytes
        checksum = sum(packet) & 0xFF
        packet.append(checksum)
        self.ser.write(packet)
        self.ser.flush()

    def read_packet1(self):
        """
        Reads 4 bytes from the serial port and converts to a float (little-endian).
        Returns (success, value-array)
        """
        try:
            payload = self.ser.read(4)
            if len(payload) != 4:
                # print("[EPMC SERIAL ERROR]: Timeout while reading 1 values")
                return False, 0.0

            # Unpack 4 bytes as little-endian float
            (val,) = struct.unpack('<f', payload)
            return True, val
        except:
            # print("[PYSERIAL ERROR]: Read Timeout")
            return False, 0.0
        
    def read_packet3(self):
        """
        Reads 12 bytes from the serial port and converts to a float (little-endian).
        Returns (success, value-array)
        """
        try:
            payload = self.ser.read(12)
            if len(payload) != 12:
                # print("[EPMC SERIAL ERROR]: Timeout while reading 3 values")
                return False, 0.0, 0.0, 0.0

            # Unpack 4 bytes as little-endian float
            a, b, c = struct.unpack('<fff', payload)
            return True, a, b, c
        except:
            # print("[PYSERIAL ERROR]: Read Timeout")
            return False, 0.0, 0.0, 0.0
    
    def read_packet4(self):
        """
        Reads 16 bytes from the serial port and converts to a float (little-endian).
        Returns (success, value-array)
        """
        try:
            payload = self.ser.read(16)
            if len(payload) != 16:
                # print("[EPMC SERIAL ERROR]: Timeout while reading 4 values")
                return False, 0.0, 0.0, 0.0, 0.0

            # Unpack 4 bytes as little-endian float
            a, b, c, d = struct.unpack('<ffff', payload)
            return True, a, b, c, d
        except:
            # print("[PYSERIAL ERROR]: Read Timeout")
            return False, 0.0, 0.0, 0.0, 0.0
        
    def read_packet6(self):
        """
        Reads 24 bytes from the serial port and converts to a float (little-endian).
        Returns (success, value-array)
        """
        try:
            payload = self.ser.read(24)
            if len(payload) != 24:
                # print("[EPMC SERIAL ERROR]: Timeout while reading 6 values")
                return False, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

            # Unpack 4 bytes as little-endian float
            a, b, c, d, e, f = struct.unpack('<ffffff', payload)
            return True, a, b, c, d, e, f
        except:
            # print("[PYSERIAL ERROR]: Read Timeout")
            return False, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
        
    def read_packet9(self):
        """
        Reads 36 bytes from the serial port and converts to a float (little-endian).
        Returns (success, value-array)
        """
        try:
            payload = self.ser.read(36)
            if len(payload) != 36:
                # print("[EPMC SERIAL ERROR]: Timeout while reading 9 values")
                return False, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

            # Unpack 4 bytes as little-endian float
            a, b, c, d, e, f, g, h, i = struct.unpack('<fffffffff', payload)
            return True, a, b, c, d, e, f, g, h, i
        except:
            # print("[PYSERIAL ERROR]: Read Timeout")
            return False, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    
    #---------------------------------------------------------------------

    def write_data1(self, cmd, val, pos=100):
        payload = struct.pack('<Bf', pos, val)
        self.send_packet_with_payload(cmd, payload)

    def read_data1(self, cmd, pos=100):
        payload = struct.pack('<Bf', pos, 0.0)  # big-endian
        self.send_packet_with_payload(cmd, payload)
        success, val = self.read_packet1()
        return success, val
    
    def write_data3(self, cmd, a, b, c):
        payload = struct.pack('<fff', a, b, c) 
        self.send_packet_with_payload(cmd, payload)

    def read_data3(self, cmd):
        self.send_packet_without_payload(cmd)
        success, a, b, c = self.read_packet3()
        return success, a, b, c

    def read_data4(self, cmd):
        self.send_packet_without_payload(cmd)
        suceess, a, b, c, d = self.read_packet4()
        return suceess, a, b, c, d
    
    def read_data6(self, cmd):
        self.send_packet_without_payload(cmd)
        success, a, b, c, d, e, f = self.read_packet6()
        return success, a, b, c, d, e, f
    
    def read_data9(self, cmd):
        self.send_packet_without_payload(cmd)
        success, a, b, c, d, e, f, g, h, i = self.read_packet9()
        return success, a, b, c, d, e, f, g, h, i
    
    #---------------------------------------------------------------------
        
    def clearDataBuffer(self):
        success, _ = self.read_data1(CLEAR_DATA_BUFFER)
        return success
    
    def setWorldFrameId(self, frame_id):
        self.write_data1(SET_FRAME_ID, frame_id)
    
    def getWorldFrameId(self):
        success, frame_id = self.read_data1(GET_FRAME_ID)
        return success, int(frame_id)
    
    def setFilterGain(self, gain):
        self.write_data1(SET_FILTER_GAIN, gain)

    def getFilterGain(self):
        success, gain = self.read_data1(GET_FILTER_GAIN)
        return success, round(gain, 3)
    
    def readQuat(self):
        success, qw, qx, qy, qz = self.read_data4(READ_QUAT)
        return success, round(qw, 6), round(qx, 6), round(qy, 6), round(qz, 6)
    
    def readRPY(self):
        success, r, p, y = self.read_data3(READ_RPY)
        return success, round(r, 6), round(p, 6), round(y, 6)
    
    def readRPYVariance(self):
        success, r, p, y = self.read_data3(READ_RPY_VAR)
        return success, round(r, 6), round(p, 6), round(y, 6)
    
    # def readAcc(self):
    #     success, ax, ay, az = self.read_data3(READ_ACC)
    #     return success, round(ax, 6), round(ay, 6), round(az, 6)
    
    def readAccVariance(self):
        success, ax, ay, az = self.read_data3(READ_ACC_VAR)
        return success, round(ax, 6), round(ay, 6), round(az, 6)
    
    def readGyro(self):
        success, gx, gy, gz = self.read_data3(READ_GYRO)
        return success, round(gx, 6), round(gy, 6), round(gz, 6)
    
    def readGyroVariance(self):
        success, gx, gy, gz = self.read_data3(READ_GYRO_VAR)
        return success, round(gx, 6), round(gy, 6), round(gz, 6)
    
    # def readMag(self):
    #     success, mx, my, mz = self.read_data3(READ_MAG)
    #     return success, round(mx, 6), round(my, 6), round(mz, 6)
    
    def readAccGyro(self):
        success, ax, ay, az, gx, gy, gz = self.read_data6(READ_ACC_GYRO)
        return success, round(ax, 6), round(ay, 6), round(az, 6), round(gx, 6), round(gy, 6), round(gz, 6)
    
    def readImuData(self):
        success, r, p, y, ax, ay, az, gx, gy, gz = self.read_data9(READ_IMU_DATA)
        return success, round(r, 6), round(p, 6), round(y, 6), round(ax, 6), round(ay, 6), round(az, 6), round(gx, 6), round(gy, 6), round(gz, 6)

    def readLinearAccRaw(self):
        success, ax, ay, az = self.read_data3(READ_LIN_ACC_RAW)
        return success, round(ax, 6), round(ay, 6), round(az, 6)
    
    def readLinearAcc(self):
        success, ax, ay, az = self.read_data3(READ_LIN_ACC)
        return success, round(ax, 6), round(ay, 6), round(az, 6)
    #---------------------------------------------------------------------