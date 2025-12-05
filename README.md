
## Easy IMU Python Library
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
>  ```git clone https://github.com/samuko-things-company/eimu_python.git```

- Ensure you have the **Easy IMU Module** is already calibrated.

- Connect the **Easy IMU Module** to your PC or microcomputer

- A simple way to get started is simply to try out and follow the example `read_rpy.py` code.

- You can copy the **`eimu.py`** file into your python robotics project, import the library as shown in the example **`read_rpy.py`** code, add it to your code, and start using it.

## Basic Library functions and usage

- connect to sic_driver shield module
  > EIMU("port_name or port_path")

- clear IMU data buffer (ret True or False)
  > clearDataBuffer

- get all imu readings - roll, pitch, yaw, ax, ay, az, gx, gy, gz
  > readImuData()

- get quaternions qw, qx, qy, qz
  > readQuat()

- get reference frame 
  > getWorldFrameId()  #(0 - NWU,  1 - ENU,  2 - NED)

- change reference frame (ret True or False)
  > setWorldFrameId(frame_id) #(0 - NWU,  1 - ENU,  2 - NED)

- get the madgwick filter gain
  > getFilterGain()

- get rpy variances- get Roll, Pitch and Yaw variance value
  > readRPYVariance()

- get gyro rate variances - gx, gy, gz
  > readGyroVariance()

- get acceleration variances - ax, ay, az
  > readAccVariance()