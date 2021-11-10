def counter(answer):

    return print(f"""Que buena explicación, sólo haz necesitado {len(answer.split())} palabras y te he entendido perfectamente!""")
#convertí a string para que no tire error si ponen un número, booleano u otro tipo de dato (aunque siempre será 1)
    
thought=str(input("En qué estás pensando?"))
counter(thought)