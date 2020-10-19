import	cv2
from tkinter import *
import tkinter as tk
import tkinter.filedialog as fdlg
import tkinter.scrolledtext as tkst
from tkinter.constants import END,HORIZONTAL, VERTICAL, NW, N, E, W, S, SUNKEN, LEFT, RIGHT, TOP, BOTH, YES, NE, X, RAISED, SUNKEN, DISABLED, NORMAL, CENTER
from tkinter import messagebox
from PIL import Image, ImageFilter



class TesteDialogs(object):
	
	appname= "Computação Gráfica e Processamento de Imagens - Andressa Marçal"
	frameWidth      = 600
	frameHeight     = 700
	padx            = 5
	pady            = 5


	def __init__(self, **kw):

		self.root = tk.Tk()

		T = Text(self.root, height=10, width=85)
		T.pack()
		T.insert(END, "Bem-vindos!\n\nPrograma desenvolvido para a disciplina de Computação Grafica, pela aluna Andressa Marçal.\n\nEscolha a opção FILTROS, para selecionar o filtro que deverá ser aplicado na imagem abaixo.\n\nOu clique em Opções>Sair, para sair do programa.")

		imagem = tk.PhotoImage(file="lena.png")
		w = tk.Label(self.root, image=imagem)
		w.imagem = imagem
		w.pack()

		self.root.title(self.appname)

		self.root.geometry('%dx%d' % (self.frameWidth, self.frameHeight))

		self.createMenuBar()

		self.minhaTela = tk.Frame(self.root)
		self.minhaTela.pack( padx= "5", pady="5",expand=1, fill="both")

		self.editor = tkst.ScrolledText(master = self.minhaTela,wrap= tk.WORD,width  = 20,height = 10)
		self.editor.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)


	def createMenuBar(self):

		menubar = tk.Menu(self.root)

		filemenu = tk.Menu(menubar, tearoff=0)
		filemenu.add_command(label="Sair", command=self.root.quit)
		menubar.add_cascade(label="Opções", menu=filemenu)

		showFileDialogsmenu = tk.Menu(menubar, tearoff=0)
		showFileDialogsmenu.add_command(label="Filtro Media", command=self.testeOpenFile)
		showFileDialogsmenu.add_command(label="Filtro Mediana", command=self.testeOpenFileName)
		showFileDialogsmenu.add_command(label="Histograma", command=self.testeAsksaveasfile)
		
		menubar.add_cascade(label="Filtros", menu= showFileDialogsmenu)


		self.root.config(menu=menubar)

	def testeOpenFile(self):

		imgOriginal	=	cv2.imread("lena2.jpg")
		imgTratada	=	cv2.blur(imgOriginal,	(5,5))

		cv2.imshow("Imagem Original",	imgOriginal)
		cv2.imshow("Imagem Tratada",	imgTratada)
		
		cv2.waitKey(10000)
		cv2.destroyAllWindows()


	def testeOpenFileName(self):

		imgOriginal	=	cv2.imread("lena2.jpg")
		imgTratada	=	cv2.medianBlur(imgOriginal,	5)

		cv2.imshow("Original",	imgOriginal)
		cv2.imshow("Tratada",	imgTratada)
		
		cv2.waitKey(10000)
		cv2.destroyAllWindows()
	

	def testeAsksaveasfile(self):
		
		imagem	=	cv2.imread("lena2.jpg",	0)

		totalPixelsPreto	=	0
		totalPixelsBranco	=	0

		for	x	in	range(0,	499):
			
			for	y	in	range(0,	499):
				
				if	imagem[x,y]	==	255:
					totalPixelsBranco	+=	1
				
				else:
					totalPixelsPreto	+=	1
		
		janela = tk.Tk()
		lb1 = Label(janela, text='Quantidade de Pixels Preto na imagem = \n\n' + str(totalPixelsPreto))
		lb2 = Label(janela, text='\nQuantidade de Pixels Brancos na imagem = \n\n' + str(totalPixelsBranco))
		
		lb1.grid(row=1000, column=1000)
		lb2.grid(row=2000, column=1000)

		janela.geometry('500x200+-600x200')


	def execute(self):
		self.root.mainloop()



def main(args):

	appProc=  TesteDialogs()
	appProc.execute()
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))