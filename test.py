# @Time       :      2020/3/27 16:15
# @Description: 比较版本号

a = '1.131.2'
b = '1.131.1'
print(a.split('.'))

def test(a, b):
    a_list = a.split('.')
    b_list = b.split('.')
    if len(a_list) == len(b_list):
        for i in range(len(a_list)):
            if a_list[i] > b_list[i]:
                return a
            elif a_list[i] < b_list[i]:
                return b
            else:
                continue
print(test(a, b))
