#!/bin/python
"""
author: yan.zhao
contact: zhaoyanz405@gmail.com
date: 2019/10/8 8:38
"""

"""
数字金额转为中文说法，例如1001.25转为壹仟零壹元两毛五分数字金额转为中文说法，例如1001.25转为壹仟零壹元两毛五分
"""


def convert(number: float) -> str:
    RMB = {'1': '壹', '2': '贰', }
    integer_postion = {1: '', 2: '拾', 3: '佰', 4: '仟'}
    float_postion = {1: '毛', 2: '分', 3: '毫'}

    str_number = str(number)
    if '.' in str_number:
        _i, _f = str_number.split('.')
    else:
        _i, _f = str_number, None

    _i = list(_i)
    _i.reverse()

    str_i_list = []
    for index, char in enumerate(_i):
        str_i_list.append(RMB[char] + integer_postion[index + 1])
    str_i_list.reverse()
    print(str_i_list)


convert(1221)
