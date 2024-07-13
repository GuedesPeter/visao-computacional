# Autor: Paulo Eduardo Guedes Peter

## Projeto de Inteligência Artificial - Contador de Pessoas

Este projeto trata-se de um contador de pessoas.
Ao analisar um vídeo, a IA identifica a contagem de pessoas a partir de um ponto específico.

### Para rodar o projeto:

- Você deve instalar as bibliotecas Opencv e Numpy

    ```bash
   pip install opencv-python numpy
   ```

## Explicação das principais funcionalidades:
Importação de bibliotecas: import cv2 importa a biblioteca OpenCV e import numpy as np importa a biblioteca numpy para manipulação de arrays.

Inicialização do vídeo: video = cv2.VideoCapture('escalator.mp4') abre o arquivo de vídeo 'escalator.mp4' para leitura.

Loop principal (while True): Este loop lê continuamente cada frame do vídeo, processa-o e exibe-o.

### Processamento de imagem:

Redimensionamento: img = cv2.resize(img, (1100, 720)) redimensiona o frame para 1100x720 pixels.

Conversão para escala de cinza: imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) converte o frame para escala de cinza.

Threshold adaptativo: cv2.adaptiveThreshold(imgGray, ...) aplica um método de threshold adaptativo para segmentar a imagem em áreas brancas e pretas.

Dilatação: cv2.dilate(imgTh, kernel, iterations=2) aumenta a intensidade dos pixels brancos na imagem binarizada para facilitar a detecção de contornos.

### Detecção de pessoas:

Contagem de pixels brancos: 
brancos = cv2.countNonZero(recorte) conta o número de pixels brancos na região de interesse.

Lógica de contagem: Baseado na quantidade de pixels brancos, decide se uma pessoa está presente na região.

### Visualização:

Desenho de retângulos e texto: 

cv2.rectangle, cv2.putText são usados para desenhar retângulos coloridos ao redor da região de interesse e para exibir informações como contagem de pessoas e número de pixels brancos.

### Exibição do resultado:

cv2.imshow('video original', img) mostra o frame processado com sobreposições na tela.

cv2.waitKey(20) espera 20 milissegundos antes de processar o próximo frame.

