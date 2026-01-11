def median_in_stream(num:list[int]):
    import heapq
    min_heap = []
    max_heap = []
    #This stores list of median values
    #appended by the stream. 
    #last value always shows the latest
    #median
    median_latest = 0
    def get_median(num:list[int]):
        nonlocal median_latest
        
        for v in num:
            median_latest=add_value(v)
            print(f"latest value of the median is {median_latest}")
        return median_latest
    def add_value(v:int):
        nonlocal median_latest
        if v > median_latest:
            heapq.heappush(min_heap,v)
            if len(min_heap) - len(max_heap) == 2:
                heapq.heappush(max_heap,-heapq.heappop(min_heap))
        else:
            heapq.heappush(max_heap,-v)
            if len(max_heap) - len(min_heap) == 2:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
        
        if len(min_heap) == len(max_heap):
            median_latest = (min_heap[0] + -max_heap[0])/2
            
        else:
            if len(min_heap) > len(max_heap):
                median_latest = min_heap[0]
            else:
                median_latest = -max_heap[0]
        return median_latest
    return get_median(num)
input=[3,4,1,2,6]
median = median_in_stream(input)
print(f"input array {input} median is {median}")

