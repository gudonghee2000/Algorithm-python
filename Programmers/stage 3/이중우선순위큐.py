import heapq


def solution(operations):
    heap = []
    max_heap = []
    for o in operations:
        a, b = o.split(" ")
        if a == "I":
            heapq.heappush(heap, int(b))
            heapq.heappush(max_heap, -int(b))
        elif a == "D":
            if len(heap) == 0:
                continue
            elif b == "-1":
                min_value = heapq.heappop(heap)
                max_heap.remove(-min_value)
            elif b == "1":
                max_value = heapq.heappop(max_heap)
                heap.remove(-max_value)

    return [max(heap), min(heap)] if len(heap) != 0 else [0, 0]