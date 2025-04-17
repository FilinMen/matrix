import numpy as np

class A:

    def __init__(self, A1, A2, A3, A4):
        self.A1 = A1
        self.A2 = A2
        self.A3 = A3
        self.A4 = A4
    
    def det(self): 

        matrix = np.array([[self.A1, self.A2], [self.A3, self.A4]])
        de = np.linalg.det(matrix)
        print(de)

mat = A(1, 2, 3, 4)
mat.det()
