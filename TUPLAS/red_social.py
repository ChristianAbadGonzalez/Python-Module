# RED SOCIAL:
# Una red social tiene una base de datos de usuarios y sus correspondientes amistades. Crea un programa que tome una base de datos de una red social como una lista de
# tuplas, donde cada tupla contiene el nombre del usuario y una lista de sus amigos. Los nombres repetidos en la lista de amigos corresponden a usuarios con varias cuentas diferentes. 
# Deberas eliminar las cuentas duplicadas y después devolver una tupla de tuplas que contiene el número real de amigos por usuario y el usuario con más amigos.

# Pista 1: Tus datos de entrada podrían ser así —> red_social = [("Juan", ["Maria", "Pedro","Luis"]), ("Maria", ["Juan", “Pedro”,”Juan”]), ("Pedro", ["Juan", "Maria"]), ("Luis", [“Juan”])] 
# Pista 2: Para eliminar duplicidades puedes usar sets

red_social = [("Juan", ["Maria", "Pedro","Luis"]), ("Maria", ["Juan", "Pedro", "Juan"]), ("Pedro", ["Juan", "Maria"]), ("Luis", ["Juan"])]

# Se crea una nueva lista sin duplicados, eliminando las cuentas repetidas de amigos
red_social_sin_duplicados = []
for usuario, amigos in red_social:
    # Se crea una lista de amigos sin duplicados
    amigos_sin_duplicados = list(set(amigos))
    # Se agrega una nueva tupla a la lista red_social_sin_duplicados con el usuario y la lista de amigos sin duplicados
    red_social_sin_duplicados.append((usuario, amigos_sin_duplicados))

# Se crea una nueva lista que almacena el número de amigos de cada usuario
amigos_por_usuario = []
for usuario, amigos in red_social_sin_duplicados:
    # Se agrega el número de amigos de cada usuario a la lista amigos_por_usuario
    amigos_por_usuario.append((usuario, len(amigos)))

# Se convierte la lista amigos_por_usuario a una tupla para hacerla inmutable
amigos_por_usuario = tuple(amigos_por_usuario)

# Se imprime la lista completa de usuarios y su número de amigos correspondiente
print("Usuarios con número de amistades:", amigos_por_usuario)

# Se obtiene el usuario con más amigos, extrayendo el índice del máximo en la lista numero_amigos
lista_usuarios = [tupla[0] for tupla in amigos_por_usuario]
numero_amigos = [tupla[1] for tupla in amigos_por_usuario]

indice_con_mas_amigos = numero_amigos.index(max(numero_amigos))
usuario_con_mas_amigos = lista_usuarios[indice_con_mas_amigos]

# Se imprime el usuario con más amigos
print("Usuario con mayor conexión:", usuario_con_mas_amigos)

# Output: tuplas de tuplas -- usuario, número de amigos
# Output: Usuario con más amigos