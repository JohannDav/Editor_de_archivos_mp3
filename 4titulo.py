import os
from mutagen.easyid3 import EasyID3

ruta = r"C:\Users\David Quirino\Documents\Musica\4K Video Downloader"

def modificar_metadatos(ruta):
    for nombre_archivo in os.listdir(ruta):
        ruta_completa = os.path.join(ruta, nombre_archivo)
        
        if os.path.isfile(ruta_completa) and nombre_archivo.endswith(".mp3"):
            nombre, _ = os.path.splitext(nombre_archivo)
            
            try:
                audio = EasyID3(ruta_completa)  # Cargar los metadatos del archivo
                audio["title"] = nombre.replace("_", " ")  # Modificar el título en los metadatos
                audio.save()  # Guardar los cambios en los metadatos
                print(f"Metadatos modificados para: {ruta_completa}")
            except Exception as e:
                print(f"No se pudieron modificar los metadatos para: {ruta_completa}. Error: {e}")

if __name__ == "__main__":
    modificar_metadatos(ruta)