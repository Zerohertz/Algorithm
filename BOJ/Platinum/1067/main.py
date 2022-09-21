import sys
from cmath import exp, pi
read = sys.stdin.readline

def fft(sig, inv):
  N = len(sig)
  if N == 1:
    return sig
  if inv == 0:
    sig_even = fft(sig[0::2], 0)
    sig_odd = fft(sig[1::2], 0)
    W = [exp(2j*pi*i/N) for i in range(N//2)]
    return [sig_even[i] + W[i] * sig_odd[i] for i in range(N//2)] + [sig_even[i] - W[i] * sig_odd[i] for i in range(N//2)]
  elif inv == 1:
    sig_even = fft(sig[0::2], 1)
    sig_odd = fft(sig[1::2], 1)
    W = [exp(-2j*pi*i/N) for i in range(N//2)]
    return [sig_even[i] + W[i] * sig_odd[i] for i in range(N//2)] + [sig_even[i] - W[i] * sig_odd[i] for i in range(N//2)]

def mul(a, b, N):
  afft = fft(a, 0)
  bfft = fft(b, 0)
  c = [0 for i in range(N)]
  for i in range(N):
    c[i] = afft[i] * bfft[i]
  res = fft(c, 1)
  for i in range(N):
    res[i] = round(res[i].real / N)
  print(max(res))

N = int(read())

X = list(map(int, read().split()))
Y = list(map(int, read().split()))

ev = 0
for i in range(18):
  if N == 2**i:
    ev = -1
    break
  elif N * 2 < 2**i:
    ev = i
    break

if ev == -1:
  X = X + X
  Y = Y[-1::-1] + [0] * N
  mul(X, Y, 2 * N)
else:
  Np = 2**i
  N, Np = Np, N * 2
  X = X + [0] * (N - Np // 2)
  Y = Y[-1::-1] + [0] * (N - Np) + Y[-1::-1]
  mul(X, Y, N)