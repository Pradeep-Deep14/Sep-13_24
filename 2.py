L=[1,2,3,4,4,5,6]
L1=[]
#Remove duplicates from list

def remove_duplicates(L):
    for i in L:
        if i not in L1 and L.count(i)>1:
            L1.append(i)
    return L1

print(remove_duplicates(L))