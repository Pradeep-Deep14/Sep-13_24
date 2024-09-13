L=['apple','apple','banana','Gauava','Pineapple']

fruit_count={}

def fruit_Count(L):
    for fruit in L:
        if fruit in fruit_count:
            fruit_count[fruit]+=1
        else:
            fruit_count[fruit]=1
fruit_Count(L)
    
for fruit,count in fruit_count.items():
   print(f"The count of {fruit} is : {count}")  