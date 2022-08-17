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


def re_addTea(test):
    key = list()
    for k in test:
        flag = ""
        for i in range(32):
            if i < 16:
                flag += chr(ord(k[i]) + 3 * (i // 2))
            else:
                flag += chr(ord(k[i]) - i // 6)
        key.append(flag)

    return key


def re_addSugar(test):
    key = list()
    for c in test:
        flag = ""
        a = c[:16]
        b = c[16:]
        j = 0
        k = 0
        for i in range(len(c)):
            if i % 2 == 0:
                flag += b[j]
                j += 1
            else:
                flag += a[k]
                k += 1
        key.append(flag)
    return key


key = re_addSugar(re_addTea(re_addMilk()))

print("input")
for k in key:
    print(f"{k}")
