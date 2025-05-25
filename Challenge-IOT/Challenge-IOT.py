import torch
import cv2

# Carrega o modelo YOLOv5 pré-treinado
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # ou yolov5m, yolov5l

# Abre o vídeo (ou use 0 para webcam)
cap = cv2.VideoCapture('motos.mp4')

if not cap.isOpened():
    print("Erro ao abrir o vídeo")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Converte de BGR para RGB
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Faz a detecção
    results = model(img_rgb, size=640)

    # Percorre os objetos detectados
    for *box, conf, cls in results.xyxy[0]:
        label = results.names[int(cls)]
        if label == 'motorcycle':
            x1, y1, x2, y2 = map(int, box)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f'{label.upper()} {conf:.2f}', (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Mostra o frame
    cv2.imshow('YOLOv5 - Detecção de Motos', frame)

    # Espera 1 milissegundo (ajuste se quiser desacelerar: ex: waitKey(10) ou (30))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
