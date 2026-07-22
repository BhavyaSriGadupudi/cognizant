import heapq

def heap_sort(a):
 heapq.heapify(a);return [heapq.heappop(a) for _ in range(len(a))]
