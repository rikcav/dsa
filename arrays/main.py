# For arrays, let's use lists as the example:
stock_prices = [298, 305, 320, 301, 292]

# Each element is accessible through its index
stock_prices[0]  # 298
stock_prices[2]  # 320

# In RAM, the elements are stored in sequential order:
# 0x00500    298
# 0x00504    305
# 0x00508    320
# 0x0050C    301
# 0x00510    292

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
# 0x0050C
# 0x00510

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


# Now about lookups by value:
# To find in which day the stock_price was 301,
# we can iterate through the array


# Linear search
def lookup_by_value(num, arr):
    for i in range(len(arr)):
        if arr[i] == num:
            return i

    return -1


lookup_by_value(301, stock_prices)

# This operation is of linear time complexity


# Now, to print all the prices:
# Again, we can iterate through the array

# Array traversal
for price in stock_prices:
    print(price)

# This operation also has linear time complexity


# To insert a value at a certain position:
# Inserting 284 at index 1 can be done with the insert method

# Array insertion
stock_prices.insert(1, 284)

# When the value is inserted, the proceding values have to be shifted.
# Thus making the operation have linear complexity, O(n)


# Delete elements by value:
# For deleting the element with value 305, we can use the remove method

# Array element deletion
stock_prices.remove(305)

# After deleting the element, the remaining elements have to be shifted,
# so the time complexity for this operation is linear, O(n)


# In Python, lists are implemented as dinamic arrays,
# meaning that the array size is not fixed.
# It grows to accomodate as many elements as you need.


# When a dinamic array is created, it initiates with a capacity, say 10
# 0x00500    new_dinamic_array
# 0x00504
# 0x00508
# 0x0050C
# 0x00510
# 0x00514
# 0x00518
# 0x0051C
# 0x00520
# 0x00524

# When the array reaches the total capacity,
# and you want to add another element (139),
# the program will reallocate memory at a
# different location with double the capacity (2*10 = 20)
# 0x00564    298    new_dinamic_array (new_capacity)
# 0x00568    305
# 0x0056C    320
# 0x00570    301
# 0x00574    292
# 0x00578    400
# 0x0057C    560
# 0x00580    901
# 0x00584    45
# 0x00588    602
# 0x0058C    139
# 0x00590    200
# 0x00594    210
# 0x00598    220
# 0x0059C    230
# 0x005A0    240
# 0x005A4    250
# 0x005A8    260
# 0x005AC    270
# 0x005B0    280


# Arrays typically don't stores different types in the same array,
# but Python lists do


# This is a 2D array:

stock_prices = [
    [2, 3, 5, 6],
    [40, 42, 38, 44],
    [78, 89, 71, 66]
]
