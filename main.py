import os

#lista_musica = []

arquivos_salvos = []

def nomear_arquivos(pasta):
    lista_arquivos = os.listdir(pasta)
    for arquivo in lista_arquivos:
        if ".ogg" in arquivo or ".mp4" in arquivo:
            if ".ogg" in arquivo:
                nome_musica = arquivo.split()[-1].replace(".ogg", "")
            else:
                nome_musica = arquivo.split()[-1].replace(".mp4", "")
            nome_musica = nome_musica.replace("_", " ")
            arquivos_salvos.append(nome_musica)
        elif ".txt" in arquivo or ".toml" in arquivo or ".usm" in arquivo or ".tga" in arquivo or ".bin" in arquivo or ".farc" in arquivo or ".dsc" in arquivo or ".tga" in arquivo or ".dll" in arquivo or ".gif" in arquivo or ".jpg" in arquivo or ".png" in arquivo:
            pass
        elif ".ogg" not in arquivo or ".mp4" not in arquivo:
            nomear_arquivos(f'{pasta}/{arquivo}')

#nomear_arquivos("Arquivos")
#print(arquivos_salvos)

#def nomear_oq_falta():
    #for musica in lista_musica:
        #if musica not in arquivos_salvos:
            #print("Falta o arquivo: "+musica)
