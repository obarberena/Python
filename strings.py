#my_string = "Hola Mundo!"
my_string = '''Este es un string que contiene\nsaltos de linea, como puedes ver.\nAdios!.'''


course = "Python3"
name = "Octavio"

final_message = "Nuevo curso de " + course + " por " + name #1
final_message = "Nuevo curso de %s por %s" %(course, name) #2
final_message = "Nueco curso de {} por {}".format(course, name)#format es un metodo y eso lo hace una "clase"
print(my_string)
print (final_message)