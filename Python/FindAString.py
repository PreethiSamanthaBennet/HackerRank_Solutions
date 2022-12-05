def count_substring(string, sub_string):
    c = 0
    l = len(sub_string)
    
    for i in range(0, len(string)):
        s = string[i:i+l]
        
        if s == sub_string:
            c +=1
    return c
