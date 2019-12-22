from .procedural_semantic import *
class Database:
    def __init__(self):
        self.atimes = [ATime("B1", "HUE", "19:00HR"),
                        ATime("B2", "HUE", "22:30HR"),
                        ATime("B3", "HUE", "20:00HR"),
                        ATime("B4", "HCMC", "18:30HR")]
        self.dtimes = [DTime("B1", "HCMC", "10:00HR"),
                        DTime("B2", "HCMC", "14:30HR"),
                        DTime("B3", "DANANG", "16:00HR"),
                        DTime("B4", "DANANG", "8:30HR")]
        self.runtimes = [RunTime("B1", "HCMC", "HUE", "9:00HR"),
                          RunTime("B2", "HCMC", "HUE", "8:00HR"),
                          RunTime("B3", "DANANG", "HUE", "4:00HR"),
                          RunTime("B4", "DANANG", "HCMC", "10:00HR"),]
    
    def query(self, condition):
        if isinstance(condition, ATime):
            records = list(filter(lambda x: condition == x, self.atimes))
            if not records:
                return "No matching record"
            return ' '.join(list(map(lambda x: x.bus, records)))
        if isinstance(condition, DTime):
            records = list(filter(lambda x: condition == x, self.dtimes))
            if not records:
                return "No matching record"
            return ' '.join(list(map(lambda x: x.bus, records)))
        if isinstance(condition, RunTime):
            records = list(filter(lambda x: condition == x, self.runtimes))
            if not records:
                return "No matching record"
            return ' '.join(list(map(lambda x: x.time, records)))

