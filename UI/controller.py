import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listShape = []

    def fillDD(self):
        self._listYear = self._model.listYears
        self._listShape = self._model.listShapes
        for y in self._listYear:
            self._view.ddyear.options.append(ft.dropdown.Option(y))
        for s in self._listShape:
            self._view.ddshape.options.append(ft.dropdown.Option(s))
        self._view.update_page()

    def handle_graph(self, e):
        anno = self._view.ddyear.value
        shape = self._view.ddshape.value
        self._model.creaGrafo(anno, shape)

    def handle_path(self, e):
        pass