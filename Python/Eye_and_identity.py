import numpy as np

n, m = map(int, input().split())

output = str(np.eye(n,m))
print(output.replace("0", " 0").replace("1", " 1"))
