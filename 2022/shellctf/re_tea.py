def Milk():
    possibilitites = list()
    final = "R;crc75ihl`cNYe`]m%50gYhugow~34i"
    s = "50gYhugow~34i"
    rest = "R;crc75ihl`cNYe`]m%"
    for i in range(1, len(rest)):
        v14 = rest[:i]
        dest = rest[i:]
        possibilitites.append(dest + s + v14)
    return possibilitites


def Tea(test):
    possibilitites = list()
    for pos in test:
        flag = ""
        for i in range(0x20):
            if i < 0x20 // 2:
                flag += chr(ord(pos[i]) + 3 * (i // 2))
            else:
                flag += chr(ord(pos[i]) - i // 6)
        possibilitites.append(flag)

    return possibilitites


def Sugar(test):
    possibilitites = list()

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
        possibilitites.append(flag)
    return possibilitites


possibilitites = Sugar(Tea(Milk()))

print("input")
for pos in possibilitites:
    print(f"{pos}")
