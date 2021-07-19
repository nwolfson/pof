import struct
file = open('1.pof', 'rb')
file_data = bytearray(file.read())
f = struct.unpack_from('<hl', file_data, 0xc)
f1 = struct.unpack_from('<2l', file_data, 0x76)
f2 = struct.unpack_from('<hl', file_data, 0x74)
print(f)