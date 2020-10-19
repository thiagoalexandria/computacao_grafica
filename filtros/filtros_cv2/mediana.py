import	cv2

imgOriginal	=	cv2.imread("lena.jpg")
imgTratada	=	cv2.medianBlur(imgOriginal,	5)

cv2.imshow("Original",	imgOriginal)
cv2.imshow("Tratada",	imgTratada)

cv2.waitKey(10000)
cv2.destroyAllWindows()