N, S = 5, 'abac'  # 사전순 정렬된 부분문자 중 찾아야할 부분문자 번호, 문자열
A = [''] * len(S)  # 접미어 배열
for i in range(len(S)):
    A[i] = S[i:]  # ex) abac, bac, ac, c
A.sort()  # 접미어 배열 사전순 정렬 / ex) abac, ac, bac, c
j = 0  # 접미어 순서
cnt = len(A[j])  # 첫번째 접미어 길이 = 부분문자 수 체크 / len('abac')는 4이며, 이는 부분문자 (a, ab, aba, abac) 4개를 포함한다
k = 0  # LCP (Longest Common Prefix) 최장 공통 접두어
while N > cnt:  # 아직 찾아야할 부분문자 번호를 못찾았다
    k = 0  # LCP 초기화
    j += 1  # 다음 접미어
    while A[j][k] == A[j-1][k]:  # 이전 접미어와 앞자리부터 같은 글자 수 체크
        k += 1  # LCP 추가
    cnt = cnt + len(A[j]) - k  # j-1번째까지 부분문자 번호 + 다음 접미어 길이 - 중복 글자 수  <- j번째 접미어까지의 부분문자 번호
cnt = cnt - len(A[j]) + k  # j번째 접미어에 찾아야할 부분문자가 있다! -> 일단, j-1번째까지 부분문자 번호로 초기화 후 계산
print(f'#1 {A[j][0]} {k+N-cnt}')
# cnt: j-1번째 접미어까지의 부분문자 번호
# N: N번째 부분문자는 j번째 접미어에 있다 -> 무조건 cnt보다 크다
# k: j번째 접미어에 N번째 부분문자가 있지만, j-1번째까지의 부분문자 중에 중복된 부분문자가 있을 수 있으니 중복값 +
# ex) N이 5이면 abac에 부분문자 4개(a,ab,aba,abac)가 있고, ac에 5번째 부분문자가 있다.
# ex) but, ac(a,ac)에서 a는 앞에서 사용한 부분문자이므로 ac가 5번째 부분문자가 된다. (k=1)
