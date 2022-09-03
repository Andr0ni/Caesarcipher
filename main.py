# шифрование + кол-во букв в слове
s = input('Введите предложение для шифровки(на английском):')
s = s.split()
b = 0
#k = int(input('Введите ключ для шифрования(на какое число символов смещение) (от 1 до 32):'))
for i in range(len(s)):
    k = len(s[i])
    if ',' in s[i] or '.' in s[i] or '!' in s[i]:
        k -= 1
    elif '"' in s[i]:
        k -= 2
    for j in range(len(s[i])):
        if s[i][j] in ',.!"':
            print(s[i][j], end='')
            continue
        if s[i][j].upper() == s[i][j]:
            b = ord(s[i][j].lower()) + k
            if b > 122:
                b = 96 - (122 - b)
            print(chr(b).upper(), end='')
        else:
            b = ord(s[i][j]) + k
            if b > 122:
                b = 96 - (122 - b)
            print(chr(b), end='')
    print(end=' ')
