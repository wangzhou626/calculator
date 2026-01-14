def show_menu():
    """显示主菜单"""
    print("\n=== 进制转换器 ===")
    print("1. 十进制 → 二进制")
    print("2. 十进制 → 八进制")
    print("3. 二进制 → 十进制")
    print("4. 八进制 → 十进制")
    print("0. 退出")
    print("=================")

def get_choice():
    """获取用户选择"""
    return input("请选择 (0-4): ")

def input_decimal():
    """输入十进制数（带验证）"""
    while True:
        try:
            num = int(input("请输入十进制数: "))
            if num >= 0:
                return num
            else:
                print("请输入非负数！")
        except ValueError:
            print("请输入有效的数字！")

def input_binary():
    """输入二进制数（带验证）"""
    while True:
        binary = input("请输入二进制数: ")
        if all(c in "01" for c in binary):
            return binary
        else:
            print("二进制数只能包含0和1！")

def input_octal():
    """输入八进制数（带验证）"""
    while True:
        octal = input("请输入八进制数: ")
        if all(c in "01234567" for c in octal):
            return octal
        else:
            print("八进制数只能包含0-7！")

def process_choice(choice):
    """处理用户的选择"""
    if choice == "1":
        num = input_decimal()
        result = dec_to_bin(num)
        print(f"十进制 {num} = 二进制 {result}")
        return True
    elif choice == "2":
        num = input_decimal()
        result = dec_to_oct(num)
        print(f"十进制 {num} = 八进制 {result}")
        return True
    elif choice == "3":
        binary = input_binary()
        result = bin_to_dec(binary)
        print(f"二进制 {binary} = 十进制 {result}")
        return True
    elif choice == "4":
        octal = input_octal()
        result = oct_to_dec(octal)
        print(f"八进制 {octal} = 十进制 {result}")
        return True
    elif choice == "0":
        return False
    else:
        print("输入错误！请输入0-4")
        return True
def main():
    """主函数"""
    print("欢迎使用进制转换器！")
    print("本程序由三位同学合作完成：")
    print("  学生A: 二进制与十进制转换")
    print("  学生B: 八进制与十进制转换")
    print("  学生C: 主程序")
    
    while True:
        show_menu()
        choice = get_choice()
        
        if not process_choice(choice):
            break
    
    print("\n谢谢使用，再见！")

if __name__ == "__main__":
    main()
    
