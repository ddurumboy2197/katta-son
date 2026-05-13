def kattasini_top(sona1, sona2):
    if sona1 > sona2:
        return sona1
    else:
        return sona2

sona1 = int(input("Birinchi sonni kiriting: "))
sona2 = int(input("Ikkinchi sonni kiriting: "))

print(kattasini_top(sona1, sona2))
