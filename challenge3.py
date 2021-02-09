def solution(xs):
    """
    To get maximum power, we just need to ensure we multiple by all postive numbers greater than 1
    and all pairs of negative numbers. First we split the numbers we want into 2 arrays, neg_arr
    for negative numbers and pos_arr for positive numbers except 0,1. Remove largest negative number in neg_array. Check length
    of neg_arr and only multiple up till the neg_n element. Finally, multiple by all the positive
    numbers than are greater than 1. Cast result to str and return.
    """
    neg_arr, pos_arr = list(), list()
    for num in xs: # O(n)
        if num < 0:
            neg_arr.append(num)
        if num > 1:
            pos_arr.append(num)

    ret = 1
    neg_n = len(neg_arr)
    if neg_n%2!=0:
        neg_max_value = -1001
        neg_max_index = 0
        for i,v in enumerate(neg_arr): # O(k)
            if v > neg_max_value:
                neg_max_index = i
                neg_max_value = v

        neg_arr.pop(neg_max_index)

    for j in pos_arr + neg_arr: # O(m+k)
        ret *= j

    # edge case: when there's only 1 neg number and/or 1s,0s for the rest of the array
    if ret == 1:
        return "0"
    return str(ret)

if __name__ == "__main__":
    assert solution([2,0,2,2,0]) == "8"
    assert solution([-2,-3,4,-5]) == "60"
    assert solution([2,-3,1,0,-5]) == "30"
    assert solution([-4]) == "0"
    assert solution([-4,0]) == "0"