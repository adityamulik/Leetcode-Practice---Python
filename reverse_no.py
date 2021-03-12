
no = 123;


def reverse(x):
    rev = 0
    while x>0:
        a = x%10
        print(a)
        rev = rev * 10 + a
        print(rev)
        x = x // 10
        print(x)

    return rev


print(reverse(no))