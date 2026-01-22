
## Easy IMU Python Serial Client Library
This library helps communicate with the already setup **`Easy IMU Module`** in your PC or microcomputer-based python projects, with the [eimu_setup_application](https://github.com/samuko-things-company/eimu_setup_application).

> you can use it in your microcomputer robotics project (e.g Raspberry Pi, PC, etc.)

A simple way to get started is simply to try out and follow the example code


## Dependencies
- you'll need to pip install the pyserial library
  ```shell
    pip3 install pyserial   //linux or mac
    pip install pyserial   //windows
  ```

## How to Use the Library
- Download (by clicking on the green Code button above) or clone the repo into your PC using **`git clone`**
> [!NOTE]  
> you can use this command if you want to clone the repo:
> 
>  ```git clone https://github.com/robocre8/eimu_serial_py.git```

- Ensure you have the **Easy IMU Module** is already calibrated.

- Connect the **Easy IMU Module** to your PC or microcomputer

- A simple way to get started is simply to try out and follow the example `read_rpy.py` code.

- You can copy the **`eimu_serial.py`** file into your python robotics project, import the library as shown in the example **`read_imu.py`** code, add it to your code, and start using it.


## Basic Library functions and usage

- connect to EIMU module
  > imu = EIMUSerialClient()
  >
  > imu.connect("port_name or port_path")

- clear imu, filter, e.t.c data buffer on the EIMU module
  > imu.clearDataBuffer() # returns bool -> success

- set imu reference frame -> NWU (0), ENU (1), NED (2) 
  > imu.setWorldFrameId(frame_id)

- get imu reference frame -> NWU (0), ENU (1), NED (2) 
  > imu.getWorldFrameId() # returns tuple -> (success, frame_id): bool, int

- adjust filter gain
  > imu.setFilterGain(gain)

- read filter gain
  > imu.getFilterGain() # returns tuple -> (success, gain): bool, float

- read all IMU data (orientation - RPY, linear acceleration, angular velocity)
  > imu.readImuData() # returns tuple -> (success, r, p, y, ax, ay, az, gx, gy, gz): bool, float, float, float, float, float, float, float, float, float

- read Oreintation - Quaterninos
  > imu.readQuat() # returns tuple -> (success, qw, qx, qy, qz): bool, float, float, float, float

- read Oreintation - RPY
  > imu.readRPY() # returns tuple -> (success, r, p, y): bool, float, float, float

- read Linear Acceleration
  > imu.readLinearAcc() # returns tuple -> (success, ax, ay, az): bool, float, float, float

- read Gyro (Angular velocity)
  > imu.readGyro() # returns tuple -> (success, gx, gy, gz): bool, float, float, float