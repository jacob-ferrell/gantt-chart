from models.time_period import TimePeriod

class Ship:
    # Represents each ship within the dataset
    def __init__(self, name, maintenance, docking):
        self.name = name
        self.maintenance = maintenance
        self.docking = docking
        self.overlap = TimePeriod.find_overlap(self.maintenance, self.docking)
    
