# 1. 
# def Hashtag(string):
#     string = 'satu dua'
#     for i in string:
#         a = str(i.split(' '))
#         b = a.upper()
#         print(a)
        # print (string.join(b))
# Hashtag('satu dua')


# 2.
# def create_phone_number(number):


# 3.
# def even(list):
#     for i in list:
#         if i % 2 == 0:
#             return(i)
# def odd(list):
#     for i in list:
#         if i % 2 != 0:
#             return(i)
# def sort_ascending(lst):
#     for i in range(len(lst)):
#         for j in range(i+1, len(lst)):
#             if lst[i] > lst[j]:
#                 lst[i], lst[j] = lst[j], lst[i]
#     return lst
# def sort_descending(lst):
#     for i in range(len(lst)):
#         for j in range(i+1, len(lst)):
#             if lst[i] < lst[j]:
#                 lst[i], lst[j] = lst[j], lst[i]
#     return lst
# def sort_odd_even(num):
#     n = []
#     for item in num:
#         if j in odd(list):
#             n.append(j)
#         elif k in even(list):
#             n.append(k)


# # 4.
# def HollowTriangle(num):
#     for i in range(num, num+1, 1):
#         for j in range(num, num+1):
#             if j >= 10-i and j <= 10+i:
#                 num += '#'
#             else:
#                 num += '_'
#             num += '\n'