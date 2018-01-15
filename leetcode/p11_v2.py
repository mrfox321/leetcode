def new_bucket(buckets,new_index):
    new_buckets = []
    for bucket in buckets:
        new_buckets.append([bucket[0],new_index])
        new_buckets.append([bucket[1],new_index])
        new_buckets.append(bucket)
    return new_buckets

def collapse(buckets,height):
    new_buckets = []
    area = []
    for bucket in buckets:
        area.append((bucket[1]-bucket[0])*min(height[bucket[1]],height[bucket[0]]))
    max_area = max(area)
    for i in xrange(len(area)):
        if area[i] == max_area:
            new_buckets.append(buckets[i])
    return new_buckets, max_area

def maxArea(height):
    buckets = [[0,1]]
    min(height[1],height[0])
    for i in xrange(2,len(height)):
        buckets = new_bucket(buckets,i)
        buckets,area = collapse(buckets,height)
    return area

print maxArea([1,2,4,3])
