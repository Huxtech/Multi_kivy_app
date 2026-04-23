from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class SecondApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        label = Label(text="This is the nested app")
        btn = Button(text="Go back to first app")
        btn.bind(on_press=self.go_back)
        layout.add_widget(label)
        layout.add_widget(btn)
        return layout

    def go_back(self, instance):
        self.stop()

SecondApp().run()