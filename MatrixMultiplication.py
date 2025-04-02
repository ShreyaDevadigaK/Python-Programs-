X = [[4,7],
 [2 ,5]]

Y = [[5,8],
 [6,7]]

result = [[0,0],
 [0,0]]
for i in range(len(X)):
 for j in range(len(Y[0])):
  for k in range(len(Y)):
     result[i][j] += X[i][k] * Y[k][j]
for r in result:
 print(r)
