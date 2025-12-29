# 八进制、十进制之间的相互转换
def dec_to_oct(num):
    if num == 0:
        return "0"
    oct_str = ""
    while num > 0:
        oct_str = str(n % 8) + oct_str
        num = num // 8
    return oct_str

def oct_to_dec(octal):
    dec_num = 0
    for i, digit in enumerate(reversed(octal)):
        dec_num += int(digit) * (8 ** i)
    return dec_num
