from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Clique no botão")
        button = Button(text="Clique aqui")
        button.bind(on_press=self.on_button_press)

        layout.add_widget(self.label)
        layout.add_widget(button)

        return layout

    def on_button_press(self, instance):
        self.label.text = "Hello World!"


if __name__ == "__main__":
    MyApp().run()
