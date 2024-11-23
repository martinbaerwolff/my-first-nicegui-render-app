from fastapi import FastAPI
import secrets
from nicegui import app, ui
from .map import map


def enable_reload_warning():
    if __debug__:
        return
    ui.run_javascript(
        """
            window.onbeforeunload = function(event) {
                event.preventDefault();
                event.returnValue = "Sind Sie sicher, dass Sie die Seite verlassen möchten? Änderungen werden verloren gehen.";
                return "Sind Sie sicher, dass Sie die Seite verlassen möchten?";
            };
        """
    )


def init(fastapi_app: FastAPI) -> None:
    @ui.page('/')
    def show():
        enable_reload_warning()
        ui.label('Hello, FastAPI!')
        ui.dark_mode().bind_value(app.storage.user, 'dark_mode')
        ui.checkbox('dark mode').bind_value(app.storage.user, 'dark_mode')
        map()

    ui.run_with(
        fastapi_app,
        storage_secret=secrets.token_hex(32),
        title="Test NiceGUI + Render",
        favicon="🐿️"
    )
