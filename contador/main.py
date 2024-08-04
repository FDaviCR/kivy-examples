from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock


class CountdownApp(App):
    def build(self):
        self.counter = 10  # Valor inicial do contador
        self.is_counting = False  # Indicador para verificar se a contagem está ativa

        layout = BoxLayout(orientation='vertical')
        self.label = Label(text=str(self.counter))
        self.button = Button(text="Iniciar contagem regressiva")

        self.button.bind(on_press=self.start_countdown)

        layout.add_widget(self.label)
        layout.add_widget(self.button)

        return layout

    def start_countdown(self, instance):
        if not self.is_counting:
            self.is_counting = True
            self.button.disabled = True  # Desativa o botão durante a contagem
            Clock.schedule_interval(self.update_countdown, 1)

    def update_countdown(self, dt):
        if self.counter > 0:
            self.counter -= 1
            self.label.text = str(self.counter)
        else:
            self.label.text = "Tempo esgotado!"
            Clock.unschedule(self.update_countdown)  # Para a contagem
            self.button.disabled = False  # Habilita o botão novamente
            self.is_counting = False  # Reseta o indicador de contagem


if __name__ == "__main__":
    CountdownApp().run()
