from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# Definindo as telas
class TelaInicial(Screen):
    pass

class Tela1(Screen):
    pass

class Tela2(Screen):
    pass

class Tela3(Screen):
    pass

# Gerenciador de telas
class GerenciadorDeTelas(ScreenManager):
    pass

# Aplicativo principal
class MyApp(App):
    def build(self):
        return Builder.load_file("interface.kv")

if __name__ == "__main__":
    MyApp().run()
