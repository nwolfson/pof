# -*- coding: utf-8 -*-
import datetime
import os

# Получить середину файла, удовлетворяющую следующим критериям
# 1. После этой середины должно быть не менее 2-х нулевых байтов подряд
# 2. Перед этой серединой не должно быть байта со значением 0xFF
def find_good_middle(data):
    data_middle = int(len(data) / 2)
    print(u"Предполагаемая середина файла {} = 0x{:08X}".format(data_middle, data_middle))
    while True:    # Цикл поиска "хорошей" середины.
                   # Внимание!!! Если хорошая середина не найдется скрипт упадет с исключением
        if data[data_middle - 1] != 0xFF and data[data_middle] == 0x0 and data[data_middle + 1] == 0x0:
            break
        data_middle += 1
        print(u"Сдвигаем разбиение файлов к {} = 0x{:08X}".format(data_middle, data_middle))
    return data_middle

# Функция записи двух половин файлов
def write_file_parts(filename, data, data_middle):
    # создаем экземпляр логгера
    start_sys_time = datetime.datetime.now()  # Получить текущее время
    temp_file_name = os.path.basename(filename).replace(".bitstream", "") # Получить название файла
    part1_file_name = u"{}_{}_part1.bitstream".format(temp_file_name, start_sys_time.strftime("%Y_%m_%d_%H_%M_%S"))
    part2_file_name = u"{}_{}_part2.bitstream".format(temp_file_name, start_sys_time.strftime("%Y_%m_%d_%H_%M_%S"))
    part1_file = open(part1_file_name, "wb")
    part2_file = open(part2_file_name, "wb")
    data_part1 = data[:data_middle]  # Получаем данные первой половины
    data_part2 = data[data_middle:]  # Получаем данные второй половины
    part1_file.write(data_part1)  # Записываем первую половину
    print(u"Записан файл с именем {} и размером".format(part1_file.name, len(data_part1)))
    part2_file.write(data_part2)  # Записываем вторую половину
    print(u"Записан файл с именем {} и размером".format(part2_file.name, len(data_part2)))
    part1_file.close()
    part2_file.close()


BIT_STREAM_FILE_NAME = "PC094.bitstream"      # задаем имя файла

bit_file = open(BIT_STREAM_FILE_NAME, "rb")   # Открываем файл на чтение в двоичном режиме
bit_file_data = bytearray(bit_file.read())        # Чтение всего содержимого файл в bit_file_data
bit_file.close()                              # Закрываем файл

data_good_middle = find_good_middle(bit_file_data)  # Определяем "хорошую" середину файла
write_file_parts(BIT_STREAM_FILE_NAME, bit_file_data, data_good_middle)
