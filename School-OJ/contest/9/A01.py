# Description

# 请统计某个给定范围[L, R]的所有整数中，数字2出现的次数。比如给定范围[2, 22]，数字2在数2中出现了1次，在数12中出现1次，在数20中出现1次，在数21中出现1次，在数22中出现2次，所以数字2在该范围内一共出现了6次。

# Input

# 输入共1行，为两个正整数L和R，之间用一个空格隔开。（<=10000）

# Output

# 输出共1行，表示数字2出现的次数。

l,r=map(int,input().split())
str1=''
for i in range(l,r+1):
    str1+=str(i)
print(str1.count('2'))