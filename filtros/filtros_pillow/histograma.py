from PIL import Image
 
# abre imagem
imagem = Image.open("lena.jpg")
# tamanho da imagem
largura, altura = imagem.size
# calcula a media de pixels
montante = largura * altura
 

total = 0
# imagem preto e branca
bw_imagem = Image.new('L', (largura, altura), 0)
# bitmap imagem
bm_imagem = Image.new('1', (largura, altura), 0)
 
for h in range(0, altura):
    for w in range(0, largura):
        r, g, b = imagem.getpixel((w, h))
 
        escalacinza = int((r + g + b) / 3)
        total += escalacinza
 
        bw_imagem.putpixel((w, h), escalacinza)
 
# media de escala de cinza
avg = total / montante
 
preto = 0
branco = 1

# percorre a matriz linhas e colunas 
for h in range(0, altura):
    for w in range(0, largura):
        v = bw_imagem.getpixel((w, h))
 
        if v >= avg:
            bm_imagem.putpixel((w, h), branco)
        else:
            bm_imagem.putpixel((w, h), preto)

bw_imagem.show()
bm_imagem.show()