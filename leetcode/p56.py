# Definition for an interval.
class Interval(object):
    def __init__(self,s,e):
        self.start = s
        self.end = e

def printIntervals(intervals):
    output = []
    for objects in intervals:
        output.append([objects.start,objects.end])
    print output


def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    intervals.sort(key = lambda x:x.start)

    index = 0
    while index < len(intervals) - 1:
        if intervals[index].end >= intervals[index+1].start and intervals[index].end <= intervals[index+1].end:
            intervals[index].end = intervals[index+1].end
            intervals.pop(index+1)
        elif intervals[index].end >= intervals[index+1].start and intervals[index].end > intervals[index+1].end:
            intervals.pop(index+1)
        elif intervals[index].end < intervals[index+1].start:
            start += 1

    return intervals
