from PIL import Image, ImageFilter

try:
    original = Image.open("lelna.png")

    img_filtromedia = original.filter(ImageFilter.BLUR)

    original.show()
    img_filtromedia.show()

    img_filtromedia.save("lena_filromedia.png")

except:
    print ("Não foi possível carregar a imagem selecionada.")