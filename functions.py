def reverse_bytes(value):
    """Функция разворота байтов в обратном порядке"""
    bytes_step = 2
    bytes_length = len(value)
    temp_bytes = ''
    for i in range(bytes_length, 0, -bytes_step):
        bytes_length -= 2
        temp_bytes += (value[bytes_length:i])
    return temp_bytes


def calc_frequency(value):
    """Функция перерасчета в частоту"""
    value = int(reverse_bytes(value), 16) + 0x900000000
    frequency = ((800000000 * value) / 2**36) / 1e6
    return frequency


def calc_field(value):
    """Функция перерасчета в поле"""
    value = int(reverse_bytes(value), 16)
    KOEFF = 461719202
    KOEFF_KM = 21.0199428
    code_F_00 = (KOEFF/940000000) * 0x1000000000
    koeff_dds = KOEFF/code_F_00
    code_F_00 -=0x700000000
    total = ((value*koeff_dds)-(code_F_00*koeff_dds))/KOEFF_KM
    return total

def sum_bytes(value):
    """Функция проверки пакета байтов по контрольной сумме"""
    start_bit = b'\xff' # сложение со стартовым байтом
    total = int(start_bit.hex(), 16) # приведение к int, так как type(start_bit)=int
    for item in value[:5]:
        total += item
    total = hex(total) # приведение к hex, т.к. у контрольной суммы остается два последних симвоола
    if str(total[3:]) == hex(value[5])[2:]:
        return value.hex()[2:10] # возвращается 4 информационных байта
        #return value # байтовая строка


if __name__ == '__main__':
    print('reverse bytes:         ->', calc_frequency('2DCD2CE1'))
    print('reverse bytes:         ->', calc_frequency('f3484b9f'))
    print(sum_bytes(b'\xc5\x83\x1e\xf8\x9f\xfc'))
