
roman_nos = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

s = "XIV"

# def roman_to_int(s):
#     n = len(s)
#     rt = 0
#     for i in range(n):
#         if i == n-1 or roman_nos[s[i]] >= roman_nos[s[i+1]]:
#             rt += roman_nos[s[i]]
#         else:
#             rt -= roman_nos[s[i]]
#
#
# print(roman_to_int(s))

# for i = 0 0 != 6 or 1000 > 100 True
# for i = 1 1 != 6 or 100 > 1000 False
# for i = 2 2 != 6 or 1000 > 10 True
# for i = 3 3 != 6 or 10 > 100 False
# for i = 4 4 != 6 or 100 > 1 True
# for i = 5 5 != 6 or 1 > 5 False
# for i = 6 6 == 6  True

# rt = 1000
# rt = 900
# rt = 1900
# rt = 1890
# rt = 1990
# rt = 1989
# rt = 1994

mappedS = [roman_nos[x] for x in s]
print(mappedS)
total = sum(mappedS)
print(total)
for i in range(len(mappedS) - 1):
    if mappedS[i] < mappedS[i+1]:
        total -= 2*mappedS[i]
print(total)

# total = 0
# prev = 0
# for i in range(len(s)):
#     curr = roman_nos[s[i]]  # all alphabet's respective roman value stored
#     # print(curr)
#     if curr > prev:
#         total += curr - 2 * prev
#         # print(total)
#     else:
#         total += curr
#     prev = curr
# print(total)

###### Explaination #########

# I
# II : I < I False
# III : I < I False
# IV : I < V True (4)
# V
# VI : V < I False
# VII : V < I False
# VIII : V < I False
# IX: I < X True (9)
# X
# XI: X < I False


# Total
# if no is 4 or 9
# total - 2(1)

#############################