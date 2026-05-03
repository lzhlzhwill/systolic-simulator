
import random

class martix:
    def multiplication(self, a, b):
        if len(a[0]) != len(b):
            print("无法相乘")
            return
        c = [[0 for i in range(len(b[0]))] for j in range(len(a))]
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(a[0])):
                    c[i][j] += a[i][k] * b[k][j]
        return c


    
if __name__ == "__main__":
    rows,cols=4,4
    a = [[random.randint(1, 10) for i in range(cols)] for j in range(rows)]
    b = [[random.randint(1, 10) for i in range(cols)] for j in range(rows)]
    c = martix()                     
              
    print("Result:")
    for row in c.multiplication(a, b):
        print(row)

