import random

def generate_large_fraction():
    # 生成随机的分子和分母
    length = random.randint(5, 10)  # 分子和分母的长度
    numerator = ''.join(random.choices('0123456789', k=length))
    denominator = ''.join(random.choices('0123456789', k=length))
    return numerator, denominator

def main():
    # 生成多个大分式
    for _ in range(5):  # 生成5个例子
        numerator, denominator = generate_large_fraction()
        print(f"Large Fraction: {numerator} / {denominator}")
        print()

if __name__ == "__main__":
    main()
