result = []
try:
    def divider(a, b):
        if a < b:
            raise ValueError
        if b > 100:
            raise IndexError
        return a/b
except ValueError as e:
    print("")
except IndexError as c:
    print("")

try:
    data = {10: 2, 2: 5, "123": 4, 18: 0, 3: 15, 8: 4}
    for key in data:
        res = divider(key, data[key])
        result.append(res)
except:
    print("")

print(result)