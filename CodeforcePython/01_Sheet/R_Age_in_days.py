N = int(input())

years = N // 365
N %= 365

months = N // 30
days = N % 30

print(f"{years} years")
print(f"{months} months")
print(f"{days} days")
