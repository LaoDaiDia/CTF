import string

m = 21
n = 22


def op(word, key):
    out = ''
    for i in range(0, len(word)):
        out = out + chr(word[i] ^ key)
    return out


def main():
    ciphertext_hex = open("cipher.txt", 'rb').read()
    print(ciphertext_hex)
    for i in ciphertext_hex:
        print(i)
    x = ciphertext_hex[:len(ciphertext_hex)//2]
    y = ciphertext_hex[len(ciphertext_hex)//2:]
    L = ''
    R = ''
    # print(R)
    for i in range(0, len(x)):
        L += chr(ord(op(y, n)[i]) ^ x[i])
    # print(L)
    for i in range(0, len(x)):
        R += chr(ord(op(L.encode(), m)[i]) ^ y[i])
    # print(R)
    print(R+L)

    # R1 = y1
    # L1 = ''
    # for i in range(0, len(x1)):
    #     L1 += chr(ord(op(R1, n)[i]) ^ ord(x1[i]))
    # x2 = L1
    # y2 = R1

    # for i in range(0, len(x)):
    #     L1 += chr(ord(op(R1, n)[i]) ^ ord(x[i]))

    #     x += chr(ord(op(R, m)[i]) ^ ord(L[i]))
    # y = op(R, 0)

    # L, R = y, x
    # x = ''
    # for i in range(0, len(L)):
    #     x += chr(ord(op(R, n)[i]) ^ ord(L[i]))
    # y = op(R, 0)


if __name__ == "__main__":
    main()
