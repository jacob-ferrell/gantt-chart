
class TimePeriod:
    # Represents a time period with a start date, end date, and duration
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.duration = self.end - self.start

