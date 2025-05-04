import webview, os
from datetime import datetime


class Api:
    def show_message(self, message):
        print(message)

    def show_error(selt, error):
        print(f"{datetime.now()} Frontend error: {error}")

    def list_files_in_dir(self, directory_path):
        files = os.listdir(directory_path)
        files = [f for f in files if os.path.isfile(os.path.join(directory_path, f))]
        return files


def main():
    api = Api()
    window = webview.create_window(
        "Простой PyWebview проект", "html/index.html", js_api=api
    )
    webview.start()


if __name__ == "__main__":
    main()
