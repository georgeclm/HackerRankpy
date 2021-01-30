def getMoneySpent(keyboards, drives, b):
    result = []
    for i in keyboards:
        for j in drives:
            if i+j <= b:
                result.append(i+j)
    return max(result) if result else -1
