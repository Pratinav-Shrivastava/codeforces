def tc():
    ve = list(map(int, input().split()))
    st = set()
    st.add(ve[3] - ve[2])
    st.add(ve[2] - ve[1])
    st.add(ve[0] + ve[1])
    print(4 - len(st))

T = int(input())
for _ in range(T):
    tc()