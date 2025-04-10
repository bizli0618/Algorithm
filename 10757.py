import sys

sys.set_int_max_str_digits(10001)

if __name__ == "__main__":
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)

