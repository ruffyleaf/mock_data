# This is the class to create mock data for Airport Incidents
# an incident has 3 types - Accident, Serious Incident, Incident
# Incident is the most frequent, followed by Serious incident, followed by Accident

import random
from numpy import random as nprd

class Incident:
    
    def __init__(self, categories, date, lam):
        self.category = random.choice(categories)
        self.date = date
        self.no_occurrences = nprd.poisson(lam=lam, size=1)

    def write_data(self, filename):
        with open(filename, 'a') as f:
            f.write('{},{},{}\n'.format(self.date, self.category, self.no_occurrences[0]))
            f.close()
