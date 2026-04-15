import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._ddAnnoValue=None
        self._ddBrandValue=None
        self._retailer=None

    def handleTopVendite(self, e):
        pass

    def handleAnalizzaVendite(self, e):
        pass

    def fillddAnno(self):
        self._view.ddAnno.options.append(
            ft.dropdown.Option(
                key=None,
                text="Nessun filtro",
                data=None,
                on_click=self._choiceDDAnno
            )
        )

        for anno in self._model.getAllAnni():
            self._view.ddAnno.options.append(ft.dropdown.Option(
                key=anno,
                data=anno,
                on_click= self._choiceDDAnno,
                text=anno.__str__()
            ))

    def _choiceDDAnno(self, e):
        self._ddAnnoValue=e.control.data
        print(self._ddAnnoValue)


    def fillddBrand(self):
        self._view.ddBrand.options.append(
            ft.dropdown.Option(
                key=None,
                text="Nessun filtro",
                data=None,
                on_click=self._choiceDDBrand
            )
        )

        for brand in self._model.getAllBrand():
            self._view.ddBrand.options.append(ft.dropdown.Option(
                key=brand,
                data=brand,
                on_click= self._choiceDDBrand,
            ))

    def _choiceDDBrand(self, e):
        self._ddBrandValue=e.control.data
        print(self._ddBrandValue)


    #USIAMO OGGETTI PER I RETAILER
    def fillddRetailer(self):

        self._view.ddRetailer.options.append(
            ft.dropdown.Option(
                key=None,
                text="Nessun filtro",
                data=None,
                on_click=self._choiceDDRetailer
        ))

        for rt in self._model.getAllRetailer():
            self._view.ddRetailer.options.append(ft.dropdown.Option
                                 (key=str(rt.Retailer_code),
                                  text=rt.Retailer_name,
                                  data=rt,
                                  on_click=self._choiceDDRetailer
                                  ))

    def _choiceDDRetailer(self, e):
        self._retailer=e.control.data
        print(self._retailer)

    def handle_hello(self, e):
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()
