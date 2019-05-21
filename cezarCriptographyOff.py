def cezarCriptographyOff(frazeCifrada, chave):
    # Alfabeto em uma lista para descriptografar/criptografar
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    #Recebe fraze cifrada, sepaara nos espaços e garante que sejam todas minusculas
    stringCifrada = frazeCifrada.lower().split(' ')
    # Cria lista vazia para receber a fraze decifrada
    stringDecifrada = []
    # Itera sobra cada palavra da fraze cifrada
    for n in stringCifrada:
    # Cria string vazia para receber o texto sendo decifrado
        resp = ''
        # Itera sobre os caracteres de cada palavra cifrada
        for b in n:
            # Caso o caractere esteja presente no alfabeto
            if b in alfabeto:
                # Recebe o index do caractere dentro do alfabeto
                index = alfabeto.index(b)
                # Caso o index seja maior ou igual a chave para decifrar(numero de casas)
                if index >= chave:
                    # Index recebe caractere decifrado
                    index = index - chave
                # Caso index seja menor que a chave     
                else:
                    # Index recebe caractere decifrado
                    index = index + (len(alfabeto) - chave)
                # String recebe palavra decifrada, letra por letra    
                resp = resp + str(alfabeto[index])
            # Caso não esteja presente no alfabeto, passa sem tratamento    
            else:
                # Caracteres não presentes no alfabeto passam sem tratamento
                resp = resp + b
        # Junta palaras decifradas em uma lista        
        stringDecifrada.append(resp)
    # Junta todas as palavras da lista com espaços pra separar    
    stringDecifrada = ' '.join(stringDecifrada)
    # Retorna a string decifrada
    return stringDecifrada
