import statistics

class data:

    def __init__(self, ages):
        self.ages = ages

    def count(self):
        return len(self.ages)

    def sum(self):
        return sum(self.ages)  

    def min(self):
        return min(self.ages)      
    
    def max(self):
        return max(self.ages)

    def ran(self):
        return range(self.ages)

    def mean(self):
        return int(statistics.mean(self.ages))

    def median(self):
        return int(statistics.median(self.ages)) 

    def mode(self):
        return int(statistics.mode(self.ages))   

    def standard_diviation(self):
        return statistics.stdev(self.ages)  

    def variance(self):
        return statistics.pvariance(self.ages)                   

D = data([31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26])       

print(D.count())
print(D.sum())
print(D.min())
print(D.max())
print(D.ran())
print(D.mean())
print(D.median())
print(D.mode())
print(D.standard_diviation())
print(D.variance())