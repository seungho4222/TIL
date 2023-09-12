# selection_sort[i] : i번째 자리에 놓을 리시트에서 i번째로 작은 원소 찾기

def selection_sort(i, lst):
    # 종료 조건
    if i == N:
        return
    # i번째에서 할 일
    minI = i
    for j in range(i + 1, N):
        if lst[j] < lst[minI]:
            minI = j
    lst[minI], lst[i] = lst[i], lst[minI]
    # 재귀 호출
    selection_sort(i + 1, lst)


lst = [3, 2, 4, 5, 1]
N = len(lst)
# 재귀 호출 시작
selection_sort(0, lst)
print(lst)
