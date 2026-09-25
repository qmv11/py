#6.1
print("Bai 6.1:\n")
def giai_thua_de_quy(n):
    if n <= 1: # dieu kien dung
        return 1
    return n * giai_thua_de_quy(n - 1)
def giai_thua_lap(n):
    ket_qua = 1
    for i in range(1, n + 1):
        ket_qua *= i
    return ket_qua
print(giai_thua_de_quy(5), "-", giai_thua_lap(5))

#6.2
print("\nBai 6.2:\n")
def fibonacci_de_quy(n):
    if n <= 1: # dieu kien dung
        return n
    return fibonacci_de_quy(n - 1) + fibonacci_de_quy(n - 2)
for i in range(10):
    print(fibonacci_de_quy(i), end=" ")
print()