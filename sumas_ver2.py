from functools import reduce

compras = [{'item':'celular', 'precio':3000},{'item':'tv', 
'precio':75000}]

print(reduce(lambda suma,item: suma+item['precio'],compras,0))


