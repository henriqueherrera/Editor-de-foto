from os import path
from PIL import Image, ImageEnhance

class Editor():
	img = None
	img_formato = None
	img_local = None
	img_nome = None
	img_ext = None
	img_cp = None
	x = 0
	def reset(self):
		self.img = None
		self.img_formato = None
		self.img_local = None
		self.img_nome = None
		self.img_ext = None

	def load(self, imagem):
		try:
			self.img = Image.open(imagem)
			self.img_cp = self.img.copy()
			self.img_formato = self.img.format
			self.img_local = path.dirname(path.realpath(imagem))
			self.img_nome, self.img_ext = path.splitext(path.basename(imagem))
			return True
		except:
			return False
	def espelhar(self):
		self.img = self.img.transpose(Image.FLIP_LEFT_RIGHT)

	def rotate(self, sentido='horario', angulo=90):
		if (sentido == 'horario'):
			self.img = self.img.rotate(angulo * -1, expand=True)
		elif (sentido == 'anti_horario'):
			self.img = self.img.rotate(angulo, expand=True)

	def preto_branco(self):
		if self.x == 0:

			conversor = ImageEnhance.Color(self.img)
			self.img = conversor.enhance(0)
			self.x+=1
		else:
			self.img = self.img_cp
			self.x = 0

	def salvar(self, local, nome_imagem):
		ln = local + '/' + nome_imagem + self.img_ext
		self.img.save(ln, self.img_formato)
		self.resetar()
ed = Editor()
