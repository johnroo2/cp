from typing import List

def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    heap = [] #x, y, dist

    for point in points:
        distance = point[0]**2 + point[1]**2
        pointData = (point[0], point[1], distance)
        heap.append(pointData)
        
        idx = len(heap) - 1

        while idx > 0:
            parent_idx = (idx - 1) // 2
            if heap[parent_idx][2] > heap[idx][2]:
                heap[parent_idx], heap[idx] = heap[idx], heap[parent_idx]
                idx = parent_idx
            else:
                break
            
    res = []

    for _ in range(k):
        if not heap:
            break

        res.append([heap[0][0], heap[0][1]])

        heap[0] = heap[-1]

        search = 0

        while True:
            l, r = search * 2 + 1, search * 2 + 2
            smallest = search

            if l < len(heap) and heap[l][2] < heap[smallest][2]:
                smallest = l
            if r < len(heap) and heap[r][2] < heap[smallest][2]:
                smallest = r
            
            if smallest == search:
                heap.pop()
                break
            else:
                heap[search], heap[smallest] = heap[smallest], heap[search]
                search = smallest

    return res
            
        