
import random

class SystolicArray:
    def __init__(self, size):
        self.size = size
        self.weights = [[0] * size for _ in range(size)]

    def load_weights(self, B):
        for i in range(self.size):
            for j in range(self.size):
                self.weights[i][j] = B[i][j]

    def run(self, A, B):
        size = self.size
        total_mac=size * size * size
        self.load_weights(B)
        a_flow = [[0] * size for _ in range(size)]
        b_flow = [[0] * size for _ in range(size)]
        C = [[0] * size for _ in range(size)]

        total_cycles = 3 * size - 2

        for t in range(total_cycles):
            for i in range(size):
                k = t - i
                if 0 <= k < size:
                    a_flow[i][0] = A[i][k]
                else:
                    a_flow[i][0] = 0

            for j in range(size):
                k = t - j
                if 0 <= k < size:
                    b_flow[0][j] = B[k][j]
                else:
                    b_flow[0][j] = 0

        
            new_a_flow = [[0] * size for _ in range(size)]
            new_b_flow = [[0] * size for _ in range(size)]

            for i in range(size):
                for j in range(size):
                    a_val = a_flow[i][j]
                    b_val = b_flow[i][j]

                    C[i][j] += a_val * b_val

                    if j + 1 < size:
                        new_a_flow[i][j + 1] = a_val
                    
                    if i + 1 < size:
                        new_b_flow[i + 1][j] = b_val

            a_flow = new_a_flow
            b_flow = new_b_flow

        stats = {
        'mac_ops': total_mac,
        'cycles': total_cycles,
        'pe_utilization': total_mac / (size * size * total_cycles),
        'throughput_gops': (total_mac / total_cycles) * 1e-9  
             }

        return C, stats


# 测试
if __name__ == "__main__":
     rows,cols=4,4
     A = [[random.randint(1, 10) for i in range(cols)] for j in range(rows)]
     B = [[random.randint(1, 10) for i in range(cols)] for j in range(rows)]
     sa = SystolicArray(4)
     
     C = sa.run(A, B)
     
     print("Result:")
     for row in C:
        print(row)
     