cipher = "QNNKG"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = 0
result = []


key = 0
while key < 26:
    
    result = []
    for l in cipher:
        location = alphabet.find(l) + key
        if l == " ":
            result.append(" ")
        elif location >= 26:
            location = location - 26
            result.append(alphabet[location])
            
        else:
            result.append(alphabet[location])
        
    print("".join(result) + str(26-key))
    # input()    
    key = key + 1




