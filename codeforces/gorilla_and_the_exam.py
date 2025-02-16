n = int(input())

for _ in range(n):
    arr_length, deletes = map(int, input().split())
    counts = {}

    for val in map(int, input().split()):
        counts[val] = counts.get(val, 0) + 1
        
    reverse_counts = {}
    highest_frequency = 0
    unique_count = len(counts.values())
    
    for i in counts:
        highest_frequency = max(highest_frequency, counts[i])
        reverse_counts[counts[i]] = reverse_counts.get(counts[i], 0) + 1

    for i in range(1, highest_frequency + 1):
       if i in reverse_counts:
            while reverse_counts[i] > 0 and deletes >= i:
                deletes -= i
                reverse_counts[i] -= 1
                unique_count -= 1

            if deletes < i:  
                break
        
    print(max(unique_count, 1))
            
            