nums = [1, 2, 3, 4, 5]

n = len(nums)


# i 번째 원소의 자리를 바꿔가면서 순열 생성
# 자리를 바꿀 수 있는 경우의 수

def perm1(i):
    # 종료 조건
    if i == n:
        print(nums)
        return

    # 재귀 호출
    # 현재위치 i와 다른위치 j의 자리 교환
    # j를 선택할 때 중복 방지를 위해 i보다 뒤에 있는 원소만 선택
    # i, j가 같을 수 있음(자리 안바꾸는 경우)
    # i번째 자리를 누구랑 바꿀지 정했다면 i+1번째 원소 바꾸러 진행
    for j in range(i, n):
        # i 번째와 j 번째 위치를 바꾸고 진행
        nums[i], nums[j] = nums[j], nums[i]
        # 다음 i + 1 번째 원소 자리 바꾸기
        perm1(i + 1)
        # # i 번째와 j 번째 위치 되돌려놓고 다음 진행
        nums[i], nums[j] = nums[j], nums[i]


# perm1(0)

nums = [1, 2, 3, 4, 5]


def perm2(i, selected):
    if i == n:
        print(selected)
        return

    for j in range(n):
        if nums[j] not in selected:
            # i 번째 위치에 j를 놓기
            selected[i] = nums[j]
            perm2(i + 1, selected)
            selected[i] = 0

perm2(0, [0] * 5)
