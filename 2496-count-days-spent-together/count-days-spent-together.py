class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def to_day_of_year(date: str) -> int:
            month, day = int(date[:2]), int(date[3:])
            return sum(days[: month - 1]) + day
        starta=to_day_of_year(arriveAlice)
        startb=to_day_of_year(arriveBob )
        enda=to_day_of_year(leaveAlice)
        endb=to_day_of_year(leaveBob)
        overlap_start = max(starta, startb)
        overlap_end = min(enda, endb)
        return max(0, overlap_end - overlap_start + 1)