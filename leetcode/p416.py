def findSum(cur_sum,goal_sum,nums):

    if not nums:
        if cur_sum == goal_sum:
            return True:
        else:
            return

    for index,num in enumerate(nums):
        new_sum = cur_sum + num
        if new_sum <= goal_sum:
            findSum(new_sum,goal_sum,nums[index+1:])


#sort then reverse to start the search with the largest numbers.
