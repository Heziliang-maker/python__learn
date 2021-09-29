print(1 + 2 + 3)
a = 0
c = a and 1
print(c)
print(bool((1,)))
a = 1
b = 2
c = 3
print(a or b and c)
# 1
print((a or b) and c)
# 3
# and or not 其中and的优先级>or 从左向右的规则被打破 如果要从左向右可以用括号括起来
