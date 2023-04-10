# Atividade #5: Visão Computacional
##### Laboratório da disciplina Inteligência Artificial e Robótica - Ciência da Computação FEI

## Imagem Castelo
*Código:*
``` python
import  math
import  numpy  as  np
import cv2
import  matplotlib.pyplot  as  plt

#Importa e converta para RGB
img = cv2.imread('./imagens/CASTELO_01.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  

#Convertendo para preto e branco (RGB -> Gray Scale -> BW)
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
a = img_gray.max()
_, thresh = cv2.threshold(img_gray, a/2*1.7, a,cv2.THRESH_BINARY_INV)

tamanhoKernel = 5
kernel = np.ones((tamanhoKernel,tamanhoKernel), np.uint8)
thresh_open = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

#Filtro de ruído (bluring)
img_blur = cv2.blur(img_gray, ksize=(tamanhoKernel,tamanhoKernel))

# Detecção borda com Canny (sem blurry)
edges_gray = cv2.Canny(image=img_gray, threshold1=a/2, threshold2=a/2)

# Detecção borda com Canny (com blurry)
edges_blur = cv2.Canny(image=img_blur, threshold1=a/2, threshold2=a/2)

# contorno
contours, hierarchy = cv2.findContours(
image = thresh,
mode = cv2.RETR_TREE,
method = cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key = cv2.contourArea, reverse = True)
img_copy = img.copy()

final = cv2.drawContours(img_copy, contours, contourIdx = -1,
color = (255, 0, 0), thickness = 2)  

#plot imagens
imagens = [img,img_blur,img_gray,edges_gray,edges_blur,thresh,thresh_open,final]

formatoX = math.ceil(len(imagens)**.5)

if (formatoX**2-len(imagens))>formatoX:
	formatoY = formatoX-1
else:
	formatoY = formatoX
for  i  in  range(len(imagens)):
	plt.subplot(formatoY, formatoX, i + 1)
	plt.imshow(imagens[i],'gray')
	plt.xticks([]),plt.yticks([])
plt.show()
```

*Imagens intermediárias*
**![](https://lh6.googleusercontent.com/WTIGIp3PL4-cm7Ml4aCfs0HgVA0OPPUCZkhRy0sQRi7dGjPtVQ1MSGY-FeTWd2bdK43M8kQcFsU14AZfqmUzj0m8VTvb46Erl2z3MC2k5PxFCYPVI6s-td0jum82pTe2aMEd6kLPigcOSMBDNrcd9g)**

*Imagem final:*
**![](https://lh5.googleusercontent.com/ayOK1QPiPdMUl1M9SGad_H_5b-uur_FO9M7exYcNNsTwIKlSzJNp7o6jq9olkRqgXyfijSxcBz6Lrmwdesoy9Lf1OTEICRzDUsWVStqFUbUat6HY6sCO3gcdET6INRq-LrKvfV904pygTiEXoYVnsEQ)**

## Imagem Avião
*Código:*
```python
import math
import numpy as np
import cv2
import matplotlib.pyplot as plt

#Importa e converta para RGB
img = cv2.imread('./AVIAO_01.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  
#Convertendo para preto e branco (RGB -> Gray Scale -> BW)
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
a = img_gray.max()
_, thresh = cv2.threshold(img_gray, a/2*1.7, a,cv2.THRESH_BINARY_INV)
  
tamanhoKernel = 4
kernel = np.ones((tamanhoKernel,tamanhoKernel), np.uint8)

#Filtro de ruído (bluring)
img_blur = cv2.blur(img_gray, ksize=(2,3))
  
# Detecção borda com Canny (com blurry)
edges_blur = cv2.Canny(image=img_blur, threshold1=a/2, threshold2=a/2)  

# contorno
contours, hierarchy = cv2.findContours(
image = edges_blur,
mode = cv2.RETR_TREE,
method = cv2.CHAIN_APPROX_SIMPLE)

contours = sorted(contours, key = cv2.contourArea, reverse = True)
img_copy = img.copy()
final = cv2.drawContours(img_copy, contours, contourIdx = -1,
color = (255, 0, 0), thickness = 2)  

#plot imagens
imagens = [img,img_gray,img_blur,edges_blur,final]
formatoX = math.ceil(len(imagens)**.5)

if (formatoX**2-len(imagens))>formatoX:
	formatoY = formatoX-1
else:
	formatoY = formatoX
for i in  range(len(imagens)):
	plt.subplot(formatoY, formatoX, i + 1)
	plt.imshow(imagens[i],'gray')
	plt.xticks([]),plt.yticks([])
plt.show()
```
*Imagens intermediárias:*
**![](https://lh4.googleusercontent.com/LX7rcW_szs1RpHo0CtvAhFhEKwM8i1pW4vgVdao5WwTzxgT-oQ0H_D11CHcqNjaiAYTwDjFMscMNenVFyWT5Lv4Pt4GTMAKLE34-54WX_ssu1W-74Okk39YWN7jF6TIlfZEcpwNmG4Ox1WoBQFUNT3g)**

*Imagem final:*
**![](https://lh5.googleusercontent.com/ZSPk42jq4T9djwQLrpswdKImt9iUmUO7_QnmX-bilTfF9ooFI7udARg4L6PVoT4KPAaOKV9b04ob59QqGDyhw8iqmlthlRwfL2CiuZaEnmdFn4IkDtVGmoM-9kQhG_0wfYv_3Ex3QdV92YBUKlgf74M)**