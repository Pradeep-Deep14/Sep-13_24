str_var="aabccab"

def reverse_string(str_var):
    rev_str_var=""
    for i in range(len(str_var)-1,-1,-1):
            rev_str_var+=str_var[i]
    return str(set(rev_str_var))

print(reverse_string(str_var))
