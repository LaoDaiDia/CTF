def re_addMilk():
    key = list()
    pwd_final = "R;crc75ihl`cNYe`]m%50gYhugow~34i"
    s = "50gYhugow~34i"
    v14_dest = "R;crc75ihl`cNYe`]m%"
    for i in range(1, len(v14_dest)):
        v14 = v14_dest[:i]
        dest = v14_dest[i:]
        key.append(dest + s + v14)
    return key


def Tea(test):
    key = list()
    for pos in test:
        flag = ""
        for i in range(0x20):
            if i < 0x20 // 2:
                flag += chr(ord(pos[i]) + 3 * (i // 2))
            else:
                flag += chr(ord(pos[i]) - i // 6)
        key.append(flag)

    return key


def Sugar(test):
    key = list()

    for pos in test:
        flag = ""
        odd = pos[:0x10]
        even = pos[0x10:]
        j = 0
        k = 0
        for i in range(len(pos)):
            if i % 2 == 0:
                flag += even[j]
                j += 1
            else:
                flag += odd[k]
                k += 1
        key.append(flag)
    return key


key = Sugar(Tea(Milk()))

print("input")
for pos in key:
    print(f"{pos}")
