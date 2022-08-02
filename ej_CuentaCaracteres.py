#Leer un archivo de texto y saber con qué frecuencia aparece cada letra (caracter UNICODE) en el texto. 

from os import strerror

def create_default_TxtFile()->str:
    """_summary_
    Crea un archivo por defecto llamado 'text.txt' en modo escritura 'w y escribe en el
    3 líneas de texto con caracteres de ejemplo.
    Esto con el fin de 'ahorrar tiempo' al momento de probar el programa
    """
    default_Path = "text.txt"
    ex_file=open(default_Path,"w") 
    ex_file.write("abc\n") 
    ex_file.write("ABC\n") 
    ex_file.write("123.\n")  
    ex_file.close() 
    return default_Path

def readFilePath():
    """_summary_
    Solicita al usuario el nombre del archivo de texto que pretendemos tratar.
    Por defecto en caso de recibir una cadena vacía creará el archivo por defecto.
    Returns
    -------
    _type_  str or exit() if IOError
        _description_
        El nombre del archivo de texto o finaliza el programa en caso de no poder crearlo
    """
    source_file_name = input("Ingresa el nombre del archivo fuente: ")
    if(source_file_name == ''): source_file_name = create_default_TxtFile()  
    try:
        source_file = open(source_file_name, 'rb')
        source_file.close()
        return source_file_name
    except IOError as e:
        print("No se puede abrir archivo fuente: ", strerror(e.errno))
        exit(e.errno)


def openTXTchar_by_char(path :str = '', mode : str = '')->bool:
    """_summary_
    Lee el archivo de texto caracter x caracter para realizar el conteo de las ocurrencias de cada caracter
    Parameters, mostrando el resultado en orden descendente.
    ----------
    path : str, optional
        _description_ 
        Recibe la ruta y / o el nombre del archivo, by default ''
    mode : str, optional
        _description_
        Recibe el modo en el que se abrirá el archvo, by default ''

    Returns
    -------
    bool
        _description_
        False si se presentó algún error, True en caso contrario
    """
    success = True    
    char_conunter = {chr(x) : 0 for x in range(48,123) if x not in (58,59,60,61,62,63,64,91,92,93,94,95,96)}
    try:
        stream = open(path, mode)
        line = stream.readline()
        while line != '':
            for char in line:
                if char in char_conunter.keys():
                    char_conunter[char] += 1
            line = stream.readline()
        stream.close()
        sortedResult = sorted(char_conunter.items(), key = lambda x : x[1], reverse = True ) 
        print(''.join('[{}] - "{}" -> {} \n'.format(ord(sortedResult[i][0]),sortedResult[i][0],sortedResult[i][1]) for i in range(len(sortedResult)) if sortedResult[i][1] != 0))        
    except IOError as e:
        print("Se produjo un error de E/S:", strerror(e.errno))
        success = False
    return success

def main():
    openTXTchar_by_char(readFilePath() , 'rt')
    
if __name__ == '__main__': main()
