import crcmod

file = open('output_1.pof', 'rb')
file_data = bytearray(file.read())
for_crc = open('for_crc.pof', 'wb')

crc_list = [["CRC-16/CCITT-FALSE", 0x1021,	0xFFFF,	False, 0x0000],
            ["CRC-16/ARC", 0x8005, 0x0000, True, 0x0000],
            ["CRC-16/AUG-CCITT", 0x1021, 0x1D0F, False, 0x0000],
            ["CRC-16/BUYPASS", 0x8005, 0x0000, False, 0x0000],
            ["CRC-16/CDMA2000", 0xC867, 0xFFFF,	False, 0x0000],
            ["CRC-16/DDS-110", 0x8005,	0x800D,	False, 0x0000],
            ["CRC-16/DECT-R", 0x0589,	0x0000,	False, 0x0001],
            ["CRC-16/DECT-X", 0x0589,	0x0000,	False, 0x0000],
            ["CRC-16/DNP", 0x3D65,	0x0000,	True, 0xFFFF],
            ["CRC-16/EN-13757",	0x3D65,	0x0000,	False, 0xFFFF],
            ["CRC-16/GENIBUS", 0x1021,	0xFFFF,	False, 0xFFFF],
            ["CRC-16/MAXIM", 0x8005,	0x0000,	True, 0xFFFF],
            ["CRC-16/MCRF4XX", 0x1021,	0xFFFF,	True, 0x0000],
            ["CRC-16/RIELLO", 0x1021, 0xB2AA,	True, 0x0000],
            ["CRC-16/T10-DIF",	0x8BB7,	0x0000,	False, 0x0000],
            ["CRC-16/TELEDISK",	0xA097,	0x0000,	False, 0x0000],
            ["CRC-16/TMS37157",	0x1021,	0x89EC,	True, 0x0000],
            ["CRC-16/USB", 0x8005,	0xFFFF,	True, 0xFFFF],
            ["CRC-A", 0x1021,	0xC6C6,	True, 0x0000],
            ["CRC-16/KERMIT", 0x1021,	0x0000,	True, 0x0000],
            ["CRC-16/MODBUS", 0x8005,	0xFFFF,	True, 0x0000],
            ["CRC-16/X-25",	0x1021,	0xFFFF,	True, 0xFFFF],
            ["CRC-16/XMODEM",	0x1021,	0x0000,	False, 0x0000]]

'''
   Algorithm             Poly        Init     RefIn/Out     XorOut
["CRC-16/CCITT-FALSE",	0x1021,	    0xFFFF,	    False,      0x0000]
["CRC-16/ARC",	        0x8005,	    0x0000,	    True,       0x0000]
["CRC-16/AUG-CCITT",	0x1021,	    0x1D0F,	    False,      0x0000]
["CRC-16/BUYPASS",	    0x8005,	    0x0000,	    False,      0x0000]
["CRC-16/CDMA2000",	    0xC867,	    0xFFFF,	    False,      0x0000]
["CRC-16/DDS-110",	    0x8005,	    0x800D,	    False,      0x0000]
["CRC-16/DECT-R",	    0x0589,	    0x0000,	    False,      0x0001]
["CRC-16/DECT-X",	    0x0589,	    0x0000,	    False,      0x0000]
["CRC-16/DNP",	        0x3D65,	    0x0000,	    True,       0xFFFF]
["CRC-16/EN-13757",	    0x3D65,	    0x0000,	    False,      0xFFFF]
["CRC-16/GENIBUS",	    0x1021,	    0xFFFF,	    False,      0xFFFF]
["CRC-16/MAXIM",	    0x8005,	    0x0000,	    True,       0xFFFF]
["CRC-16/MCRF4XX",	    0x1021,	    0xFFFF,	    True,       0x0000]
["CRC-16/RIELLO",	    0x1021,	    0xB2AA,	    True,       0x0000]
["CRC-16/T10-DIF",	    0x8BB7,	    0x0000,	    False,      0x0000]
["CRC-16/TELEDISK",	    0xA097,	    0x0000,	    False,      0x0000]
["CRC-16/TMS37157",	    0x1021,	    0x89EC,	    True,       0x0000]
["CRC-16/USB",	        0x8005,	    0xFFFF,	    True,       0xFFFF]
["CRC-A",	            0x1021,	    0xC6C6,	    True,       0x0000]
["CRC-16/KERMIT",	    0x1021,	    0x0000,	    True,       0x0000]
["CRC-16/MODBUS",	    0x8005,	    0xFFFF,	    True,       0x0000]
["CRC-16/X-25",	        0x1021,	    0xFFFF,	    True,       0xFFFF]
["CRC-16/XMODEM",	    0x1021,	    0x0000,	    False,      0x0000]
'''

def terminator(file_data):

    buffer = file_data[:-2]
    array = bytearray(buffer)
    return array

#terminator(file_data)


def crc_calculation(list_of_crc, array):
    
    for i in list_of_crc:
        alg = []
        for j in i:
            alg.append(j)
        crc_calc = crcmod.mkCrcFun(alg[1] | 0x10000, initCrc=alg[2], rev=alg[3], xorOut=alg[4])
        crc_value = crc_calc(array)
        if crc_value == 0x3a86:
            result = 'Success'
        else:
            result = 'Not match'
        print("algorithm = {:20}, crc_value = {:08X}, result = {}".format(alg[0], crc_value, result))

crc_calculation(crc_list, terminator(file_data))
