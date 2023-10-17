import cv2
import os

def get_video_capture(num_camera=0, output_path='data/output/video.mp4'):
    # Inicializa la cámara
    cap = cv2.VideoCapture(num_camera)  # El número '0' indica la cámara predeterminada

    if not cap.isOpened():
        print("Error: No se puede abrir la cámara.")
        exit()

    # Define el codificador para el archivo de salida
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (640, 480))  # Puedes ajustar la resolución y la velocidad de fotogramas

    while True:
        # Captura un fotograma de la cámara
        ret, frame = cap.read()

        if not ret:
            print("Error: No se pudo capturar el fotograma.")
            break

        # Muestra el fotograma en una ventana
        cv2.imshow('Video', frame)

        # # Guarda el fotograma en el archivo de video
        # out.write(frame)

        # Presiona 'q' para salir del bucle
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libera la cámara y cierra la ventana
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    save_path = os.path.join('data', 'output')
    
    # Verifica si la carpeta 'data' existe, si no, la crea
    if not os.path.exists('data'):
        os.makedirs('data')

    # Verifica si la carpeta 'data/output' existe, si no, la crea
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    get_video_capture()
