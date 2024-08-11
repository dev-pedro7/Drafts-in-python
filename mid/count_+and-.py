def count_positives_sum_negatives(arr):
    if not arr:
        return []
    negativo = 0
    count = 0
    for i in arr:
        if i < 0:
            negativo += i
        elif i > 0:
            count += 1
    return [count, negativo]
            