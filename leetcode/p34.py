def searchRange(nums, target, start):

    infs = 2308230823

    if (nums[0] < target and nums[-1] < target) or (nums[0] > target and nums[-1] > target):
        L = infs
        R = -infs
        return L,R

    elif nums[0] == target and nums[-1] == target:
        L = start
        R = start + len(nums) - 1
        return L,R

    else:
        center = len(nums)//2
        left = nums[:center]
        right = nums[center:]
        L_left,R_left = searchRange(left,target,start)
        L_right,R_right = searchRange(right,target,start+center)
        return min(L_left,L_right),max(R_left,R_right)

nums =[5,7,7,8,8,10]
target = 8

print searchRange(nums,target,0)
