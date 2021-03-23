
# import operator
# def find_lucky(arr_lucky):
#     print(arr_lucky.count(4))
#     count = {i:arr_lucky.count(i) for i in arr_lucky}
#     sorted_count = dict(sorted(count.items(), key=operator.itemgetter(1), reverse=True))
#     for c in sorted_count:
#         if c == sorted_count[c]:
#             print(c)
#             return c
#         else:
#             return -1


# Optimised Method

def find_lucky(arr):
    cnt = [0] * 501
    for a in arr:
        cnt[a] += 1
    for i in range(500, 0, -1):
        if cnt[i] == i:
            return i
    return -1

arr = [4,3,2,2,4,1,3,4,3]
print(find_lucky(arr))