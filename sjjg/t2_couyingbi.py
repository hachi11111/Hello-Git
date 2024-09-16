def count_ways_to_make_change(n):
    # 将元转换为分
    n_cents = n * 100
    
    # 硬币面值
    coins = [1, 2, 5]
    
    # 初始化dp数组，dp[i]表示凑出i分钱的方法数
    dp = [0] * (n_cents + 1)
    
    # 初始条件
    dp[0] = 1
    
    # 动态规划计算
    for coin in coins:
        for i in range(coin, n_cents + 1):
            dp[i] += dp[i - coin]
    
    return dp[n_cents]

def main():
    n = int(input("请输入n的值（元）: "))
    result = count_ways_to_make_change(n)
    print(f"凑出{n}元钱的方法数为: {result}")

if __name__ == "__main__":
    main()
