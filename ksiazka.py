class Ksiazka:
    ID: str
    Nazwa: str
    Rozszerzenie_pliku: str
    Data_Modyfikacji: str
    link: str

    def __init__(self, ID: str, Nazwa: str, Rozszerzenie_pliku: str, Data_Modyfikacji: str, link: str):
        self.zapisz_dane(ID, Nazwa, Rozszerzenie_pliku, Data_Modyfikacji, link)

    def zapisz_dane(self, ID: str, Nazwa: str, Rozszerzenie_pliku: str, Data_Modyfikacji: str, link: str) -> bool:
        try: 
            self._is_Valid("ID", ID)
            self.ID = ID
            self._is_Valid("Nazwa", Nazwa)
            self.Nazwa = Nazwa
            self._is_Valid("Rozszerzenie_pliku", Rozszerzenie_pliku)
            self.Rozszerzenie_pliku = Rozszerzenie_pliku
            self._is_Valid("Data_Modyfikacji", Data_Modyfikacji)
            self.Data_Modyfikacji = Data_Modyfikacji
            self._is_Valid("link", link)
            self.link = link
        except Exception as e:
            print(e)

    def _is_Valid(self, data_type: str, new_data: str):
        isInvalid = False
        if data_type == "ID":
            if len(new_data) > 64:
                isInvalid = True
            return True
        elif data_type == "Nazwa":
            if len(new_data) > 32:
                isInvalid = True
            return True
        elif data_type == "Rozszerzenie_pliku":
            if len(new_data) > 4:
                isInvalid = True
            return True
        elif data_type == "Data_Modyfikacji":
            if len(new_data) > 60:
                isInvalid = True
            return True
        elif data_type == "link":
            if len(new_data) > 512:
                isInvalid = True
            return True
        if isInvalid:
            raise Exception(f"Input parameter {data_type} is invalid.")
        raise Exception(f"Input parameter {data_type} does not exist.")

    def sortuj(self):
        pass

    def filtruj(self):
        pass

    def __str__(self) -> str:
        return (self.Nazwa)

if __name__ == "__main__":
    print("Wrong file. Try to run aplikacja.py instead of ksiazka.py")