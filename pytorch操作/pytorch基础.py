import torch

'''
张量
    标量  0维
    向量  1维
    矩阵  2维
    长方体 3维

'''
# todo 1 tensor 的创建
a = torch.Tensor(2, 3)
print(a)

b = torch.ones_like(a)
print(b)

c = torch.zeros_like(a)
print(c)

d = torch.randn(3, 4)
print(d)

# 正态分布 正态曲线呈钟型，两头低，中间高，左右对称因其曲线呈钟形，因此人们又经常称之为钟形曲线。

e = torch.normal(mean=0, std=torch.rand(5))  # 均值0，标准差 随机
print(e)

a1 = torch.Tensor(2, 3).uniform_(-2, 2)
print(a1)

# 序列

t1 = torch.arange(0, 10, 2)
print(t1)

t2 = torch.linspace(2, 10, 3)  # 等间隔的序列
print(t2)
print(t2.type())

t3 = torch.randperm(10)
print(t3)
print(t3.type())

# todo 2 tensor 的属性：device， dtype， 稠密、稀疏
# dev = torch.device('cpu') # 尚未安装cuda
c1 = torch.tensor([1, 2], dtype=torch.float)
print(c1)
print(c1.type())

i = torch.tensor([[0, 1, 2], [0, 1, 2]])
v = torch.tensor([1, 2, 3])
c2 = torch.sparse_coo_tensor(i, v, (5, 5))
c3 = torch.sparse_coo_tensor(i, v, (5, 5)).to_dense()
print(c2)
print(c3)

# todo 3 算术运算
'''
c = a + b
c = torch.add(a,b)
c = a.add(b)
a.add_(b)  # 带下划线 对本身的数据进行修改
# 同上 还有 div,mul 乘法：对应位置相乘
torch.pow(a,3) 幂运算 a的三次方
矩阵相乘 torch.mm, torch.matmul, @
torch.log(a)
torch.log_(a)
a.sqrt() 开方运算
乘法： 
    哈达玛积  对应位置相乘

'''

# todo 4 in_place 就地运算，原位操作
# x = x + y, add_，div_, mul_

# todo  5 广播机制
'''
广播机制: 
    张量参数可以自动扩展为相同大小
    广播机制需要满足两个条件:
        每个张量至少有一个维度,
        满足右对齐 （对应位置相同，或者有一个为1）

'''

# todo  6 tensor的比较运算
'''
torch.eq(a,b) 逐个比较 返回的也是tensor
torch.equal(a,b) 逐个比较 返回的是 一个 T/F
torch.gt, le,nt,lt,ge
torch.sort() 排序
torch.topk() 返回最大k个数值和索引值
torch.kthvalue() 返回最小k个数值和索引值

torch.isfinite(tensor) / torchisinf(tensor) / torchisnan(tensor)
返回一个标记元素是否为 finite/inf/nan 的mask 张量。



'''
a = torch.tensor([[1, 3, 2, 2, 5], [2, 1, 3, 1, 5]])
print(a)
print(a.sort())
print(a.sort(dim=0, descending=True))  # 列
print(a.sort(dim=1))  # 行

print(a.topk(k=2, dim=1))
print(a.topk(k=1, dim=0))

print(torch.isfinite(a))  # 是否有界
a = a / 0
print(torch.isinf(a))  # 是否无穷
print(torch.isnan(a))

# todo 7 torch的数学运算、统计学相关运算
'''
torch.abs()  绝对值
torch.erf()
torch.erfinv()
torch.sigmoid()  联系的 sign函数，常用激活函数，存在梯度消失
torch.neg0)
torch.reciprocal0)
torch.rsqrt()
torch.sign() 分段函数 ，x<0 y=0,x>0 y= 1
torch.lerp()
torch.addcdiv()
torch.addcmul()
torch.cumprod()
torch.cumsum()

Tensor中统计学相关的函数
    torch.mean()    #返回平均值
    torch.sum()     #返回总和
    torch.prod()    #计算所有元素的积
    torch.max()     # 返回最大值
    torch.min()     # 返回最小值
    torch.argmax()  #返回最大值排序的索引值
    torch.argmin()  #返回最小值排序的索引值

    torch.std()         返回标准差
    torch.var()         返回方差
    torch.median()      返回中间值
    torch.mode()        返回众数值
    torch.histc()       计算input的直方图
    torch.bincount()    返回每个值的频数
 
'''
a = torch.rand(2, 3)
print(a)
# 都是降维操作
print(a.sum())
print(a.mean())
print(torch.mean(a))
print(torch.prod(a))

a = torch.tensor([1, 2, 1, 2, 3, 4, 5])
print(torch.bincount(a))  # 只支持一位的张量

# todo 8
#  torch.distributions 分布函数

# todo 9 随机抽样

torch.manual_seed(1)  # 定义一个随机种子，可以保证每次抽样的数据一致
mean1 = torch.rand(1, 2)
std1 = torch.rand(1, 2)
print(torch.normal(mean=mean1, std=std1))

# todo 10 pytorch的线性代数运算
'''
 0范数、1范数、2范数、p范数、核范数
        求和、a:平方后求和再开方,b:..., |a-b|
torch.norm()  2范数
torch.dist(input,output,p=2)  p范数
'''
a = torch.tensor([9,16],dtype=float)
b = torch.tensor([3,4], dtype=float)
print(torch.dist(a,b,p=1))
print(torch.dist(a,b,p=2))
print(torch.norm(b))
print(torch.norm(b, p=1))
print(torch.norm(b, p='fro'))

# todo 11 矩阵分解
'''
常见的矩阵分解
    LU分解:将矩阵A分解成L (下三角)矩阵和U(上三角)矩阵的乘积 
    QR分解:将原矩阵分解成一个正交矩阵Q和一个上三角矩阵R的乘积
    
    EVD分解:
        特征值分解： 讲一个矩阵分解为---特征向量和特征值     
        PCA算法     满秩  无监督
        
        PCA与特征值分解  （方阵）
            PCA:将n维特征映射到k维上，这k维是全新的正交特征也被称为主成分，
            是在原有n维特征的基础上重新构造出来的k维特征PCA算法的优化目标就是:
                降维后同一纬度的方差最大
                不同维度之间的相关性为0
                协方差矩阵
                
    SVD分解: （m*n）
        奇异值分解     LDA算法     有监督
        LDA:    同类的间隔小，不同类别的间隔大
    


'''