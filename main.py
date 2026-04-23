import os

from kivy import platform
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder

if platform == "android":
    from libs.android import launch_client_activity, AppStorageDir


AppKV = """
Screen:
    Button:
        text: "Launch"
        size_hint: None, None
        height: dp(48)
        width: dp(128)
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        on_press:
            app.launch()
"""


class Main(App):

    def __init__(self, **kwargs):
        Window.clearcolor = [1, 1, 1, 1]
        super(Main, self).__init__(**kwargs)

    def build(self):
        return Builder.load_string(AppKV)

    def launch(self, *args) -> None:
        if platform == "android":
            launch_client_activity(
                os.path.abspath(os.path.join(AppStorageDir, "nested_app.py"))
            )


if __name__ == "__main__":
    Main().run()
