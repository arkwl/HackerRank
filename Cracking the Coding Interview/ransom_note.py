def ransom_note(magazine, ransom):
    m_dict, r_dict = {}, {}
    for word in magazine:
        if (not word in m_dict):
            m_dict[word] = 1
        else:
            m_dict[word] += 1

    for word in ransom:
        if (not word in r_dict):
            r_dict[word] = 1
        else:
            r_dict[word] += 1

    for word in ransom:
        if (not word in m_dict):
            return False
        elif (r_dict[word] <= m_dict[word]):
            continue
        else:
            return False

    return True


m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
