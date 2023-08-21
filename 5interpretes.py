import os
from mutagen.easyid3 import EasyID3

ruta = r"C:\Users\David Quirino\Documents\Musica\4K Video Downloader"

def modificar_interprete(ruta):
    for nombre_archivo in os.listdir(ruta):
        ruta_completa = os.path.join(ruta, nombre_archivo)
        
        if os.path.isfile(ruta_completa) and nombre_archivo.endswith(".mp3"):
            nombre, _ = os.path.splitext(nombre_archivo)
            
            partes = nombre.split(" - ")  # Dividir el nombre por el guión
            if len(partes) >= 2:
                interprete = partes[0].replace("_", " ")  # Usar la primera parte como intérprete
                try:
                    audio = EasyID3(ruta_completa)
                    audio["artist"] = interprete
                    audio.save()
                    print(f"Intérprete modificado para: {ruta_completa}")
                except Exception as e:
                    print(f"No se pudieron modificar los metadatos para: {ruta_completa}. Error: {e}")

if __name__ == "__main__":
    modificar_interprete(ruta)