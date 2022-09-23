A, B, V = map(int, input().split())
D = (V - B) / (A - B)
print(int(D) if D == int(D) else int(D) + 1)