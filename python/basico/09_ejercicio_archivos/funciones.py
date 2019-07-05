import unicodedata


def sacar_espacios(texto): 
    texto.strip()
    return texto.replace(" ","")


def eliminarTildes(texto):
    trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
    texto = unicodedata.normalize('NFKC', unicodedata.normalize('NFKD', texto).translate(trans_tab))
    return texto



def generoLosTitulosDeLosArchivos(informacion):
    titulos = []
    periodos = informacion["periodo"]
    dias = informacion["dia"]
    franja_horas =  informacion["franja_hora"]

    for periodo in periodos :
        for dia in dias:
            for franja_hora in franja_horas:
                titulos.append("indice_circulacion_" + periodo + "_" + dia + "_" + franja_hora +"_caba_3857.map")
    return titulos