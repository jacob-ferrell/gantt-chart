from models.time_period import TimePeriod

# Find the overlap, if any, within two time periods
def find_overlap(period1, period2):
    overlap_start = max(period1.start, period2.start)
    overlap_end = min(period1.end, period2.end)

    if overlap_start < overlap_end:
        return TimePeriod(overlap_start, overlap_end)
    
    return None