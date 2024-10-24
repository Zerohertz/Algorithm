import sys
from collections import defaultdict

read = sys.stdin.readline

DIV = 1_000_000_007


def fibonacci(n):
    if n == 0:
        return 0
    if n in [1, 2]:
        return 1
    if 0 < mem[n]:
        return mem[n]
    if n % 2 == 0:
        tmp = (
            fibonacci(n // 2) ** 2 + 2 * fibonacci(n // 2) * fibonacci(n // 2 - 1)
        ) % DIV
    else:
        tmp = (fibonacci((n + 1) // 2) ** 2 + fibonacci((n - 1) // 2) ** 2) % DIV
    mem[n] = tmp
    return tmp


def main():
    """
    F(n) = F(n-1) + F(n-2)
    F(n) = F(n-2) + F(n-3) + F(n-2)
         = 2*F(n-2) + F(n-3)
    F(n) = 2*F(n-3) + 2*F(n-4) + F(n-3)
         = 3*F(n-3) + 2*F(n-4)
    F(n) = 3*F(n-4) + 3*F(n-5) + 2*F(n-4)
         = 5*F(n-4) + 3*F(n-5)

    1, 2, 3, 5, 8
    1, 1, 2, 3, 5
    -> Fibonacci

    F(n) = F(k+1)*F(n-k) + F(k)*F(n-k-1)

    if k = n/2
    F(n) = F(n/2+1)*F(n/2) + F(n/2)*F(n/2-1)

    if n is even
    F(2n) = F(n+1)*F(n) + F(n)*F(n-1)
          = F(n)*[F(n+1) + F(n-1)]
          = F(n)*[F(n) + 2*F(n-1)]
          = F(n)^2 + 2*F(n)*F(n-1)
    F(n) = F(n/2)^2 + 2*F(n/2)*F(n/2-1)

    if n is odd
    F(2n+2) = F(2n+1) + F(2n)
    F(2n+1) = F(2n+2) - F(2n)
            = F(n+1)^2 + 2*F(n+1)*F(n) - F(n)^2 - 2*F(n)*F(n-1)
            = F(n+1)^2 + 2*F(n+1)*F(n) - F(n)^2 - 2*F(n)*(F(n+1) - F(n))
            = F(n+1)^2 + 2*F(n+1)*F(n) - F(n)^2 - 2*F(n+1)*F(n) + 2*F(n)^2
            = F(n+1)^2 + F(n)^2
    F(n) = F((n+1)/2)^2 + F((n-1)/2)^2
    """
    print(fibonacci(N))


if __name__ == "__main__":
    N = int(read())
    mem = defaultdict(int)
    main()
