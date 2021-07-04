# def merge_the_tools(string, k):
#     for i in range(0,len(string),k):
#         print("".join(list(dict.fromkeys(string[i:i+k]))))
#
#
# if __name__ == '__main__':
#     string, k = input(), int(input())
#     merge_the_tools(string, k)
K, M = [int(x) for x in input().split()]
arrayN = []
for _i_ in range(K):
    arrayN.append([int(x) for x in input().split()][1:])

from itertools import product

possible_combination = list(product(*arrayN))


def func(nums):
    return sum(x * x for x in nums) % M


print(max(list(map(func, possible_combination))))