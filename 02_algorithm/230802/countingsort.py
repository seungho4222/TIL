def counting_sort_asc(A, B, K):
    # A : 정렬 대상
    # B : 정렬 결과
    # K : 정렬 대상 중 최댓값(숫자 수를 세야하는데 배열의 크기)
    C = [0] * (K + 1)
    # C : 카운트 배열(원소의 개수를 세주고, 자리 정리)
    # C[X] = X의 등장 횟수
    # C[1] => A안에 1이 몇개 있는지?

    # 1. 각 원소의 등장 횟수를 세준다.
    for i in range(len(A)):
        # A[i]의 등장 횟수를 하나씩 증가시켜 주면 된다.
        C[A[i]["num"]] += 1

    # 2. 각 원소의 등장횟수를 계싼해서 각 원소가 들어갈 자리의 위치를 구해 준다.
    for i in range(1, len(C)):
        # i는 i보다 작은수가 몇개 있는지 알면 그뒤에 등장
        C[i] += C[i - 1]

    # 3. 뒤에서부터 A를 확인하면서 자리 채워줌
    # 뒤에서부터 확인하는 이유는 안정정렬(원래배열의 순서 보장)
    # 자리를 채울때마다 1씩 감소(자리중복 방지)
    # for i in range(len(B)):  # 불안정 정렬
    for i in range(len(B) - 1, -1, -1):
        # C[A[i]] => A[i]가 들어갈 자리를 가르킴(들어가기 전 1 빼기)
        # C[A[i]] -= 1
        C[A[i]["num"]] -= 1

        # 자리에 A[i]를 넣어주면 됨
        # B[C[A[i]]] = A[i]
        B[C[A[i]["num"]]] = A[i]


nums = [0, 4, 1, 3, 1, 2, 4, 1]
nums_dict = [
    {"name": "김", "num": 0},
    {"name": "이", "num": 4},
    {"name": "박", "num": 1},
    {"name": "최", "num": 3},
    {"name": "승", "num": 1},
    {"name": "천", "num": 2},
    {"name": "양", "num": 4},
    {"name": "홍", "num": 1},
]

result_asc = [0] * 8


# counting_sort_asc(nums_dict, result_asc, max(nums))
#
# print(result_asc)


def counting_sort_desc(A, B, K):
    C = [0] * (K + 1)
    for i in range(len(A)):
        C[A[i]] += 1
    for i in range(len(C) - 2, -1, -1):
        C[i] += C[i + 1]
    for i in range(len(B) - 1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]


counting_sort_desc(nums, result_asc, max(nums))

print(result_asc)
