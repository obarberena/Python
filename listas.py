my_list = ["strings", 15, 15.6, True]
my_list.append(6)
my_list.insert(1, "insert") #insterta la palabra en la posicion que quieras
my_list.remove(15) #solo remueve los numeros 15
last_value = my_list.pop()

print(my_list)



my_list2 = [22,23]
my_list = [1,9,22,6,8,65,14,99]
my_list.sort(reverse = True) #ordena de forma ascendente y si le agrego reverse, al reves
my_list.extend(my_list2) #agrega los numeros, no usar append porque no lo muestra igual
print(my_list)