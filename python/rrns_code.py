import numpy as np
import random
import time




def encode(data,module):
    data_coding = np.zeros((len(data),len(module)))
    for i in range(0,len(data)):
        for j in  range(0,len(module)):
            mod = data[i] % module[j]
            data_coding[i,j] = mod
    return data_coding


# 费马小定理求逆元
# a^p-1 == 1(mod p)
# 于是a*a^p-2 == 1(mod p),a^p-2就是a关于p的逆元
def inverse(a, p):
    b = a**(p-2)
    return b % p


# for循环求逆元
def inverse_two(a,p):
    for i in range(1,9999999):
        t = a*i
        if (t%p == 1):
            return i
     
    
    
def CRT(remainder,module):
    T = np.zeros((1,len(module)))
    Y = np.zeros((1,len(module)))
    M = 1
    MM = np.zeros((1,len(module)))
    for i in range(0,len(module)):
        M = M * module[i]
    for j in range(0,len(module)):
        MM[0,j] = M/module[j]
    # 求逆元T
    for k in range(0,len(module)):
        T[0,k] = inverse(MM[0,k],module[k])
    for n in range(0,len(module)):
        Y[0,n] = T[0,n]*MM[0,n]*remainder[n]
    YY = np.sum(Y,axis=1)
    original_word = YY % M
    return original_word
        
    
    
def decode(remainder,module):
    original_data = np.zeros((1,len(remainder)))
    for i in range(0,len(remainder)):
        original_data[0,i] = CRT(remainder[i,:],module)
    return original_data

# test 

X = [61, 45]
M = [3, 5, 7, 11, 17]

A = encode(X,M)
print(A)
B = decode(A,M)
print(B)

# print(inverse(11,7))



# 主要参数
n = 14; k = 10;
N = 1024*1024*k;

modulus = [257,263,269,271,277,281,283,293,307,311,313,317,331,337]
modulus_1 = [257,263,269,271,277,281,283]
modulus_2 = [293,307,311,313,317,331,337]

'''
modulus = [79,83,89,97,101, 103,107,109,113,127,131,137,139,149]
modulus_1 = [79,83,89,97,101, 103,107]
modulus_2 = [109,113,127,131,137,139,149]
'''

'''
# 数据生成 10Mb二进制数据
data = np.random.randint(0,2,(1,N))
np.savetxt('data.txt',data,'%d')
'''

time_start=time.time()

# 数据导入
data_load = np.loadtxt('data.txt',dtype=int)
data_load = data_load.reshape((int(N/8),8))
print(data_load.shape)

# 数据转化，8位二进制转十进制
data_10_int = []
for i in range(0,int(N/8)):
    data_to_str = ''.join(str(i) for i in data_load[i,:])
    data_to_int = int(data_to_str,2)
    data_10_int.append(data_to_int)
print(len(data_10_int))


# 编码
print(data_10_int[0:2])
data_encode = encode(data_10_int,modulus)
print(data_encode)
print("encoding is over !")
np.savetxt('data_encode.txt',data_encode,'%d')

time_end=time.time()
print('totally cost',time_end-time_start)



time_start_2=time.time()
# 解码
data_encode_load = np.loadtxt('data_encode.txt',dtype=int)
data_decode = decode(data_encode_load,modulus)
print("decoding is over !")
time_end_2=time.time()
print('totally cost',time_end_2-time_start_2)
# 00np.savetxt('data_decode.txt',data_decode,'%d')

