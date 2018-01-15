import heapq

def findPairs(nums1,nums2,k):

    k = min(k,len(nums1)*len(nums2))
    print k
    len1 = len(nums1)
    len2 = len(nums2)

    if len2 < len1:
        swap = 1
        nums2,nums1 = nums1,nums2
        len2,len1 = len1,len2
    else:
        swap = 0

    pairs = []

    for i in xrange(min(len1,len2,k)):
        heapq.heappush(pairs,(nums1[i]+nums2[0],i,0))

    low_pairs = []

    triplet = heapq.heappop(pairs)
    tot,i,j = triplet[0],triplet[1],triplet[2]
    low_pairs.append([nums1[i],nums2[j]])

    while len(low_pairs) < k:

        if not pairs:
            i,j = i,j+1
            low_pairs.append([nums1[i],nums2[j]])

        elif j + 1 < len2:
            #check heap against candidate
            print i,j+1,pairs[0][0]
            if nums1[i] + nums2[j+1] <= pairs[0][0]:
                tot,i,j = nums1[i] + nums2[j+1],i,j+1
                low_pairs.append([nums1[i],nums2[j]])

            else:
                heapq.heappush(pairs,(nums1[i] + nums2[j+1],i,j+1))
                triplet = heapq.heappop(pairs)
                tot,i,j = triplet[0],triplet[1],triplet[2]
                low_pairs.append([nums1[i],nums2[j]])

        else:
            triplet = heapq.heappop(pairs)
            tot,i,j = triplet[0],triplet[1],triplet[2]
            low_pairs.append([nums1[i],nums2[j]])

    if swap == 0:
        return low_pairs
    else:
        low_pairs = [low_pairs[i][::-1] for i in xrange(len(low_pairs))]
        return low_pairs

print findPairs([1,2,4,5,6],[3,5,7,9],3)
