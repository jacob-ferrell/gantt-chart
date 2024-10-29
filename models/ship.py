from utils.find_overlap import find_overlap

class Ship:
    # Represents each ship within the dataset
    def __init__(self, name, maintenance, docking):
        self.name = name
        self.maintenance = maintenance
        self.docking = docking
        self.overlap = find_overlap(self.maintenance, self.docking)
    
