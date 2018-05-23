#!/usr/bin/python
# -*- coding: utf-8 -*-
import re


# 加减运算
def add_subtract(expression):
    expression = expression.replace("+-", "-")
    expression = expression.replace("++", "+")
    expression = expression.replace("-+", "-")
    expression = expression.replace("--", "+")

    # 匹配加减号
    temp = re.compile('[\-]?\d+\.*\d*[\+\-]{1}\d+\.*\d*')
    flag = temp.search(expression)
    # 如果加减算式不存在, i.e. 加减计算已完成,返回计算式
    if not flag:
        return expression
    data = flag.group()
    if len(data.split("+")) > 1:
        part1, part2 = data.split("+")
        value = float(part1)+float(part2)
    elif data.startswith("-"):
        part1, part2, part3 = data.split("-")
        value = -float(part2)-float(part3)
    else:
        part1, part2 = data.split("-")
        value = float(part1)-float(part2)

    s1, s2 = temp.split(expression, 1)
    new_expression = "%s%s%s" % (s1, value, s2)
    return add_subtract(new_expression)


# 乘除运算
def mul_divide(expression):
    expression = expression.replace(" ", "")
    # 匹配乘除号
    temp = re.compile('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*')
    flag = temp.search(expression)
    # 如果乘除算式不存在, i.e. 乘除计算已完成,返回计算式
    if not flag:
        return expression
    data = flag.group()
    if len(data.split("/")) > 1:
        part1, part2 = data.split("/")
        if float(part2) == 0:
            exit("denominator is 0")
        value = float(part1)/float(part2)
    else:
        part1, part2 = data.split("*")
        value = float(part1)*float(part2)

    s1, s2 = temp.split(expression, 1)
    new_expression = "%s%s%s" % (s1, value, s2)
    return mul_divide(new_expression)


# 去掉括号
def rem_brackets(expression):
    temp = re.compile(r'\([^()]+\)')
    flag = temp.search(expression)
    if not flag:
        r1 = mul_divide(expression)
        r2 = add_subtract(r1)
        return r2
    sub = flag.group().strip('[()]')
    temp_result1 = mul_divide(sub)
    temp_result2 = add_subtract(temp_result1)
    s1, s2 = temp.split(expression, 1)
    new_expression = '%s%s%s' % (s1, temp_result2, s2)
    return rem_brackets(new_expression)


def main():
    exit_flag = False
    while not exit_flag:
        print("系统支持的计算式格式".center(20, "*"))
        print("\r")
        msg = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
        print(msg)
        print("\r")
        print("The end".center(27, "*"))
        user_exp = input("\r\n\r\n请输入计算式(限加减乘除), 输入quit退出: ")
        expression = user_exp.strip()
        if expression == "quit":
            exit_flag = True
        else:
            compute1 = rem_brackets(expression)
            compute2 = eval(expression)
            print("Result of expression：\033[31;1m%s\033[0m" % compute1)
            if float(compute1) == float(compute2):
                print("计算结果正确")
                print("\r")
            else:
                print("\r\n计算结果错误".center(20, "*"))
                print("\r")