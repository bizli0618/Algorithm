import math

def eratos(start:int, end: int) -> list:
    '''
    에라토스테네스의 체 활용하여
    입력 받은 숫자보다 작은 모든 소수를 list 형태로 반환한다.
    '''
    is_prime = [True]*(end+1)

    for p in range(2, math.isqrt(end)+1):
        if is_prime[p]:
            for q in range(p*p, end+1, p):
                is_prime[q] = False
            
    prime_num = [x for x in range(max(2, start), end+1) if is_prime[x]]
    return prime_num

if __name__== "__main__":
    M, N = map(int, input().split())
    prime_numbers = eratos(M,N)
    for num in prime_numbers:
        print(num)
    