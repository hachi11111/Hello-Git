def multiply_large_numbers(n, x, y):
    # 将输入的字符串转换为整数
    num1 = int(x)
    num2 = int(y)
    
    # 计算乘积
    result = num1 * num2
    
    # 将结果转换为字符串并返回
    return str(result)

def main():
    n = int(input("请输入位数n: "))
    x = input("请输入第一个n位的数字: ")
    y = input("请输入第二个n位的数字: ")
    
    # 检查输入的数字是否符合要求
    if len(x) != n or len(y) != n:
        print("输入的数字位数不正确，请重新输入。")
        return
    
    result = multiply_large_numbers(n, x, y)
    print(f"相乘结果: {result}")

if __name__ == "__main__":
    main()

