def solution(N, a, M, b):
    N.sort()
    def binarysearch(array, target, start, end):
        if start > end:
            return None
        else:
            mid = (start+end)//2
            if array[mid] == target:
                return mid
            else:
                if array[mid] > target:
                    return binarysearch(array, target, start, mid-1 )
                else:
                    return binarysearch(array, target, mid+1, end)
    results = []     
    for i in b:
        result = binarysearch(a, i, 0, N-1)
        if result == None:
            results.append("No")
        else:
            results.append(result)
solution(5, [8,3,7,9,2], 3, [5,7,9])