import	cv2

imgOriginal	=	cv2.imread("lena.jpg")
imgTratada	=	cv2.blur(imgOriginal,	(5,5))

cv2.imshow("Imagem Original",	imgOriginal)
cv2.imshow("Imagem Tratada",	imgTratada)

cv2.waitKey(10000)
cv2.destroyAllWindows()