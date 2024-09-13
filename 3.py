L=[1,2,3,4,4,5,6]
L1=[]
#Print unique elements alone

def unique_elements(L):
    for i in L:
        if i not in L1:
            L1.append(i)
    return L1

print(unique_elements(L))