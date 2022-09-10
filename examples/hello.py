from hatheist import *
code = [2, 36, 11, 7, 18, 1, 37, 4, 1, 37, 12, 2, 18, 17, 2, 36, 3, 6, 84, 104, 101, 114, 101, 32, 97, 114, 101, 32, 110, 111, 32, 103, 111, 100, 115, 46, -1, 1]
vm = Hatheistvm(code)
vm.until()
print (vm.out.out)
