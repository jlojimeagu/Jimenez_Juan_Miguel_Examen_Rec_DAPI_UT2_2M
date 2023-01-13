def check_DGT(documento):
    import csv
    with open(documento, encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",", dialect=csv.excel)
        for persona in reader:
            print(persona)
            datos = persona
            nombre = check_username(datos[0], datos[1])
            dni = check_nif(datos[2])
            telefono = check_phone(datos[3])
            total = calculate_bill(datos[5], datos[6], datos[7])
            if datos[3] != 'Teléfono':
                num = datos[3].split(')')
                country = num[0].split('(')
                pais = countries_dict[country[1]]
                check = [nombre, dni, telefono, pais, total]
            else:
                pais = 'Pais'
                check = [nombre, dni, telefono, pais, total]
            escrito = open(documento, 'w', encoding='utf-8')
            escrito.writelines(str(check))




countries_dict = {'30': 'Grecia', '33': 'Francia', '34': 'España', '351': 'Portugal', '380': 'Ucrania', '39': 'Italia',
                  '41': 'Suiza', '44': 'Reino Unido', '49': 'Alemania', '7': 'Rusia'}
nif_dict = {'0': 'T', '1': 'R', '2': 'W', '3': 'A', '4': 'G', '5': 'M', '6': 'Y', '7': 'F', '8': 'P', '9': 'D',
            '10': 'X', '11': 'B', '12': 'N', '13': 'J', '14': 'Z', '15': 'S', '16': 'Q', '17': 'V', '18': 'H',
            '19': 'L', '20': 'C', '21': 'K', '22': 'E'}


def check_username(nombre, apellido):
    """
    :param nombre: el nombre de la persona
    :param apellido: el apellido o apellidos.
    :return:retorna su respectivo dato con la inicial en
    mayuscula
    """
    return nombre.title(), apellido.title()


def check_nif(nif):
    """
    :param nif: numero de identificacion
    :return: correccion del numero de identificacion
    """
    if nif == 'DNI':
        return nif
    else:
        dni = str(nif)
        num = dni[0:8]
        check = int(num) % 23
        good_num = nif_dict[str(check)]
    return num + good_num


def check_phone(num_phone):
    """
    :param num_phone: numero de telefono en formato erroneo
    :return: forma correcta de exprecion de numero telefonico
    """
    if num_phone == 'Teléfono':
        return num_phone
    else:
        num = num_phone.split(')')
        codig = num[0]
        numer0 = num[1]
        cod = codig.split('(')
        numero = numer0.split('-')
        phone = '+' + cod[1] + '-' + numero[0] + numero[1]
    return phone

def calculate_bill(multa1,multa2,multa3):
    if multa1 == 'Multas Radar' or multa2 == 'Multas ITV' or multa3 == 'Multas Estupefacientes':
        return 'Total'
    bill = int(multa1) + int(multa2) + int(multa3)
    return bill

print(check_DGT('Juan Miguel Jiménez Aguas - DGT'))