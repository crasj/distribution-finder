import numpy as np
class Distribution_Generator:
    def __init__(self, N):
        self.N = N
        self.distribution_type = 'uniform'
        self.data = np.array(N) * np.nan


    def get_sample_size(self):
        return self.N

    def get_data(self):
        return self.data

    def generate_data(self):
        self.data = np.random.uniform()
        return self.data