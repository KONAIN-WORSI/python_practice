def fibonnaci(n):
    if n <= 0:
        return [0]
    if n == 1:
        return [1]
        
    series = [0,1]
    
    while len(series) < n:
        series.append(series[-1] + series[-2])
        
    sum_ = sum(series)
        
    return series, sum_
    
    
print(fibonnaci(10))
            
            