import lote
c = lote.Lote('Peras', 100, 490.1)
print(c)
columnas = ['nombre', 'cajones']
for colname in columnas:
    print(colname, '=', getattr(c, colname))