import serial
import struct

START_BYTE = 0xBB
READ_QUAT = 0x01
READ_RPY = 0x02
READ_RPY_VAR = 0x03
READ_ACC = 0x05
READ_ACC_VAR = 0x09
READ_GYRO = 0x0B
READ_GYRO_VAR = 0x0F
READ_MAG = 0x11
GET_FILTER_GAIN = 0x1E
SET_FRAME_ID = 0x1F
GET_FRAME_ID = 0x20
READ_QUAT_RPY = 0x22
READ_ACC_GYRO = 0x23
CLEAR_DATA_BUFFER = 0x27
READ_IMU_DATA = 0x28



class EIMU:
    def __init__(self, port, baud=115200, timeOut=0.1):
        self.ser = serial.Serial(port, baud, timeout=timeOut)
    
    #------------------------------------------------------------------------
    def send_packet_without_payload(self, cmd):
        length = 0
        packet = bytearray([START_BYTE, cmd, length])
        checksum = sum(packet) & 0xFF
        packet.append(checksum)
        self.ser.write(packet)

    def send_packet_with_payload(self, cmd, payload_bytes):
        length = len(payload_bytes)
        packet = bytearray([START_BYTE, cmd, length]) + payload_bytes
        checksum = sum(packet) & 0xFF
        packet.append(checksum)
        self.ser.write(packet)

    def read_packet1(self):
        """
        Reads 4 bytes from the serial port and converts to a float (little-endian).
        Returns (success, value-array)
        """

        try:
            payload = self.ser.read(4)
            if len(payload) != 4:
                print("[EPMC SERIAL COMM]: Timeout while reading 4 bytes")
                return False, [0.0]

            # Unpack 4 bytes as little-endian float
            (val,) = struct.unpack('<f', payload)
            return True, [val]

        except serial.SerialException as e:
            print(f"[EPMC SERIAL COMM]: Serial error — {e}")
            return False, [0.0]
        
    def read_packet2(self):
        """
        Reads 8 bytes from the serial port and converts to a float (little-endian).
        Returns (success, value-array)
        """
        try:
            payload = self.ser.read(8)
            if len(payload) != 8:
                print("[EPMC SERIAL COMM]: Timeout while reading 8 bytes")
                return False, [0.0, 0.0]

            # Unpack 4 bytes as little-endian float
            a, b = struct.unpack('<ff', payload)
            return True, [a, b]

        except serial.SerialException as e:
            print(f"[EPMC SERIAL COMM]: Serial error — {e}")
            return False, [0.0, 0.0]
        
    def read_packet3(self):
        """
        Reads 12 bytes from the serial port and converts to a float (little-endian).
        Returns (success, value-array)
        """
        try:
            payload = self.ser.read(12)
            if len(payload) != 12:
                print("[EPMC SERIAL COMM]: Timeout while reading 12 bytes")
                return False, [0.0, 0.0, 0.0]

            # Unpack 4 bytes as little-endian float
            a, b, c = struct.unpack('<fff', payload)
            return True, [a, b, c]

        except serial.SerialException as e:
            print(f"[EPMC SERIAL COMM]: Serial error — {e}")
            return False, [0.0, 0.0, 0.0]
    
    def read_packet4(self):
        """
        Reads 16 bytes from the serial port and converts to a float (little-endian).
        Returns (success, value-array)
        """
        try:
            payload = self.ser.read(16)
            if len(payload) != 16:
                print("[EPMC SERIAL COMM]: Timeout while reading 16 bytes")
                return False, [0.0, 0.0, 0.0, 0.0]

            # Unpack 4 bytes as little-endian float
            a, b, c, d = struct.unpack('<ffff', payload)
            return True, [a, b, c, d]

        except serial.SerialException as e:
            print(f"[EPMC SERIAL COMM]: Serial error — {e}")
            return False, [0.0, 0.0, 0.0, 0.0]
    
    def read_packet6(self):
        """
        Reads 24 bytes from the serial port and converts to a float (little-endian).
        Returns (success, value-array)
        """
        try:
            payload = self.ser.read(24)
            if len(payload) != 24:
                print("[EPMC SERIAL COMM]: Timeout while reading 24 bytes")
                return False, [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

            # Unpack 4 bytes as little-endian float
            a, b, c, d, e, f = struct.unpack('<ffffff', payload)
            return True, [a, b, c, d, e, f]

        except serial.SerialException as e:
            print(f"[EPMC SERIAL COMM]: Serial error — {e}")
            return False, [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    
    def read_packet8(self):
        """
        Reads 32 bytes from the serial port and converts to a float (little-endian).
        Returns (success, value-array)
        """
        try:
            payload = self.ser.read(32)
            if len(payload) != 32:
                print("[EPMC SERIAL COMM]: Timeout while reading 32 bytes")
                return False, [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

            # Unpack 4 bytes as little-endian float
            a, b, c, d, e, f, g, h = struct.unpack('<ffffffff', payload)
            return True, [a, b, c, d, e, f, g, h]

        except serial.SerialException as e:
            print(f"[EPMC SERIAL COMM]: Serial error — {e}")
            return False, [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        
    def read_packet9(self):
        """
        Reads 36 bytes from the serial port and converts to a float (little-endian).
        Returns (success, value-array)
        """
        try:
            payload = self.ser.read(36)
            if len(payload) != 36:
                print("[EPMC SERIAL COMM]: Timeout while reading 36 bytes")
                return False, [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

            # Unpack 4 bytes as little-endian float
            a, b, c, d, e, f, g, h, i = struct.unpack('<fffffffff', payload)
            return True, [a, b, c, d, e, f, g, h, i]

        except serial.SerialException as e:
            print(f"[EPMC SERIAL COMM]: Serial error — {e}")
            return False, [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    
    #---------------------------------------------------------------------

    def write_data1(self, cmd, pos, val):
        payload = struct.pack('<Bf', pos, val)
        self.send_packet_with_payload(cmd, payload)
        success, val_arr = self.read_packet1()
        return success, val_arr[0]

    def read_data1(self, cmd, pos):
        payload = struct.pack('<Bf', pos, 0.0)  # big-endian
        self.send_packet_with_payload(cmd, payload)
        success, val_arr = self.read_packet1()
        return success, val_arr[0]
    
    def write_data2(self, cmd, a, b):
        payload = struct.pack('<ff', a,b) 
        self.send_packet_with_payload(cmd, payload)

    def read_data2(self, cmd):
        self.send_packet_without_payload(cmd)
        success, val_arr = self.read_packet2()
        return success, val_arr
    
    def write_data3(self, cmd, a, b, c):
        payload = struct.pack('<fff', a,b,c) 
        self.send_packet_with_payload(cmd, payload)

    def read_data3(self, cmd):
        self.send_packet_without_payload(cmd)
        success, val_arr = self.read_packet3()
        return success, val_arr

    def write_data4(self, cmd, a, b, c, d):
        payload = struct.pack('<ffff', a,b,c,d) 
        self.send_packet_with_payload(cmd, payload)

    def read_data4(self, cmd):
        self.send_packet_without_payload(cmd)
        success, val_arr = self.read_packet4()
        return success, val_arr
    
    def write_data6(self, cmd, a, b, c, d, e, f):
        payload = struct.pack('<ffffff', a,b,c,d,e,f) 
        self.send_packet_with_payload(cmd, payload)

    def read_data6(self, cmd):
        self.send_packet_without_payload(cmd)
        success, val_arr = self.read_packet6()
        return success, val_arr
        
    def write_data8(self, cmd, a, b, c, d, e, f, g, h):
        payload = struct.pack('<ffffffff', a,b,c,d,e,f,g,h) 
        self.send_packet_with_payload(cmd, payload)

    def read_data8(self, cmd):
        self.send_packet_without_payload(cmd)
        success, val_arr = self.read_packet8()
        return success, val_arr
    
    def read_data9(self, cmd):
        self.send_packet_without_payload(cmd)
        success, val_arr = self.read_packet9()
        return success, val_arr
    
    #---------------------------------------------------------------------
        
    def clearDataBuffer(self):
        success, res = self.write_data1(CLEAR_DATA_BUFFER, 100, 0.0)
        return success
    
    def setWorldFrameId(self, id):
        success, res = self.write_data1(SET_FRAME_ID, 100, id)
        return success
    
    def getWorldFrameId(self):
        success, id = self.read_data1(GET_FRAME_ID, 100)
        if success:
            return success, int(id)
        else:
            return success, 0
    
    def getFilterGain(self):
        success, gain = self.read_data1(GET_FILTER_GAIN, 100)
        if success:
            return success, round(gain, 3)
        else:
            return success, 0
    
    def readQuat(self):
        success, quat_arr = self.read_data4(READ_QUAT)
        return success, quat_arr
    
    def readRPY(self):
        success, rpy_arr = self.read_data3(READ_RPY)
        return success, rpy_arr
    
    def readRPYVariance(self):
        success, rpy_arr = self.read_data3(READ_RPY_VAR)
        return success, rpy_arr
    
    def readAcc(self):
        success, acc_arr = self.read_data3(READ_ACC)
        return success, acc_arr
    
    def readAccVariance(self):
        success, acc_arr = self.read_data3(READ_ACC_VAR)
        return success, acc_arr
    
    def readGyro(self):
        success, gyro_arr = self.read_data3(READ_GYRO)
        return success, gyro_arr
    
    def readGyroVariance(self):
        success, gyro_arr = self.read_data3(READ_GYRO_VAR)
        return success, gyro_arr
    
    def readMag(self):
        success, mag_arr = self.read_data3(READ_MAG)
        return success, mag_arr

    #---------------------------------------------------------------------

    def readQuatRPY(self):
        success, imu_data_arr = self.read_data8(READ_QUAT_RPY)
        return success, imu_data_arr
    
    def readAccGyro(self):
        success, imu_data_arr = self.read_data8(READ_ACC_GYRO)
        return success, imu_data_arr
    
    def readImuData(self):
        success, imu_data_arr = self.read_data9(READ_IMU_DATA)
        return success, imu_data_arr