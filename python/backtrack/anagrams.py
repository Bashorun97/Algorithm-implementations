
'''
def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]

def all_perms(elements):
    if len(elements) <=1:
        return elements
    else:
        tmp = []
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                tmp.append(perm[:i] + elements[0:1] + perm[i:])
        return tmp

word = "abc"
print(list(all_perms(word)))
'''
def anagram(s1,s2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1
        
    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1
'''
def anagram(s1, s2):
    
    optimize = {ord(f) - ord('a'):ord(s) - ord('a') for f, s in zip(s1, s2)}
    left, right = 0, 0
    for k, v in optimize.items():
        left += k
        right += v
        print(left, right)
    print(optimize)
    if left != right:
        return False
    return True

  
print(anagram('apple','pleap'))
'''


    j = 0
    stillOK = True
    while j<26 and stillOK:
        if c1[j]==c2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK

print(anagram('apple','pleap'))