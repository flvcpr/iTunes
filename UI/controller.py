import warnings

import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_hello(self, e):
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def handleCreaGrafo(self, e):
        try:
            totDint = int(self._view._txtInDurata.value)
        except ValueError:
            warnings.warn_explicit(message="duration not integrable",
                                   category=TypeError,
                                   filename="controller.py",
                                   lineno=22)
            return

        self._model.buildGraph(totDint)
        nodes = self._model.getNodes()
        nodes.sort(key=lambda x: x.Title)

        for n in nodes:
            self._view._ddAlbum.controls.append(ft.dropdown.Option(data=n, text=n.Title,
                                                                   on_click=self.getSelectedAlbum))
            print("done")
        listDD = map(lambda x: ft.dropdown.Option(data=x,
                                                  text=x.Title,
                                                  on_click=self.getSelectedAlbum),
                                                  nodes)
        self._view._ddAlbum.options = listDD
        self._view.update_page()
    def getSelectedAlbum(self, e):
        print("getSelectedAlbum chiamata")
        pass

    def handleAnalisiComp(self, e):
        pass

    def handleGetSetAlbum(self, e):
        pass
