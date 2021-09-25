#estructura de datos que almacena enteros, strings boleanos, listas y otros diccionarios.
#datos inmutables
diccionario = { 'a' : True, 5: "esto es un string"}

diccionario['c'] = 'nuevo string' #"reariamos clave /valor"
diccionario['a'] = False #Si la llave/clave se ecnuentra actualizada, sino crea

#valor = diccionario['a'] #obtenemos los valores
valor = diccionario.get('z', (12,2))

#del diccionario[5] #del nos ayuda a eliminar

#print(diccionario)
#print(valor)

llaves = tuple( diccionario.keys() ) #objeto iterable
valores = tuple( diccionario.values() )

diccionario_dos = {'z':23,'w':88}

diccionario.update(diccionario_dos)#el que queremos que incremente

print(llaves)
print(valores)
print(diccionario_dos)
