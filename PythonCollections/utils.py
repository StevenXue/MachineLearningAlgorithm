# -*- coding: utf-8 -*-  
"""  
  @desc:  
  @author: StevenXue 
  @date: 2019/4/13
"""
from collections import Counter
from collections import OrderedDict


def equals_char_seq(str1, str2):
    """
    检查两个字符串是不是由相同字母不同顺序组成
    :param str1:
    :param str2:
    :return:
    """
    return Counter(str1) == Counter(str2)


def most_frequent_element_in_list(a_list):
    """
    查找列表中频率最高的值
    :param a_list:
    :return:
    """
    print(max(set(a_list), key=a_list.count))
    cnt = Counter(a_list)
    # 返回前三个数量最大的字符和数量
    return cnt.most_common(3)


def random_char_string(length):
    """
    随机生成指定位数的字符串
    :param length:
    :return:
    """
    import random, string
    str1 = string.ascii_letters
    str2 = string.digits
    all_char = str1+str2
    random_list = random.sample(all_char, length)
    print(random_list)
    return "".join(random_list)


def is_num(number):
    """
    判断是否为数字
    :param number:
    :return:
    """
    string = str(number)
    print("判断所有字符都是数字或者字母: ", string.isalnum())
    print("判断所有字符都是字母: ", string.isalpha())
    print("判断所有字符都是数字: ", string.isdecimal())
    print("判断所有字符都是数字: ", string.isnumeric())  # 此方法只针对unicode对象
    print("判断所有字符都是小写: ", string.islower())
    print("判断所有字符都是大写: ", string.isupper())
    print("判断所有字符都是空白符: ", string.isspace())
    return string.isdigit()


def get_maximum_common_divisor(num1, num2):
    """
    获取两数据的最大公约数
    :param num1:
    :param num2:
    :return:
    """
    if is_num(num1) and is_num(num2):
        # 获取最小的数
        min_num = num2
        if num1 < num2:
            min_num = num1
        result = 1
        for i in range(1, min_num + 1):
            if (num1 % i == 0) and (num2 % i == 0):
                print("公约数：", i)
                result = i
        return result
    else:
        return "Data format error"


def get_minimum_common_multiple(num1, num2):
    """
    获取两数据的最小公倍数
    :param num1:
    :param num2:
    :return:
    """
    if is_num(num1) and is_num(num2):
        # 获取最大的数
        greater = num1
        if num1 < num2:
            greater = num2

        while True:
            if (greater % num1 == 0) and (greater % num2 == 0):
                # print(greater)
                return greater
            else:
                greater += 1
    else:
        return "Data format error"


def test_int():
    # 整数间的判断， 各种类型处理， 进制转换
    number = float(input('请输入一个数字： '))
    num_sqrt = number ** 0.5
    print("平方根为： ", num_sqrt)
    num_three = number ** 3
    print("立方根为： ", num_three)

    print(is_num(0x3246A))
    print(get_maximum_common_divisor(16, 8))
    print(get_minimum_common_multiple(13, 169))
    number = 12
    print("十进制数据为: ", number)
    print("转换为二进制数据: ", bin(number))
    print("转换为八进制数据: ", oct(number))
    print("转换为十六进制数: ", hex(number))


def date_time_util():
    import calendar
    """
    时间格式处理
    """
    print(calendar.month(2019, 4))  # 显示日历
    print(calendar.monthrange(2019, 5))  # 显示某月份的天数和1号的星期数


def fibonacci_sequence(number):
    """
    打印斐波那契数列
    :param number:
    :return:
    """
    n1 = 0
    n2 = 1
    if is_num(number):
        if number == 0:
            return "请输入一个正整数。"
        if number == 1:
            print(n1)
        else:
            count = 0
            print("斐波那契数列: ")
            # 通过指定end参数的值，可以取消在末尾输出回车符，实现不换行。
            print(n1, ", ", n2, end=", ")
            while count < number:
                nth = n1 + n2
                print(n1+n2, end=", ")
    else:
        return "数据格式不对, 请传入整数。"


def sort_pao(sort_list):
    length = len(sort_list)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if sort_list[j] > sort_list[j + 1]:
                sort_list[j], sort_list[j + 1] = sort_list[j + 1], sort_list[j]
    return sort_list


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 23, 2, 3, 5, 44, 23, 2, 2, 1, 23, 6]
    print(sort_pao(a))
    # print(most_frequent_element_in_list(a))
    # print(random_char_string(6))
    new_list = [1, 2, 3, 2]
    print(list(reversed(new_list)))  # 列表逆序排列method1
    print(new_list[::-1])  # 反转列表method2
    print(max(new_list))  # 列表中的最大值
    # 移除列表中的重复元素，保持原序列
    print(OrderedDict.fromkeys(new_list).keys())

    # new_list = ["hello", 12, 10000, 100.5]
    # print(", ".join(str_or_list))  # 转换列表为逗号分割符格式, 如果格式统一
    # print(", ".join(map(str, new_list)))  # 转换列表为逗号分割符格式, 强制类型变为字符串
