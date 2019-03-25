import cv2
import numpy as np

# Leitura das Imagens
src = cv2.imread("input/airplane.jpg")
dst = cv2.imread("input/sky.jpg")

# Criando a mascara do obejeto
mask = np.zeros(src.shape,src.dtype)
poly = np.array([[4,80],[30,54],[151,63],[254,37],[298,90],[272,134],[43,122]],np.int32)
cv2.fillPoly(mask, [poly],  (255,255,255))
#sobrepor o objeto

# Definindo local do objeto
place = (200,100)
#place = (int(dst.shape[1]/2),

# Clone seamlessly.
output_normal = cv2.seamlessClone(src,dst,mask,place,cv2.NORMAL_CLONE)
output_mixed = cv2.seamlessClone(src, dst,mask, place, cv2.MIXED_CLONE)
output_monochrome_transfer = cv2.seamlessClone(src,dst, mask,place, cv2.MONOCHROME_TRANSFER)

resize = lambda img: cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))
# Mostar os resultados

cv2.imshow("sobreposto", resize(src))
cv2.imshow("fundo", resize(dst))
cv2.imshow("output_normal", resize(output_normal))
cv2.imshow("output_mixed", resize(output_mixed))
cv2.imshow("output_monochrome", resize(output_monochrome_transfer))

cv2.waitKey(0)
