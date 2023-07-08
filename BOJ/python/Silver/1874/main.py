import sys

read = sys.stdin.readline

n = int(read())
st = []
res = []
cnt = 1
tmp = True
for i in range(n):
    num = int(read())
    while cnt <= num:
        st.append(cnt)
        res.append("+")
        cnt += 1
    if st[-1] == num:
        st.pop()
        res.append("-")
    else:
        tmp = False

if tmp == False:
    print("NO")
else:
    for i in res:
        print(i)
