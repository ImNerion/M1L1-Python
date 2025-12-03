meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "FUNAR": "Cancelar o desacreditar publicamente a alguien, generalmente en redes sociales",
            "BRO": "Forma de referirse a un amigo cercano.",
            "XD": "Manera de representar risa textualmente",
            "RANDOM": "Algo aleatorio o al azar",
            "GLOW UP": "Una mejora notoria en la apariencia",
            "POV": "Se usa para referirse al punto de vista de algo o alguien",
            "SYBAU":"Manera agresiva o irrespetuosa para mandar a callar",
            "AESTHETIC": "Relacionado con la estética o un estilo visual particular y agradable"
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Parece que esa palabra no esta en este diccionario, Revisa que este bien escrito o intenta con otra")
