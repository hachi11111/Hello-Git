def calculate_original_peaches(n, m):
    # 从第n号猴开始逆向计算
    peaches = m
    for _ in range(n):
        peaches = peaches * 2 + 1
    return peaches

def main():
    n = int(input("请输入第n号猴: "))
    m = int(input("请输入剩下m个桃子: "))
    
    result = calculate_original_peaches(n, m)
    print(f"原本有 {result} 个桃子")

if __name__ == "__main__":
    main()
    
