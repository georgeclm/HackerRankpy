def bonAppetit(bill, k, b):
    bill[k] = 0
    print("Bon Appetit") if sum(bill) /2 ==b else print(int(abs(sum(bill) / 2 - b )))
