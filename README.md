# Detecção de Motos com YOLOv5 e OpenCV
# Integrantes: Henzo Puchetti RM555179 / Luann Mariano - RM558548
Este projeto em Python utiliza o modelo pré-treinado YOLOv5 (You Only Look Once) para realizar a detecção automática de motos em vídeos. A aplicação faz uso das bibliotecas PyTorch e OpenCV para processar quadros de vídeo em tempo real e exibir as detecções na tela.


📦 Tecnologias Utilizadas
Python 3.x

PyTorch — Framework para deep learning.

YOLOv5 — Modelo de detecção de objetos.

OpenCV — Processamento de imagens e vídeos.


🚀 Funcionalidades
Carregamento automático do modelo YOLOv5 pré-treinado.

Processamento de vídeo frame a frame.

Detecção de objetos e filtragem específica para o rótulo "motorcycle".

Exibição do vídeo com caixas delimitadoras e probabilidades sobre as motos detectadas.

Encerramento do programa ao pressionar a tecla q.


▶️ Como Executar
Clone o repositório e acesse a pasta do projeto.

Instale as dependências:

bash
Copiar
Editar
pip install torch torchvision
pip install opencv-python
Certifique-se de ter o arquivo de vídeo motos.mp4 na pasta do projeto.
OU altere o código para usar a webcam substituindo 'motos.mp4' por 0.

Execute o script:

bash
Copiar
Editar
python detect_motos.py


⚙️ Estrutura do Código
Carregamento do modelo:
Utiliza torch.hub.load para carregar o modelo yolov5s.

Processamento de vídeo:
Utiliza cv2.VideoCapture para ler um vídeo ou câmera.

Detecção:
Converte os frames para RGB, passa pelo modelo e desenha caixas verdes ao redor das motos detectadas, exibindo a confiança da detecção.

Finalização:
Pressione "Q" para encerrar o programa, liberando os recursos de vídeo.


📝 Observações
O modelo pode ser ajustado para maior precisão utilizando versões maiores do YOLOv5 (yolov5m, yolov5l).

Dependendo do desempenho da sua máquina, pode ser necessário ajustar o parâmetro cv2.waitKey() para melhorar a fluidez ou desacelerar o processamento.
