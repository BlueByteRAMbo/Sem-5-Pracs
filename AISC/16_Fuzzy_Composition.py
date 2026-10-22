R = [[0.8,0.3,0.6],
     [0.4,0.9,0.2]]
S = [[0.7,0.2],
     [0.5,0.8],
     [0.1,0.9]]

rows_R = len(R)
cols_R = len(R[0])
rows_S = len(S)
cols_S = len(S[0])

if cols_R != rows_S:
    print("Given Relation Matrices are incompatible")
else:
    max_min = []
    max_product = []
    
    for i in range(rows_R):
        row_min = []
        row_product = []

        for j in range(cols_S):
            min_values = []
            product_values = []

            for k in range(cols_R):
                min_values.append( min(R[i][k],S[k][j]) )
                product_values.append( R[i][k]*S[k][j] )

            row_min.append(max(min_values))
            row_product.append(max(product_values))

        max_min.append(row_min)
        max_product.append(row_product)

print("---------------\nMax-Min Composition:")
for row in max_min:
    print(row)
print("---------------\nMax-Product Composition:")
for row in max_product:
    print(row)
