from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# Dados simulando um banco de dados
itens = []

# Classes para as telas
class TelaMenu(Screen):
    pass

class TelaAdd(Screen):
    def adicionar_item(self, nome):
        global itens
        if nome:
            itens.append(nome)
            self.ids.nome_input.text = ''  # Limpa o campo de input

class TelaList(Screen):
    def on_pre_enter(self):
        self.ids.container.clear_widgets()
        for item in itens:
            self.ids.container.add_widget(ListItem(nome=item))

    def remover_item(self, item):
        global itens
        itens.remove(item)
        self.on_pre_enter()

class ListItem(BoxLayout):
    def __init__(self, nome, **kwargs):
        super().__init__(**kwargs)
        self.ids.item_label.text = nome

    def editar(self, novo_nome):
        if novo_nome:
            global itens
            index = itens.index(self.ids.item_label.text)
            itens[index] = novo_nome
            self.ids.item_label.text = novo_nome

# Gerenciador de telas
class GerenciadorDeTelas(ScreenManager):
    pass

# Carregar os arquivos .kv
Builder.load_file('tela_add.kv')
Builder.load_file('tela_list.kv')

class MyApp(App):
    def build(self):
        return Builder.load_file('menu.kv')

if __name__ == '__main__':
    MyApp().run()
