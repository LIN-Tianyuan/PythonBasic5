"""
@Time ：06/04/2024 15:10
@Auth ：LIN Tianyuan
@File ：exercise2.py
@Motto：ABC(Always Be Coding)
"""


# def my_max(n1, n2, n3):
#     list1 = [n1, n2, n3]
#     max_number = list1[0]
#     for element in list1:
#         if element >= max_number:
#             max_number = element
#     return max_number


def my_max1(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3


def my_max2(n1, n2, n3):
    max_number = n1
    if n1 < n2:
        if n2 < n3:
            max_number = n3
        else:
            max_number = n2
    return max_number


max_number1 = my_max1(2, 5, 4)
print(max_number1)

max_number2 = my_max2(2, 5287328327, 42260293209302)
print(max_number2)

