a = int(input("Enter your  total second"))
Hrs = (a//3600)

min = ((a//60)-(Hrs*60))
print(min)
sec = (a - (min*60 + Hrs*60*60))

print(f"Hours : {Hrs}, Minutes : {min}, Seconds : {sec}")