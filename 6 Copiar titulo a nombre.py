import os
import eyed3

def obtener_titulo(ruta_archivo):
    audiofile = eyed3.load(ruta_archivo)
    if audiofile.tag.title:
        # Reemplazar caracteres no deseados en el título
        titulo_limpio = ''.join(c for c in audiofile.tag.title if c.isprintable())
        return titulo_limpio
    else:
        return None

def renombrar_archivos_con_titulo(ruta):
    archivos = os.listdir(ruta)
    archivos_no_modificados = []

    for nombre_archivo in archivos:
        ruta_completa = os.path.join(ruta, nombre_archivo)

        # Verifica si el archivo es un archivo de audio (mp3)
        if nombre_archivo.lower().endswith(".mp3"):
            try:
                titulo = obtener_titulo(ruta_completa)

                if titulo:
                    nuevo_nombre = f'{titulo} - {nombre_archivo}'
                    nueva_ruta = os.path.join(ruta, nuevo_nombre)

                    # Renombrar el archivo
                    os.rename(ruta_completa, nueva_ruta)
                    print(f'Renombrado: {nombre_archivo} -> {nuevo_nombre}')
            except Exception as e:
                archivos_no_modificados.append(nombre_archivo)
                print(f'Error al intentar renombrar {nombre_archivo}: {str(e)}')

    if archivos_no_modificados:
        print("\nArchivos que no pudieron modificarse:")
        for archivo in archivos_no_modificados:
            print(archivo)

# Ruta del directorio que contiene los archivos de audio
ruta_directorio = r'C:\Users\David Quirino\Downloads\4K Video Downloader'

# Llamada a la función para renombrar los archivos
renombrar_archivos_con_titulo(ruta_directorio)