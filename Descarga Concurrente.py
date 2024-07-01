import urllib.request
import threading

# Lista de URLs
urls = [    
    'https://d.winrar.es/d/103z1719721454/ZhBPjprONK6v13Ya1J8Scg/winrar-x64-701es.exe',
    'https://garesaintsauveur.lille3000.com/data/json/info.json',
    
    #Muy Pesado
    #'https://download.virtualbox.org/virtualbox/7.0.18/VirtualBox-7.0.18-162988-Win.exe'
    
]

def descargar_archivo(url):
    # Función para descargar un archivo desde una URL usando urllib
    try:
        nombre_archivo = url.split('/')[-1]
        urllib.request.urlretrieve(url, nombre_archivo)
        print(f'Descargado {url} correctamente')
    except Exception as e:
        print(f'Error al descargar {url}: {str(e)}')

def descargar_concurrente(urls):
    # Función para descargar archivos concurrentemente
    threads = []
    for url in urls:
        thread = threading.Thread(target=descargar_archivo, args=(url,))
        threads.append(thread)
        thread.start()
    
    # Esperar a que todos los hilos terminen
    for thread in threads:
        thread.join()
    
    print('Descarga completa')

if __name__ == '__main__':
    descargar_concurrente(urls)
