def bonAppetit(bill, k, b):
    print('Bon Appetit' if sum(bill)-bill[k] == b*2 else bill[k]//2)
