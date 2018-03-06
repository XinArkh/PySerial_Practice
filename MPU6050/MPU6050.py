import serial
import time
import os

print("正在打开串口...")
ser = serial.Serial('COM3', 9600, timeout=1)
if not ser.is_open:
    ser.open()
time.sleep(2) # 等待串口开启完毕
print("串口成功开启！")
print("正在初始化MPU6050模块...")
ser.write(b'y') # 输入启动传感器模块的信号
time.sleep(5)  # 等待MPU6050模块初始校核结束
print("模块初始化完毕！")
# 清空缓存区数据
ser.flushInput()
ser.flushOutput()

# os.remove('步态数据.txt')
print("读取数据...")
while True:
    f = open('步态数据.txt', 'a')
    line = ser.readline().decode()
    ser.flush()
    f.write(line)
    f.close()
    print(line)
    time.sleep(0.005)