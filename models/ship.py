from models.time_period import TimePeriod
from models.maintenance_docking_pair import MaintenanceDockingPair

class Ship:
    # Represents each ship within the dataset
    def __init__(self, row):
        self.name = row['Ship Name']
        maintenance = TimePeriod(row['Maintenance Start Date'], row['Maintenance End Date'])
        docking = TimePeriod(row['Docking Start Date'], row['Docking End Date'])
        self.maintenance_docking_pairs = [MaintenanceDockingPair(maintenance, docking)]

    # Combine maintenance/docking time periods of to Ship objects
    def merge(self, other):
        self.maintenance_docking_pairs += other.maintenance_docking_pairs

    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other):
        return isinstance(other, Ship) and self.name == other.name
    
