import struct
pof_file = open('1.pof', 'rb')
pof_file_data = bytearray(pof_file.read())
def tag_finder(p_file):
    number_of_tags = 0
    for i in range(len(p_file)):
        if i == 0xc:
            print("tag = " + str(p_file[i]), "at " + hex(i))
            number_of_tags += 1
            offset_i = struct.unpack_from('<hl', p_file, i)
            i += 6 + offset_i[1]
            print("tag = " + str(p_file[i]), "at = " + hex(i))
            number_of_tags += 1
            offset_i = struct.unpack_from('<hl', p_file, i)
            i += 6 + offset_i[1]
            print("tag = " + str(p_file[i]), "at = " + hex(i))
            number_of_tags += 1
            offset_i = struct.unpack_from('<hl', p_file, i)
            i += 6 + offset_i[1]
            print("tag = " + str(p_file[i]), "at = " + hex(i))
            number_of_tags += 1
            offset_i = struct.unpack_from('<hl', p_file, i)
            i += 6 + offset_i[1]
            print("tag = " + str(p_file[i]), "at = " + hex(i))
            number_of_tags += 1
            offset_i = struct.unpack_from('<hl', p_file, i)
            i += 6 + offset_i[1]


    print("number of tags = " + str(number_of_tags))

tag_finder(pof_file_data)
