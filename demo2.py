import os

# for root, dirs, files in os.walk(r'C:\Users\yudj\Desktop\复试材料准备'):
#     print('=====')
#     # print(root)
#     # print(dirs)
#     # print(files)
#     for i in files:
#         print(os.path.join(root,i))

a = ['a','b','v']

a = [
    {'name':'xx', 'age':11 },
    {'name':'xx', 'age':13 },
    {'name':'x1', 'age':11 },
    {'name':'x1', 'age':13 },
    {'name':'x2', 'age':11 },
    {'name':'x2', 'age':10 },
     ]

temp = []
temp_name = []
a = [1,2,3]
b = ['1','2','3']

c = zip(a,b)
for i in c:
    print(i)