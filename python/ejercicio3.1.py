nombre = "L"
apellidos = "R"
edad = "25"
email = "mail@mail.com"
telefono = "888-888-8888"
casado = True
con_hijos = False
amigos = ["Maria", "Mariana", "Martin", "Marcos", "Mauricio", "Mercedes"]
peliculas_vitas = ["John Wick 1", "John Wick 2", "John Wick 3"]

print("Nombre: {0}, Apellidos: {1}, Edad: {2}, Email: {3}, Telefono: {4}, Casado: {5}, Hijos: {6}".format(nombre, apellidos, edad, email, telefono, casado, con_hijos))
for amigo in amigos:
	print(amigo)
	
for pelicula in peliculas_vitas:
	print(pelicula)
