file = open('poet.txt', 'r')
# print("Is this file readable? ", file.readable())
# print(file.read())
# print(file.readline())
# print(file.readlines())

# for line in file.readlines() : 
#     print(line)

#!Wrting
# file = open('poet.txt', 'a')
# file.write("It feels like heaven")

poet_2 = open('poet_2.txt', 'w')
poet_2.write('For God sake! Give you hand and let me love.')
poet_2.close()
# file.close()