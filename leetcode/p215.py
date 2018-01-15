import heapq #this is a min-heap

def findK(nums,k):
    #convert min-heap to max-heap
    nums = [-num for num in nums]

    heapq.heapify(nums)

    for i in xrange(k):
        x = heapq.heappop(nums)

    return -x
