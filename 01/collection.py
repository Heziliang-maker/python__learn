# 集合
# 特性:1 不重复性 2. 一些操作 len / in /not in 3.无序性


__colect__ = {1, 2, 34}
# __colect__[0]
# __colect__[0:2]
# __colect__ = {1, 1, 2, 3, 3, 3, 3, 3}  => {1,2,3}
len1 = len(__colect__)
print(len1)
isIn = 1 in __colect__
print(isIn)

# 集合1中剔除集合2的
col1 = {1, 2, 3, 4, 5, 6}
col2 = {3, 4}

# - 操作符 求集合差集

col_res1 = col1 - col2
print(col_res1)
# 输出{1, 2, 5, 6}

# & 操作符 求集合交集

col_res2 = col1 & col2
print(col_res2)
# 输出{3, 4}

# | 操作符 合并集合(并集)

col_res3 = col1 | {7, 8}
print(col_res3)
# 输出{3, 4}|


# 定义空的集合

print(type({}))
# <class 'dict'>


print(type(set()))
# <class 'set'>
# 验证: 长度为0
print(len(set()))

print(type({1}))


def my_func(name):
    print(f"my name is {name}")


my_func('hzl')
print(type(my_func))
print(type(.22))
