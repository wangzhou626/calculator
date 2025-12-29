# calculator
# 二进制与十进制之间的相互转换
def binary_to_decimal(binary_str):
     decimal_num = 0
     for i, digit in enumerate(reversed(binary_str)):
         decimal_num += int(digit) * (2 ** i)
     print(decimal_num)  # 输出

def dec_to_bin(dec_num):
    bin_str = ''
    while dec_num > 0:
        bin_str = str(dec_num % 2) + bin_str
        dec_num = dec_num // 2
    print(bin_str)  # 输出
