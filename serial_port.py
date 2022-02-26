import serial

def serial_port():
    """ Определение подключенного com-порта Windows"""
    ports = ['COM%s' % i for i in range(256)]
    result = ''
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            return port
        except (OSError, serial.SerialException):
            pass
    return result


if __name__ == '__main__':
    print(serial_port())
