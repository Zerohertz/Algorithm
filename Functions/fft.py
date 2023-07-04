from cmath import exp, pi


def fft(sig, inv):
    N = len(sig)
    if N == 1:
        return sig
    if inv == 0:
        sig_even = fft(sig[0::2], 0)
        sig_odd = fft(sig[1::2], 0)
        W = [exp(2j * pi * i / N) for i in range(N // 2)]
        return [sig_even[i] + W[i] * sig_odd[i]
                for i in range(N // 2)] + [sig_even[i] - W[i] * sig_odd[i] for i in range(N // 2)]
    elif inv == 1:
        sig_even = fft(sig[0::2], 1)
        sig_odd = fft(sig[1::2], 1)
        W = [exp(-2j * pi * i / N) for i in range(N // 2)]
        return [sig_even[i] + W[i] * sig_odd[i]
                for i in range(N // 2)] + [sig_even[i] - W[i] * sig_odd[i] for i in range(N // 2)]
