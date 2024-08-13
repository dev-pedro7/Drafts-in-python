def series_sum(n):
    if n == 0:
        return "0.00"
    total_som = 0.00
    for i in range(1, n+1):
        total_som += 1/ (3 * i - 2)
        
    return f"{total_som:.2f}" 