import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._anno = None
        self._brand = None
        self._retailer_code = None

    def handle_top_vendite(self, e):
        """
        funzione che recupera le prime 5 (per ricavo) vendite presenti nel database, con i vincoli
        dati dal menu a tendina, e stampa i risultati nella GUI
        """
        top_vendite = self._model.get_top_sales(self._anno, self._brand, self._retailer_code)
        self._view.lst_result.controls.clear()
        if len(top_vendite) == 0:
            self._view.lst_result.controls.append(ft.Text("Nessuna vendita con i filtri selezionati"))
        else:
            for vendita in top_vendite:
                self._view.lst_result.controls.append(ft.Text(vendita))
        self._view.update_page()

    def handle_analizza_vendite(self, e):
        """
            funzione che stampa nella GUI delle statistiche sommarie di tutte le vendite presenti nel
            database con i vincoli specificati dai menu a tendina
        """
        statistiche_vendite = self._model.get_sales_stats(self._anno, self._brand, self._retailer_code)
        self._view.lst_result.controls.clear()
        self._view.lst_result.controls.append(ft.Text("Satistiche vendite:"))
        self._view.lst_result.controls.append(ft.Text(f"Giro d'affari: {statistiche_vendite[0]}"))
        self._view.lst_result.controls.append(ft.Text(f"Numero vendite: {statistiche_vendite[1]}"))
        self._view.lst_result.controls.append(ft.Text(f"Numero retailers coinvolti: {statistiche_vendite[2]}"))
        self._view.lst_result.controls.append(ft.Text(f"Numero prodotti coinvolti: {statistiche_vendite[3]}"))
        self._view.update_page()

    ################################################################################
    ################################################################################
    #######    Utilities per popolare/leggere i menu a tendina     #################
    ################################################################################
    ################################################################################

    ######### Dropdpwn Anno #############
    def populate_dd_anno(self):
        """methodo che popola la tendina con tutti gli anni in cui ci sono state vendite,
        prendendo le informazioni dal database"""
        anni = self._model.get_years()
        for anno in anni:
            self._view.dd_anno.options.append(ft.dropdown.Option(anno[0]))
        self._view.update_page()

    def read_anno(self, e):
        """event handler che legge l'anno scelto dal menu a tendina ogniqualvolta viene cambiata
        la scelta, e lo memorizza in una variabile di instanza. L'anno è un intero, se si tratta di un anno,
        oppure un None se viene scelta l'opzione nessun filtro sull'anno"""
        if e.control.value == "None":
            self._anno = None
        else:
            self._anno = e.control.value

    ######### Dropdpwn Brand #############
    def populate_dd_brand(self):
        """metodo che popola la tendina con tutti i brands presenti nel database"""
        brands = self._model.get_brands()
        for brand in brands:
            self._view.dd_brand.options.append(ft.dropdown.Option(brand[0]))
        self._view.update_page()

    def read_brand(self, e):
        """event handler che legge il brand scelto dal menu a tendina ogniqualvolta viene cambiata
            la scelta, e lo memorizza in una variabile di instanza. Il brand è una stringa oppure,
             `None` se viene scelta l'opzione nessun filtro.
             """
        if e.control.value == "None":
            self._brand = None
        else:
            self._brand = e.control.value

    ######### Dropdpwn Retailer #############
    def populate_dd_retailer(self):
        """
        Funzione per popolare il menu a tendina dei retailers. NOTA BENE: a differenza delle altre tendine,
        che sono popolate con delle stringhe o interi, questa tendina la popoliamo con degli oggetti di tipo
        Retailer, sfruttando l'opzione data. In questo modo, quando selezioniamo una opzione dal menu,
        possiamo andare a recuperare direttamente l'oggetto. Per fare questa cosa, l'event handler non deve essere
        sul menu a tendina, ma direttamente nelle opzioni (on_click), perché l'oggetto contenuto da una opzione é
        accessibile solo dall'opzione stessa.
        """
        retailers = self._model.get_retailers()
        for retailer in retailers:
            self._view.dd_retailer.options.append(ft.dropdown.Option(text=retailer.retailer_name,
                                                                     data=retailer,
                                                                     on_click=self.read_retailer))
        self._view.update_page()

    def read_retailer(self, e):
        """event handler che legge il retailer scelto dal menu a tendina ogniqualvolta viene cliccata una opzione.
        In questo caso andiamo a leggere direttamente l'oggetto, contenuto nel campo data dell'opzione.
        """
        if e.control.data is None:
            self._retailer_code = None
        else:
            self._retailer_code = e.control.data.retailer_code
