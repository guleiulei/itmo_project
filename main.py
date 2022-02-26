import collections
import serial
from functions import calc_frequency, sum_bytes
from matplotlib import pyplot as plt
from serial_port import serial_port

i = 1
numbers = 0
maxsize = 15000
x1 = 0
x2 = 30
step_x = (x2 - x1) / maxsize # 0.00075


x = collections.deque([0]*maxsize, maxlen=maxsize)
y = collections.deque([0]*maxsize, maxlen=maxsize) # список со хначениям частоты

serial_port = serial_port()
with serial.Serial(serial_port, baudrate=115200) as ser:
    while 1:
        ser.read_until(expected=b'\xff')
        data = ser.read(120) # 5000 байтов
        if sum_bytes(data):
            data = calc_frequency(data.hex()[2:10])
            y.append(data)
            x.append(numbers)
            i += 1
            numbers += 1
            plt.ion()
            more_bytes = ser.inWaiting()
            print(more_bytes)
            if i > 15:
                plt.clf()
                plt.xlabel('Количество отсчетов')
                plt.ylabel('Частота, Мгц')
                plt.xlim(0, 15000)
                plt.ylim(480.7, 481.8)
                plt.plot(x, y)

                plt.draw() # обновление графика
                plt.gcf().canvas.flush_events() # обновление графикаиИ

                i = 0
                x1 += 3000
                x2 += 3000
            #plt.ioff()
            plt.show()
