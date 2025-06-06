a = int(input("son kritng: "))
b = int(input("son kritng: "))
c = int(input("son kritng: "))
d = int(input("son kritng: "))
e = int(input("son kritng: "))


n = (a, b, c, d, e)

for i in range(min(n)+1):
    print(i)
for x in range(max(n)+1):
    print(x)

result = (i, x)
natija = sum(result)

print(f"min {i}, max {x}: {i} + {x} = {natija}")
print(f"Javob: {natija / 2}")

