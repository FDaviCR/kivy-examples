from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class CenteredApp(App):
    def build(self):
        # Define o tamanho da janela em pixels
        app_width, app_height = 800, 600
        Window.size = (app_width, app_height)

        # Calcula a posição para centralizar a janela
        screen_width, screen_height = Window.system_size
        Window.left = (screen_width - app_width) / 2 
        Window.top = (screen_height - app_height) / 2 + 25

        # Cria um layout e um label para exibir uma mensagem
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        label = Label(text="Esta janela está centralizada na tela")
        layout.add_widget(label)

        return layout

if __name__ == "__main__":
    CenteredApp().run()
