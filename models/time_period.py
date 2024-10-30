
class TimePeriod:
    # Represents a time period with a start date, end date, and duration
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.duration = self.end - self.start

    # Find the overlap, if any, within two time periods, and return a new TimePeriod object
    @staticmethod
    def find_overlap(period1, period2):
        overlap_start = max(period1.start, period2.start)
        overlap_end = min(period1.end, period2.end)

        if overlap_start < overlap_end:
            return TimePeriod(overlap_start, overlap_end)

        return None

