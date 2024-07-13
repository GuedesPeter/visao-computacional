import cv2
import numpy as np

def main():
    video = cv2.VideoCapture('contador-pessoas/area-pessoas.mp4')
    contador = 0
    liberado = False

    while True:
        ret, img = video.read()
        if not ret:
            break

        img = cv2.resize(img, (1100, 720))
        imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        x, y, w, h = 490, 230, 30, 150
        imgTh = cv2.adaptiveThreshold(imgGray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 12)
        kernel = np.ones((8, 8), np.uint8)
        imgDil = cv2.dilate(imgTh, kernel, iterations=2)

        recorte = imgDil[y:y+h, x:x+w]
        brancos = cv2.countNonZero(recorte)

        if brancos > 4000 and liberado == True:
            contador += 1
        if brancos < 4000:
            liberado = True
        else:
            liberado = False

        if liberado == False:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 4)

        cv2.rectangle(imgTh, (x, y), (x + w, y + h), (255, 255, 255), 6)
        cv2.putText(img, str(brancos), (x - 30, y - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
        cv2.rectangle(img, (575, 155), (575 + 88, 155 + 85), (255, 255, 255), -1)
        cv2.putText(img, str(contador), (x + 100, y), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 5)

        # Adiciona a mensagem "Pressione 'Q' para sair" em vermelho no canto superior esquerdo
        cv2.putText(img, "Pressione 'Q' para sair!", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow('video original', img)

        # Aguarda 20 milissegundos para a próxima iteração do loop
        key = cv2.waitKey(20)

        # Verifica se a tecla 'q' foi pressionada para sair do loop
        if key == ord('q'):
            break

    # Libera o vídeo e fecha todas as janelas abertas do OpenCV
    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
