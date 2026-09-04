day_so = list(range(1,21))  #day so tu 1 den 20

so_chan = [x for x in day_so if x % 2 == 0]   #lay ra cac so chan
so_le = [x for x in day_so if x % 2 != 0]    #lay ra cac so le

print("So chan: ", so_chan)
print("So le: ", so_le)