n = int(input("son krinitng: "))

toq_natija = 0
juft_natija = 0

for i in range(1, n+1):
    if i % 2 == 0:
        juft_natija += i
    else:
        toq_natija += i

print("toq natija: ", toq_natija)
print("juft natija: ", juft_natija)


