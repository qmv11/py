c, d = 17, 5
thuong_du = divmod(c, d)    #divmod tra ve mot tuple (thuong, du)
thuong, du = thuong_du  #unpacking ket qua
print(f"{c} chia {d} duoc thuong {thuong}, du {du}")