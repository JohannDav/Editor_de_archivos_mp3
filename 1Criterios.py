import os

def rename_files_in_directory(directory, artist_keywords, words_to_remove, prefix):
    for filename in os.listdir(directory):
        if filename.endswith(".mp3"):  # Modifica la extensión según sea necesario
            for artist_keyword in artist_keywords:
                if artist_keyword.lower() in filename.lower():
                    new_filename = filename
                    for word in words_to_remove:
                        new_filename = new_filename.replace(word, "")
                    new_filename = prefix + new_filename.replace(".mp3", "") + ".mp3"
                    os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
                    break  # No es necesario seguir buscando en las otras palabras clave

if __name__ == "__main__":
    # Edita la ruta del directorio aquí
    directory_path = r"C:\Users\David Quirino\Documents\Musica\4K Video Downloader\Modificar"
    
    # Edita las palabras clave del artista aquí (hasta tres)
    artist_keywords = ["PalabraClave1", "PalabraClave2", "PalabraClave3"]
    
    # Edita las palabras para eliminar aquí (hasta tres)
    words_to_remove = ["Palabra1", "Palabra2", "Palabra3"]
    
    # Edita el prefijo aquí
    prefix = "Prefijo - "

    # No es necesario cambiar nada más a partir de aquí
    rename_files_in_directory(directory_path, artist_keywords, words_to_remove, prefix)
    print("Proceso completado.")

    #Hola, soy David. Si vas a usar este código te recomiendo algunas cosas:
    # Se muy epecífico con las palabras a eliminar "Incluyer mayúsculas, minúsculas y espacios".
    # NUNCA dejes un espacio en blanco como """" porque te va a arruinar todo.
    # Guarda este archivo .py en la carpeta donde esten los archivos a modificar.
    # No olvides poner la ruta de manera correcta (recomiendo un ctrl + c y ctrl + v).