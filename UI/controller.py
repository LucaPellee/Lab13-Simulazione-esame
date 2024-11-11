import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDyear(self):
        listaAnni = self._model.getAnni()
        for a in listaAnni:
            self._view.ddyear.options.append(ft.dropdown.Option(a))
        self._view.update_page()

    def fillDDshape(self, e):
        self._view.ddshape.options.clear()
        self._view.ddshape.value = None
        an = self._view.ddyear.value
        try:
            anno = int(an)
        except ValueError:
            self._view.create_alert("Il valore dell'anno non è convertibile in intero")
        listaShape = self._model.getShape(anno)
        for s in listaShape:
            self._view.ddshape.options.append(ft.dropdown.Option(s))
        self._view.update_page()

    def handle_graph(self, e):
        anno = int(self._view.ddyear.value)
        shape = self._view.ddshape.value
        self._model.creaGrafo(anno, shape)
        nNodes = self._model.getNumNodes()
        nEdges = self._model.getNumEdges()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Numero di vertici: {nNodes}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {nEdges}"))
        listaTuple = self._model.calcolaSommaArchi()
        for t in listaTuple:
            self._view.txt_result.controls.append(ft.Text(f"Nodo {t[0]}, somma pesi su archi = {t[1]}"))
        self._view.update_page()

    def handle_path(self, e):
        self._view.txtOut2.controls.clear()
        path, dist = self._model.getPath()
        self._view.txtOut2.controls.append(ft.Text(f"Distanza massima: {dist}"))
        for i in range(len(path)-1):
            self._view.txtOut2.controls.append(ft.Text(f"{path[i]}-->{path[i+1]}"))
        self._view.update_page()