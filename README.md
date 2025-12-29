# calculator
# 二进制与十进制之间的相互转换
def binary_to_decimal(binary_str):
     decimal_num = 0
     for i, digit in enumerate(reversed(binary_str)):
         decimal_num += int(digit) * (2 ** i)
     print(decimal_num)  # 输出
