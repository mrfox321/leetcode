#djistras on an 1-d grid

class Solution(object):
    def jump(self, nums):
        unvisited = {i : len(nums)+1 for i in range(len(nums))}
        unvisited[0] = 0
        visited = {}
        old_state = 0
        while len(nums)-1 in unvisited:
            state = min(unvisited, key=unvisited.get)
            max_jump = nums[state]
            start = max(0,state-max_jump)
            end = min(state+max_jump,len(nums)-1)
            for new_state in range(start,end+1):
                if new_state != state and new_state != old_state
                    if new_state in visited:
                        if unvisited[state] + 1 < visited[new_state]:
                            visited[new_state] = unvisited[state] + 1
                    elif new_state in unvisited:
                        if unvisited[state] + 1 < unvisited[new_state]:
                            unvisited[new_state] = unvisited[state] + 1
            visited[state] = unvisited.pop(state)
            old_state = state
        return visited[len(nums)-1]
