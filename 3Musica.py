import os

ruta = r'C:\Users\David Quirino\Documents\Musica\4K Video Downloader'
palabra_clave = 'Keyblade'

# Obtener la lista de archivos en la ruta
archivos = os.listdir(ruta)

for nombre_archivo in archivos:
    if palabra_clave in nombre_archivo:
        nuevo_nombre = f'Keyblade - {nombre_archivo}'
        vieja_ruta = os.path.join(ruta, nombre_archivo)
        nueva_ruta = os.path.join(ruta, nuevo_nombre)
        
        # Renombrar el archivo
        os.rename(vieja_ruta, nueva_ruta)
        print(f'Renombrado: {nombre_archivo} -> {nuevo_nombre}')