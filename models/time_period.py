from utils.calculate_duration import calculate_duration

class TimePeriod:
    # Represents a time period with a start date, end date, and method for calculating duration
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.duration = calculate_duration(self.start, self.end)

