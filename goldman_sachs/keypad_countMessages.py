"""
Given a String,message that can contain the uppercase characters and space only. 
There are array of 8 strings representing the characters from keys 2 to 9.
Determine the key sequence needed to generate the message and then determine 
how many different messages that key sequence can form.
"""

def countMessages(key:list, message:str):
    key_map = {}

    for i in range(len(key)):
        for j in range(len(key[i])):
            key_map[key[i][j]] = (i,j+1)


    res = 1
    stack = []
    for char in message:
        #print(key_map[char])
        if char not in key_map:
            continue

        if not stack:
            stack.append(key_map[char])
        else:
            k, freq = key_map[char]
            if stack[-1][0] == k:
                stack.append((k, stack.pop()[1]+ freq))
            else:
                pass
                res *= 2**(stack.pop()[1]-1)
                stack.append(key_map[char])
    
    if stack:
        res *= 2**(stack.pop()[1]-1)

    return res % (10**9+7)

print(countMessages(['MGJ','YIZ','DKS','BHP','VENA','FLQ','URT','CWOX'], 'HHY'))
print(countMessages(['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ'], 'ME'))
print(countMessages(["MGJ","YIZ","DKS","BHP","VENA","FLQ","URT","CWOX"], "HEY HEY HEY"))
