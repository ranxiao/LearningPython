# convert content into bites
from struct import *

# Store as bytes data
packed_data = pack('iif', 6, 19, 4.73)
print(packed_data)

# show size of bytes for integer and float types
print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))

# To get bytes data back to normal data: b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@'
original_data = unpack('iif', packed_data)
print(original_data)

