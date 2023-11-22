def create_number(abaco):
    number = 0
    i = 6
    for elemento in abaco:
        cont = 0
        
        for digito in str(elemento):
            if digito == "O":
                cont += 1
            else:
                break
        number += cont * (10 ** i)
        i -= 1
    
    formatted_number = "{:,}".format(number)
    print(formatted_number)
                

abaco = [
    "O---OOOOOOOO",
    "OOO---OOOOOO",
    "---OOOOOOOOO",
    "OO---OOOOOOO",
    "OOOOOOO---OO",
    "OOOOOOOOO---",
    "---OOOOOOOOO"]


create_number(abaco)