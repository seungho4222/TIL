def merge_sort(lst):
    l_lst = len(lst)
    if l_lst == 1:
        return lst
    l = lst[:l_lst // 2]
    r = lst[l_lst // 2:]
    return merge(merge_sort(l), merge_sort(r))


def merge(l, r):
    global cnt
    if l[-1] > r[-1]:  # 왼쪽 마지막원소가 더 크면 카운트
        cnt += 1
    ll = len(l)  # 왼쪽 길이
    lr = len(r)  # 오른쪽 길이
    li = 0  # 왼족 인덱스
    ri = 0  # 오른쪽 인덱스

    result = [0] * (ll + lr)  # 병합한 리스트
    idx = 0  # 병합용 인덱스
    while li < ll or ri < lr:
        if li < ll and ri < lr:
            if l[li] <= r[ri]:
                result[idx] = l[li]
                li += 1
                idx += 1
            else:
                result[idx] = r[ri]
                ri += 1
                idx += 1
        elif li < ll:
            result[idx] = l[li]
            li += 1
            idx += 1
        elif ri < lr:
            result[idx] = r[ri]
            ri += 1
            idx += 1
    return result


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0

    print(f'#{tc} {merge_sort(A)[N // 2]} {cnt}')
