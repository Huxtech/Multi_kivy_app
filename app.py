from kivy.app import App
from kivy.uix.button import Button

from jnius import autoclass

PythonActivity = autoclass('org.kivy.android.PythonActivity')
Intent = autoclass('android.content.Intent')
String = autoclass("java.lang.String")

class Main(App):
    def build(self):
        btn = Button(text="Launch nested app")
        btn.bind(on_press=self.open_activity)
        return btn

    def open_activity(self, instance):
        activity = PythonActivity.mActivity
        intent = Intent(activity, PythonActivity)
        intent.putExtra("entrypoint", String("nested_app.py"))
        activity.startActivity(intent)

