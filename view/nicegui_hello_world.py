from fastapi import FastAPI
import secrets
from nicegui import app, ui


def init(fastapi_app: FastAPI) -> None:
    @ui.page('/')
    def show():
        ui.label('Hello, FastAPI!')
        ui.dark_mode().bind_value(app.storage.user, 'dark_mode')
        ui.checkbox('dark mode').bind_value(app.storage.user, 'dark_mode')

    ui.run_with(
        fastapi_app,
        storage_secret=secrets.token_hex(32)
    )
