# ----
# ## Exercicio 2

# Use as imagens **figs/procurado.jpg** e **figs/tripaSeca.png** para criar um cartaz de procurado igual ao apresentado na imagem na imagem **figs/tripaSeca_procurado.png**.

# Você pode aplicar qualquer técnica aprendida na disciplina e qualquer sequência de operações para chegar no resultado esperado. Porém, sugere-se a seguinte sequência:
# - Remova o texto do cartaz usando máscara de cor, conforme ensinado no notebook de operações aritméticas. Porém, em vez de aplicar na imagem inteira, selecione apenas a região onde está o texto para facilitar.
# - Ao remover o texto, ficarão marcas do texto antigo. Para removê-las, aplique algum filtro passa-baixa.
# - Adicione o texto novo usando a função putText da OpenCV
# - Aplique um novo filtro passa-baixa para que a imagem do cartaz fique um pouco borrada de forma a similar a foto do personagem.
# - Aumente a imagem **figs/tripaSeca.png** para o rosto do personagem caber na região adequada da imagem **figs/procurado.jpg**.
# - Aplique equalização no rosto do personagem
# - Adicione o rosto do personagem no cartaz

# Salve a imagem resultante no caminho **figs_resultado/ex02_tripaSeca_procurado.png**


import cv2
import matplotlib.pyplot as plt
import numpy as np

image_background = cv2.imread("AC2/figs/procurado.jpg")
background_rgb = cv2.cvtColor(image_background, cv2.COLOR_BGR2RGB)


def normalize_image(image, crop, threshold, channel, replacement_color):

    cropped_img = image[crop[0] : crop[1], crop[2] : crop[3]]

    # verifica se os pixeeis do canal RGB informado é menor que o threshold
    mask = cropped_img[:, :, channel] < threshold
    cropped_img[mask] = replacement_color

    blurred_img = cv2.GaussianBlur(cropped_img, ksize=(33, 33), sigmaX=14, sigmaY=None)

    image[crop[0] : crop[1], crop[2] : crop[3]] = blurred_img

    return image


imageBlank1 = normalize_image(
    background_rgb,
    crop=(83, 181, 313, 664),
    threshold=140,
    channel=0,
    replacement_color=[243, 231, 217],
)

imageBlank2 = normalize_image(
    imageBlank1,
    crop=(205, 268, 296, 687),
    threshold=140,
    channel=0,
    replacement_color=[243, 231, 217],
)
imageBlank3 = normalize_image(
    imageBlank2,
    crop=(795, 888, 259, 749),
    threshold=140,
    channel=0,
    replacement_color=[233, 217, 201],
)

cv2.putText(
    imageBlank3,
    "PROCURADO",
    (325, 150),
    cv2.FONT_HERSHEY_DUPLEX,
    fontScale=1.8,
    color=(109, 73, 51),
    thickness=6,
)
cv2.putText(
    imageBlank3,
    "VIVO OU MORTO",
    (319, 220),
    cv2.FONT_HERSHEY_DUPLEX,
    fontScale=1.4,
    color=(109, 73, 51),
    thickness=6,
)
cv2.putText(
    imageBlank3,
    "RECOMPENSA R$50000",
    (210, 870),
    cv2.FONT_HERSHEY_DUPLEX,
    fontScale=1.6,
    color=(109, 73, 51),
    thickness=6,
)

image_tripaSeca = cv2.imread("AC2/figs/tripaSeca.png")
image_tripaSeca_RGB = cv2.cvtColor(image_tripaSeca, cv2.COLOR_BGR2RGB)
crop_tripaSeca = image_tripaSeca_RGB[46:198, 350:498]
x, y = 766 - 230, 778 - 292
# Redimensiona a imagem para ter o mesmo tamanho do quadro da imagem de fundo
crop_tripaSeca = cv2.resize(crop_tripaSeca, (x, y))
crop_tripaSeca = cv2.convertScaleAbs(crop_tripaSeca, alpha=1.2, beta=7)
crop_tripaSeca = cv2.GaussianBlur(crop_tripaSeca, ksize=(5, 5), sigmaX=0.5)

imageBlank3[292:778, 230:766] = crop_tripaSeca


plt.axis('off')
plt.imshow(imageBlank3)
plt.savefig("AC2/figs_resultado/ex02_tripaSeca_procurado.png")
