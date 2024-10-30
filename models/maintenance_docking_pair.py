from models.time_period import TimePeriod

class MaintenanceDockingPair:
    def __init__(self, maintenance, docking):
        self.maintenance = maintenance
        self.docking = docking
        self.overlap = TimePeriod.find_overlap(maintenance, docking)