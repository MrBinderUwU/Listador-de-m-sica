import os

#lista_musica = []

arquivos_salvos = []

def nomear_arquivos(pasta):
    lista_arquivos = os.listdir(pasta)
    for arquivo in lista_arquivos:
        if ".ogg" in arquivo or ".mp4" in arquivo or ".mp3" in arquivo:
            if ".ogg" in arquivo:
                nome_musica = arquivo.replace(".ogg", "")
            elif ".mp4" in arquivo:
                nome_musica = arquivo.replace(".mp4", "")
            else:
                nome_musica = arquivo.replace(".mp3", "")
            nome_musica = nome_musica.replace("_", " ")
            arquivos_salvos.append(nome_musica)
        elif ".txt" in arquivo or ".toml" in arquivo or ".usm" in arquivo or ".tga" in arquivo or ".bin" in arquivo or ".farc" in arquivo or ".dsc" in arquivo or ".tga" in arquivo or ".dll" in arquivo or ".gif" in arquivo or ".jpg" in arquivo or ".png" in arquivo or ".ini" in arquivo or ".zip" in arquivo or ".exe" in arquivo or ".pdf" in arquivo or ".md" in arquivo or ".docx" in arquivo or ".htm" in arquivo or ".csv" in arquivo or ".jpeg" in arquivo or ".html" in arquivo:
            pass
        elif ".ogg" not in arquivo or ".mp4" not in arquivo or "mp3" not in arquivo:
            nomear_arquivos(f'{pasta}/{arquivo}')

#nomear_arquivos("Arquivos")
#print(arquivos_salvos)

#def nomear_oq_falta():
    #for musica in lista_musica:
        #if musica not in arquivos_salvos:
            #print("Falta o arquivo: "+musica)
