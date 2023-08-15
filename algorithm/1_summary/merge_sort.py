def merge_sort(lst):
    def merge(l,r):
        result = []
        while len(l) > 0 and len(r) > 0:
            if l[0] <= r[0]:
                result.append(l.pop(0))
            else:
                result.append(r.pop(0))
        if len(l) > 0:
            result.extend(l)
        if len(r) > 0:
            result.extend(r)
        return result

    if len(lst) <= 1:
        return lst
    
    l = lst[:len(lst)//2]
    r = lst[len(lst)//2:]
    return merge(merge_sort(l), merge_sort(r))

print(merge_sort([3,1,2,5,4,6]))