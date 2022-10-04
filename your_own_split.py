def mysplit(strng):
    n = len(strng)
    word_list = []
    while True:
        #print(f'string:{strng}')
        i = strng.find(' ')
        if i == 0:
            strng = strng[1:]
            continue
        elif i == -1:
            if strng != '':
                word = strng
                word_list.append(word)
            break
        else:
            word = strng[:i]
            strng = strng[i+1:]
            word_list.append(word)
    return word_list

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
