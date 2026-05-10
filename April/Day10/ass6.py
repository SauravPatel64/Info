
amount = int(input("Enter amount : "))

tenCoins = amount // 10
remaining = amount % 10
fiveCoins = remaining // 5

print(f"₹10 x {tenCoins}, ₹5 x {fiveCoins}")