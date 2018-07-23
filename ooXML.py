# Python 3.6 ver
# name :  ooXML_header
#-*- coding : utf-8 -*-

import sys
import struct

f = open (sys.argv[1], 'rb')
f.seek(0)
sp = f.read(1024)

print("ooXML_Signature : ", hex(struct.unpack_from("<l", sp, 0x00)[0]))
print("ooXML_Version : ", hex(struct.unpack_from("<H", sp, 0x04)[0]))
print("ooXML_purpose bit flag : ", hex(struct.unpack_from("<H", sp, 0x06)[0]))
print("ooXML_compression bit flag : " , hex(struct.unpack_from("<H", sp, 0x08)[0]))
print("ooXML_last modify file time : " , hex(struct.unpack_from("<H",sp, 0x10)[0]))
print("ooXML_last modify file date : " , hex(struct.unpack_from("<H",sp, 0x12)[0]))
print("ooXML_crc-32 : " , hex(struct.unpack_from("<l", sp, 0x14)[0]))
print("ooXML_compressed size :" ,hex(struct.unpack_from("<l", sp, 0x18)[0]))
print("ooXML_uncompressed size : ", hex(struct.unpack_from("<l",sp, 0x22)[0]))
print("ooXML_file name length : ", hex(struct.unpack_from("<H",sp, 0x26)[0]))
print("ooXML_extra field length : ", hex(struct.unpack_from("<H", sp, 0x28)[0]))
