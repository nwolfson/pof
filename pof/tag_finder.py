import struct

pof_file = open('output_1.pof', 'rb')
pof_file_data = bytearray(pof_file.read())
pof_file.close()
prog_pof = open('bytes.pof', 'wb')
bitstream_file = open('1.bitstream', 'rb')
bitstream = bytearray(bitstream_file.read())

def tag_finder(input_file, output_file, tag_adress):
    arr = []
    tag_counter = 0                     #   Счетчик тегов
    number_of_tags = input_file[0x8]    #   Получение числа тегов из файла
    print(number_of_tags)               #   Вывод числа тегов для проверки
    for adress in range(len(input_file)):
            if adress == tag_adress and tag_counter != number_of_tags:
                tag_counter += 1
                packet_length_tuple = struct.unpack_from('<hl', input_file, adress)
                packet_length = packet_length_tuple[1]
                print(packet_length)
                i = adress
                print(i)
                while i <= packet_length + adress + 5:
                    arr.append(input_file[i])
                    i += 1
                tag_adress = adress + 6 + packet_length
                print(tag_adress)
    array = bytearray(arr)
    print(array)
    output_file.write(array)


tag_finder(pof_file_data, prog_pof, 0xc)



