from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        # Criar um layout vertical
        self.layout = BoxLayout(orientation='vertical')

        # Criar botões
        self.add_button = Button(text='Adicionar Botão')
        self.remove_button = Button(text='Remover Botão')
        
        # Associar os botões às funções
        self.add_button.bind(on_release=self.add_widget)
        self.remove_button.bind(on_release=self.remove_widget)
        
        # Adicionar os botões ao layout
        self.layout.add_widget(self.add_button)
        self.layout.add_widget(self.remove_button)

        return self.layout

    def add_widget(self, instance):
        # Adicionar um novo botão ao layout
        self.new_button = Button(text='Novo Botão')
        self.layout.add_widget(self.new_button)

    def remove_widget(self, instance):
        # Remover o novo botão do layout se ele existir
        if self.new_button:
            self.layout.remove_widget(self.new_button)
            self.new_button = None  # Opcional: Para evitar remoções repetidas

if __name__ == '__main__':
    MyApp().run()
