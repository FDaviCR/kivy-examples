from kivy.config import Config
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

# Configurar a janela para ser redimensionável e maximizar ao iniciar
Config.set('graphics', 'resizable', True)  # Permitir que a janela seja redimensionável
Config.set('graphics', 'borderless', False)  # Garantir que tenha borda para maximizar/minimizar
Config.set('graphics', 'fullscreen', 'fake')  # "fake" mantém a barra de tarefas visível

class MyApp(App):
    def build(self):
        # Inicializar a janela maximizada
        Window.maximize()

        # Layout da aplicação
        layout = BoxLayout(orientation='vertical')

        # Adicionar componentes à interface
        label = Label(text="Aplicação Maximizada", font_size=30)

        layout.add_widget(label)

        return layout

    def close_app(self, instance):
        # Função para fechar a aplicação
        App.get_running_app().stop()

if __name__ == "__main__":
    MyApp().run()
