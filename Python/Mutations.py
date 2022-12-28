def mutate_string(string, position, character):
    string1 = string[:position] + character + string[position+1:] 
    return string1
