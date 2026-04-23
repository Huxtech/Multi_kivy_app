from app import Main
from jnius import autoclass

activity = autoclass("org.kivy.android.PythonActivity").mActivity
intent = activity.getIntent()
entrypoint = intent.getStringExtra("entrypoint")

if __name__ == '__main__':
    if entrypoint:
        import runpy
        runpy.run_path(entrypoint, run_name="__main__")
    else:
        Main().run()