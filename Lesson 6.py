
#
# # file open
# try:
#     a = int(input("a = "))
#     b = int(input("b = "))
#     c = a/b
#     print(c)
# except Exception as ex:
#     print(ex)
# finally:
#     print("file close")
#
# print("end")


# def checker(var1):
#     if type(var1) != str:
#         raise TypeError(f"{var1} not string")
#     else:
#         return var1
#
# a = 12
# checker(a)


result = []
def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a/b

data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}
for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)