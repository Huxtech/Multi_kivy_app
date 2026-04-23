import os
from jnius import autoclass
from android import mActivity  # type: ignore
from android.runnable import run_on_ui_thread  # type: ignore

ClientActivity = autoclass("org.huxtech.client.ClientActivity")
Intent = autoclass("android.content.Intent")
Uri = autoclass("android.net.Uri")

AppStorageDir = os.path.join(mActivity.getFilesDir().getAbsolutePath(), "app")


@run_on_ui_thread
def launch_client_activity(entrypoint_path: str) -> None:
    uri = Uri.parse("file://" + entrypoint_path)

    intent = Intent(mActivity.getApplicationContext(), ClientActivity)
    intent.setData(uri)
    intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_MULTIPLE_TASK)
    mActivity.startActivity(intent)
