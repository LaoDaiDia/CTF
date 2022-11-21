# import string

# m = 21
# n = 22


# def op(word, key):
#     out = ''
#     for i in range(0, len(word)):
#         out = out + chr(ord(word[i]) ^ key)
#     return out


# def main():
#     content = 'DOCTF{'
#     L = content[:len(content)//2]
#     R = content[len(content)//2:]
#     x = ''
#     for i in range(0, len(L)):
#         # print(ord(op(R, m)[i]))
#         # print(type(op(R, m)[i]))
#         # print(chr(ord(op(R, m)[i]) ^ ord(L[i])))
#         x += chr(ord(op(R, m)[i]) ^ ord(L[i]))
#     y = op(R, 0)

#     L, R = y, x
#     x = ''
#     for i in range(0, len(L)):
#         x += chr(ord(op(R, n)[i]) ^ ord(L[i]))
#     y = op(R, 0)

#     ciphertext = x+y
#     print(ciphertext)


# if __name__ == "__main__":
#     main()

ciphertext_hex = '47 4c 40 57 45 78 32 57 50 5c 37 5c 45 30 4a 5c 27 e2 99 a3 e2 80 bc ef bf bd 75 e2 96 bc 31 c2 b6 e2 86 93 e2 86 93 e2 97 84 e2 86 91 e2 98 bb 21 3b'

