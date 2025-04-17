import numpy as np

class A:

    def __init__(self, a1, a2, a3, a4):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
    
    def det(self): 

        row_1 = [self.a1, self.a2]
        row_2 = [self.a3, self.a4]
        list_1 = [row_1, row_2]
        result = list_1[0][0]*list_1[1][1] - list_1[0][1]*list_1[1][0]
        print(result)

mat = A(1, 2, 3, 4)
mat.det()

class B:
    
    def __init__(self, A1, A2, A3, A4):
        self.A1 = A1
        self.A2 = A2
        self.A3 = A3
        self.A4 = A4

    def det4(self):

        list_1 = [self.A1, self.A2, self.A3, self.A4]
        for i in range(0,4):
            for j in range(0,4):
                list_1.pop([i][j])
                result = ((-1)**(i+j)) *list_1[i][j] * ((list_1[i+1][i+1]*list_1[i+2][i+2]*list_1[i+3][i+3] + list_1[2][3]*list_1[1][2]*list_1[3][1] + list_1[1][0]*list_1[2][1]*list_1[0][2]) - (list_1[1][3]*list_1[2][2]*list_1[3][1] + list_1[2][3]*list_1[3][2]*list_1[1][1] + list_1[1][2]*list_1[2][1]*list_1[3][3]))
