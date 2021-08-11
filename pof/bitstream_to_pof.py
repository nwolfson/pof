import struct

pof_file = open('output_1.pof', 'rb')
pof_file_data = bytearray(pof_file.read())
pof_file.close()
prog_pof = open('bytes.pof', 'wb')
bitstream_file = open('1.bitstream', 'rb')
bitstream = bytearray(bitstream_file.read())

def tag_finder(input_file, tag_adress):
    arr = []
    for adress in range(0xc, 0x76):
        if adress == tag_adress and adress != 0x70:
            packet_length_tuple = struct.unpack_from('<hl', input_file, adress)
            packet_length = packet_length_tuple[1]
            i = adress
            while i <= packet_length + adress + 5:
                arr.append(input_file[i])
                i += 1
            tag_adress = adress + 6 + packet_length
        if adress == 0x70:
            i = adress
            while i <= adress + 5:
                arr.append(input_file[i])
                i += 1
    array = bytearray(arr)
    print(array)
    return array


def copy_file_part(input_file, start, stop):
    arr = []
    for i in range(start, stop):
        arr.append(input_file[i])
    array = bytearray(arr)
    print(array)
    return array

def write_bitstr(input_file):
    arr = []
    for i in range(len(input_file)):
        arr.append(input_file[i])
    array = bytearray(arr)
    return array

def terminator(input_file):    # терминатор находится в последних 8 байтах файла
    arr = []
    for i in range(len(input_file)):
        arr.append(input_file[i])
    buffer = arr[-8:]                       # последние 8 байтов
    array = bytearray(buffer)
    return array

def result_array(copy_1, tags, copy_2, bitstream, copy_3, terminator):      # сложение всех списков и запись в файл
    return copy_1 + tags + copy_2 + bitstream + copy_3 + terminator


prog_pof.write(result_array(copy_file_part(pof_file_data, 0x0, 0xc), tag_finder(pof_file_data, 0xc), copy_file_part(pof_file_data, 0x76, 0x100c2), write_bitstr(bitstream), copy_file_part(pof_file_data, 0x600c3, 0x80082), terminator(pof_file_data)))





