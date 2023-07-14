compras = [{'item':'celular', 'precio':3000},{'item':'tv', 
'precio':75000}]
suma=0
for items in compras:
    print (items['precio'])
    suma+=items['precio']
    
print(suma)