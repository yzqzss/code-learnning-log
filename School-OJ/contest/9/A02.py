# Description

# 据说唐僧师徒四人经过千山万水去西天取经，突然又一天，来到一个寺庙里，发现了一本很厚的天书，调
# 皮的孙猴子把书打开，看了半天，发现里面一个字都没有，这就彻底激怒了大圣，他将书的某页撕掉了，
# 使得这本无字天书不完整。观世音派千里眼过来看看究竟，结果他看后，知道了大圣把书的最后一页撕掉
# 了，若加上这一页该书的页码中正好出现了2022个数字2。聪明的您能否帮千里眼算算该天书一共有多少
# 页吗？

# Input

# 无

# Output

# 一个正整数（表示该书的页码）

sum = 0
for i in range(1, 4000):
    sum+=str(i).count('2')
    if sum == 2022:
        print(i)
        break
