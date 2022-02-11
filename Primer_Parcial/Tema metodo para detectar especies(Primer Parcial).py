"""La compañía ACME S.A. está desarrollando un nuevo método para detectar especies en base a su ADN. Para 
representar una especie por su ADN se utiliza una secuencia S compuesta únicamente de las letras A, C, G y T.
Se tienen como datos:
Una lista L de secuencias S y una cadena de referencia R que identifica de forma única a la especie buscada. R no 
tiene letras repetidas.
Implemente un programa en Python que muestre todas las secuencias S que pertenecen a la especie buscada y los 
índices en la inversa de S (INV) donde aparece la cadena de referencia R.
Para realizar esta tarea, por cada secuencia S en L:
1. Forme la cadena inversa (INV) de la secuencia S.
2. Si la cadena R aparece exactamente dos veces en la segunda mitad de INV y al menos 3 veces en total, la 
secuencia S pertenece a la especie buscada.
3. Si S pertenece a la especie buscada, muestre la secuencia S y los índices.
Ejemplo:
L = [ 'ATTTGCTTGCTATTTAAACCGGTTATGCATAGCGC', 'ATTAGCCGCTATCGA', … ]
R = 'CG'
Salida:
Secuencia: ATTTGCTTGCTATTTAAACCGGTTATGCATAGCGC 
Índices: [0, 2, 7, 25, 29]
Secuencia: ... 
Índices: ..."""
L = [ 'ATTTGCTTGCTATTTAAA CCGGTTATGCATAGCGC', 'ATTAGCCGCTATCGA'] #Lista de prueba, puede tener mas elementos
R = 'CG'
for secuencia in L:
    secuencia_inversa = secuencia[::-1]
    cantidad_primera_mitad = secuencia_inversa[:len(secuencia_inversa) // 2].count(R)
    cantidad_segunda_mitad = secuencia_inversa[len(secuencia_inversa) // 2:].count(R)
    if (cantidad_segunda_mitad == 2) and ((cantidad_segunda_mitad + cantidad_primera_mitad) >= 3):
        indices = []
        for indice in range(len(secuencia_inversa) - 1):
            if R[0] == secuencia_inversa[indice] and R[1] == secuencia_inversa[indice + 1]:
                indices.append(indice)
        print("Secuencia: {}".format(secuencia))
        print("Indices: {}".format(indices))