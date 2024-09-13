L=[1,1,2,3,4,5,6,6,7,8]
L1=[]
#Separate Unique and Duplicate Elements

def separate_unique_duplicate_elements(L):
    seen=set()
    unique_elements=[]
    duplicate_elements=[]
    for i in L:
        if i not in seen:
            unique_elements.append(i)
            seen.add(i)
        else:
            duplicate_elements.append(i)
            seen.add(i)
    return unique_elements,duplicate_elements

unique_elements,duplicate_elements=separate_unique_duplicate_elements(L)

print(f"The unique elements are : {unique_elements}")
print(f"The Duplicate elements are : {duplicate_elements}")