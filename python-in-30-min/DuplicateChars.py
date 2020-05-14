# Task 2 -> Find all duplicate characters in a given string. For example, if the string is "rahul arora",
# the duplicate chars in ["r", "a"]

# # Python list
# myList = [100, 2, 10]  # 100 - 0th index, 2 - 1st index and 10 - 2nd index
# # print(myList)
# # print(myList[1])  # Acess
# # myList.append(5)  # Append
# # print(myList)
# # del myList[0]  # Delete
# # print(myList)

# # Iterate through a list
# for x in myList:
#     print(x)

# for index, x in enumerate(myList):
#     print("{} element at index {}".format(x, index))

# Python String
# myString = "Hello"  # -> myString = myStringChars = ["H", "e", "l", "l", "o"]
# print(myString[0])
# myString[0] = "P"
# print(myString[0])

# Python dictionary
# myDict = {
#     'name': 'rahul',
#     'age': 33
# }
# print(myDict['name'])  # Access
# # print(myDict['sex'])
# print(myDict.get('sex'))
# print(myDict.get('sex', "EMPTY"))

# myDict['name'] = 'rahul arora'
# print(myDict)

# myDict['sex'] = 'M'
# print(myDict)

# del myDict['sex']
# print(myDict)

# # Iterate
# for key, value in myDict.items():
#     print(key, value)

# Task 2 -> Find all duplicate characters in a given string. For example, if the string is "rahul arora",
# the duplicate chars in ["r", "a"]

str = "rahul arora"
strDict = dict()  # Empty dict initialization
for char in str:
    strDict[char] = strDict.get(char, 0) + 1
# print(strDict)

duplicateCharList = []  # Empty list
for key, value in strDict.items():
    if value > 1:
        duplicateCharList.append(key)

print(duplicateCharList)
