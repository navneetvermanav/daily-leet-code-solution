class MyCalendarThree:

    def __init__(self):
        self.intervals = []

        
    def meeting_room(self,intervals):
        intervals.sort()
        
        room = []
        heapq.heappush(room, intervals[0][1])
        
        for interval in intervals[1:]:
            if interval[0]>= room[0]:
                heapq.heappop(room)
            heapq.heappush(room, interval[1])
        return len(room)
            
        
        
    def book(self, start: int, end: int) -> int:
        self.intervals.append([start,end])
        return self.meeting_room(self.intervals)