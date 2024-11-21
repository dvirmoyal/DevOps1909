

for i in range(0,101):
   if i % 7 != 0 and "7"  not in str(i) :
        print(i)


names = ["natan", "shay", "ronen", "aaron"]
result = [name.upper() for name in names if "n" in name]
print(result)

result = [print(i) for i in range(0,101) if i % 7 != 0 and "7" not in str(i)]