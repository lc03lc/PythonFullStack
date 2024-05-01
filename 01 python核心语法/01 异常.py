"""
try:
    sentence
except ERROR1:
    solution1
except ERROR2:
    solution2
except ...:
    solution...
else:
    Normal Condition
Finally:
    Any Condition
"""

try:
    num = int(input('请输入一个整数: '))
    res = 8 / num
except ValueError as e:
    print('请输入整数', e)
except ZeroDivisionError as e:
    print('除数不能是0', e)
else:
    print(res)
finally:
    print('感谢使用')
