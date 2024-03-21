# For arrays, let's use lists as the example:
stock_prices = [298, 305, 320, 301, 292]

# Each element is accessible through its index
stock_prices[0]  # 298
stock_prices[2]  # 320

# In RAM, the elements are stored in sequential order:
# 0x00500    298
# 0x00504    305
# 0x00508    320
# 0x0050A    301
# 0x0050F    292

# In memory, the numbers would be stored in binary:
# 298 = 100101010

# For ints, in many programming languages,
# the binary number is stored in 4 bytes:
# 00000000 00000000 00000001 00101010

# Each byte would be stored in memory like so:
# 0x00500    00000000
# 0x00501    00000000
# 0x00502    00000001
# 0x00503    00101010

# Which would make the RAM representation look like this:
# 0x00500    00000000    298
# 0x00501    00000000
# 0x00502    00000001
# 0x00503    00101010
# 0x00504    00000000    305
# 0x00505    00000000
# 0x00506    00000001
# 0x00507    00110001
# ...

# Accessing elements by index works like so:
# When stock_prices is created, it is assigned a certain address in memory:
# 0x00500    stock_prices
# 0x00504
# 0x00508
# 0x0050A
# 0x0050F

# When you try to access any element of stock_prices by its index,
# this operation is done:
# stock_prices[0] -> 0x00500  # Beginning of stock_prices
# stock_prices[2] -> 0x00500 + 2 * sizeof(int)

# Considering int of size 4, it gives us:
# 0x00500 + 2 * 4
# 0x00500 + 8
# 0x00508

# So it peeks into the value inside 0x00508 memory address:
# 0x00508 -> 320

# Because only arithmetic operations are done,
# index lookups have constant time complexity, O(1)
