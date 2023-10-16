import cv2
import os
import datetime

def generate_timestamp_filename(extension=".jpg"):
    # Obtiene la fecha y hora actual
    current_time = datetime.datetime.now()

    # Formatea la fecha y hora como una cadena legible
    timestamp = current_time.strftime("%Y%m%d%H%M%S")

    # Combina la marca de tiempo con la extensión del archivo
    filename = timestamp + extension

    return filename

def get_capture(num_camera=0):

    # Inicializa la cámara
    cap = cv2.VideoCapture(num_camera)  # El número '0' indica la cámara predeterminada

    if not cap.isOpened():
        print("Error: No se puede abrir la cámara.")
        exit()

    # Captura un fotograma de la cámara
    ret, frame = cap.read()

    # Libera la cámara
    cap.release()

    # Cierra todas las ventanas de OpenCV
    cv2.destroyAllWindows()

    if not ret:
        print("Error: No se pudo capturar la imagen.")
        exit()
    else:
        return frame


# Ejemplo de uso:
if __name__ == "__main__":
    save_path = os.path.join('data', 'output')
    
    # Verifica si la carpeta 'data' existe, si no, la crea
    if not os.path.exists('data'):
        os.makedirs('data')

    # Verifica si la carpeta 'data/output' existe, si no, la crea
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    filename = generate_timestamp_filename()
    filename = os.path.join(save_path, filename)

    frame = get_capture()
    try:
        # Guarda la imagen capturada en un archivo
        cv2.imwrite(filename, frame)

        print(f"Imagen capturada y guardada como '{filename}'")
    except:
        print("Falló en la captura")
