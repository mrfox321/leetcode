def jumpGame(nums):

    visited = {}

    to_visit = []

    to_visit.append(0)
    visited[0] = 1
    goal = len(nums) - 1


    while to_visit:
        state = to_visit.pop()

        if state == goal:
            return True

        jump = nums[state]
        start = max(0,state-jump)
        end = min(len(nums),state+jump+1)

        for new_state in xrange(start,end):
            if new_state not in visited:
                visited[new_state] = 1
                to_visit.append(new_state)
    return False
