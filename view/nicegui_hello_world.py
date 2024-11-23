from fastapi import FastAPI

from nicegui import app, ui


def init(fastapi_app: FastAPI) -> None:
    @ui.page('/')
    def show():
        ui.label('Hello, FastAPI!')

        # NOTE dark mode will be persistent for each user across tabs and server restarts
        ui.dark_mode().bind_value(app.storage.user, 'dark_mode')
        ui.checkbox('dark mode').bind_value(app.storage.user, 'dark_mode')

    ui.run_with(
        fastapi_app
    )
