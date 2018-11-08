from io import BytesIO
from editor import ed
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.core.image import Image as aImage
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, RiseInTransition, FadeTransition

Window.clearcolor = 0.3, 0.1, 0, 1 #deixa a janela azul

Builder.load_file('kvlang.kv')#carrega o arquivo kv

class Geral():#classe para mudar a tela
	def trocar(self, nome_tela, tipo_transicao='Slide', sentido_da_imagem='up'):
		if (tipo_transicao == 'Slide'):
			self.manager.transition = FadeTransition()
		else:
			self.manager.transition = RiseInTransition()
		self.manager.transition.direction = sentido_da_imagem
		self.manager.current = nome_tela

class TelaInicial(Screen, Geral):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		Window.bind(on_dropfile=self.soltou)

	def alterar_mensagem(self, texto):
		lb = self.ids.mensagem
		lb.text = texto

	def soltou(self, window, caminho_arquivo):
		ca = caminho_arquivo.decode('utf-8')

		if (ed.load(ca) == False):
			self.alterar_mensagem('tente novamente')
		else:
			tela_edicao = self.manager.get_screen('tela_edicao')
			tela_edicao.exibir_imagem()
			self.trocar('tela_edicao')

class TelaEdicao(Screen, Geral):
	def exibir_imagem(self):
		area_imagem = self.ids.area_imagem
		area_imagem.clear_widgets()
		img_buffer = BytesIO()
		ed.img.save(img_buffer, format=ed.img_formato)
		img_buffer.seek(0)

		co = aImage(img_buffer, ext=ed.img_formato.lower())
		textura = co.texture

		img_buffer.close()

		img = Image()
		img.texture = textura

		area_imagem.add_widget(img)

	def girar_anti_horario(self):
		ed.rotate('anti_horario')
		self.exibir_imagem()
       
	def girar_horario(self):
 		
		ed.rotate('horario')
		
		self.exibir_imagem()

	def preto_e_branco(self):
		ed.preto_branco()
		self.exibir_imagem()
	def esp(self):
		ed.espelhar()
		self.exibir_imagem()

	def cancelar(self):
		tela_inicial = self.manager.get_screen('tela_inicial')
		tela_inicial.alterar_mensagem('insira uma imagem aqui')
		self.trocar('tela_inicial', 'No')
		ed.reset()

telinha = ScreenManager()
telinha.add_widget(TelaInicial(name='tela_inicial'))
telinha.add_widget(TelaEdicao(name='tela_edicao'))

class Programa(App):
	title = 'editor'
	def build(self):
		return telinha
if __name__ == '__main__':
	Programa().run()
