from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock


class CountdownApp(App):
    def build(self):
        self.counter = 0  # Valor inicial do contador (em segundos)
        self.is_counting = False  # Indicador para verificar se a contagem está ativa

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Entrada de texto para definir o tempo inicial em segundos
        self.time_input = TextInput(hint_text='Digite o tempo em segundos', multiline=False, input_filter='int')
        layout.add_widget(self.time_input)

        # Label para exibir o tempo restante
        self.label = Label(text="Tempo restante: 00:00")
        layout.add_widget(self.label)

        # Botão para iniciar a contagem regressiva
        self.button = Button(text="Iniciar contagem regressiva")
        self.button.bind(on_press=self.start_countdown)
        layout.add_widget(self.button)

        return layout

    def start_countdown(self, instance):
        if not self.is_counting:
            try:
                self.counter = int(self.time_input.text)
                if self.counter > 0:
                    self.is_counting = True
                    self.button.disabled = True  # Desativa o botão durante a contagem
                    Clock.schedule_interval(self.update_countdown, 1)
                    self.time_input.disabled = True  # Desativa a entrada de texto durante a contagem
            except ValueError:
                self.label.text = "Por favor, insira um número válido."

    def update_countdown(self, dt):
        if self.counter > 0:
            self.counter -= 1
            minutes, seconds = divmod(self.counter, 60)
            self.label.text = f"Tempo restante: {minutes:02}:{seconds:02}"
        else:
            self.label.text = "Tempo esgotado!"
            Clock.unschedule(self.update_countdown)  # Para a contagem
            self.button.disabled = False  # Habilita o botão novamente
            self.time_input.disabled = False  # Habilita a entrada de texto novamente
            self.is_counting = False  # Reseta o indicador de contagem


if __name__ == "__main__":
    CountdownApp().run()
