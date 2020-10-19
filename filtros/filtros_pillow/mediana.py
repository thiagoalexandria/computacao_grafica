from PIL import Image, ImageFilter

try:
    #abre imagem 
    imagem = Image.open('lena.jpg')

    #aplicando filtro mediana 3x3 e salvando nova imagem com filtro aplicado 
    filtro_mediana = imagem.filter(ImageFilter.MedianFilter(3))
    filtro_mediana.save('lena_filtromediana.jpg')

    #exibindo imagem antiga e imagem tratada
    imagem.show()
    filtro_mediana.show()

except:
    print("Não foi possível carregar a imagem selecionada.")