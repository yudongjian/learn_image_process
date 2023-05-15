import torch


# 创建张量
a = torch.ones(3,4)
print(a)
print(type(a))

b = torch.tensor([[1,2,3],[4,5,6],[7,8,9]])
print(b)
print(type(b))

# 张量之间的运算
a = torch.tensor([1,2])
b = torch.tensor([2,2])

c = a.add(b)
print(c)
print(a)

c = a.add_(b)  # 带下划线的计算，也会改变其自身的值
print(c)
print(a)