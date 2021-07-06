# global a, b, i
def print_rangoli(size):
    # your code goes here
    b = ""
    a = ""
    c = ""
    s = 64
    m = 2*size-1
    print(m)
    print(size)

    t = 4*size-3
    print(t)
    for i in range(1, m):
        for j in range(size, 0, -1):
            c = str(chr(s + j)).center(m, '-')
            print("this is c", c)
            for k in range(0, i-1):
                a = str(chr(s + j-k)).rjust(t-3, '-')
                print("this is a", a)

                b = str(chr(s + k+1)).ljust(t-3, '-')
                print("this is b", b)

        print("this is the new line", a + c + b)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)