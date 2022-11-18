from ksiazka import Ksiazka
from utils import getInput
import base64

class Aplikacja:
    ksiazki = list()
    _counter = 0

    def dodaj_ksiazke(self):
        base64_id = base64.b64encode(str(self._counter).encode('ascii')).decode('ascii')
        self._counter += 1
        name = getInput("\t\tPodaj nazwę książki: ")
        extension = getInput("\t\tPodaj rozszerzenie książki: ")
        date = getInput("\t\tPodaj datę wydania książki: ")
        link = getInput("\t\tPodaj link do książki: ")
        self.ksiazki.append(Ksiazka(base64_id, name, extension, date, link))
    def usun_ksiazke(self): #TODO
        name = getInput("\t\tPodaj nazwę książki do usunięcia: ")
        list_of_valid_books = []
        counter = 0
        for ksiazka_object in self.ksiazki:
            if str(ksiazka_object) == name:
                list_of_valid_books.append((counter, ksiazka_object))
                counter += 1
        if len(list_of_valid_books) == 0:
            print("\t\tNie ma żadnych książek o podanym tytule.")
        elif len(list_of_valid_books) == 1:
            self._usun_ksiazke(list_of_valid_books[0][1].ID)
            print("\t\tUsunięto jedyną książkę o podanym tytule.")
        else:
            print("\t\tWybierz książkę do usunięcia: ")
            for data_tuple in list_of_valid_books:
                print(
                    '\t\t' + 
                    str(data_tuple[0] + 1) + 
                    ". Nazwa:" + data_tuple[1] + 
                    " | Rozszerzenie: " + data_tuple[1].Rozszerzenie_pliku +
                    " | Data Modyfikacji: " + data_tuple[1].Data_Modyfikacji +
                    " | Link: " + data_tuple[1].link +
                    )
    def edytuj_ksiazke(self):
        pass 
    def sortuj(self):
        for ksiazka_object in self.ksiazki:
            print(ksiazka_object)
    def filtruj(self):
        pass

    def _dodaj_ksiazke(self, id: str, nazwa: str, rozszerzenie_pliku: str, data_modyfikacji: str, link: str):
        temp_ksiazka = Ksiazka()
        try:
            temp_ksiazka.zapisz_dane(id, nazwa, rozszerzenie_pliku, data_modyfikacji, link=link)
            self.ksiazki.append()
        except Exception as e:
            print("Failed to add a book ;< .")

    def _usun_ksiazke(self, id: str):
        for index in range(len(self.ksiazki)):
            if self.ksiazki[index].ID == id:
                self.ksiazki.pop(index)
                return

    # def _edytuj_ksiazke(self, id: str, nazwa: str, rozszerzenie_pliku: str, data_modyfikacji: str, link: str):
    #     pass 

    # def _sortuj(self):
    #     pass

    # def _filtruj(self, nazwa: str = None, rozszerzenie_pliku: str = None, data_modyfikacji: str = None, link: str = None):
    #     pass


    def _wyswietl_menu_aplikacji(self):
        print("============================================================================")
        print("Witaj w aplikacji! Oto możliwe opcje:")
        print("1. Zarządanie albumem książek.")
        print("2. Zarządanie wyświetlaniem albumu.")
        print("3. Zakończ program.")
        return getInput(
            "Podaj numer operacji do wykonania: ",
            int,
            errorMessage="Proszę, podaj tą informację w formie numeru :)."
            )

    def _wyswietl_menu_zarzadzania(self):
        print("\tJesteś w menu zarządania albumem - oto możliwe opcje:")
        print("\t1. Dodaj książkę.")
        print("\t2. Edytuj książkę.")
        print("\t3. Usuń książkę.")
        print("\t4. Zakończ zarządzanie książkami.")
        return getInput(
            "\tPodaj numer operacji do wykonania: ",
            int,
            errorMessage="\tProszę, podaj tą informację w formie numeru :)."
            )

    def _wyswietl_porzegnanie_zarzadania(self):
        print("\tKończysz pracę z menu zarządania albumem.")

    def _wyswietl_menu_wyswietlania_ksiazek(self):
        print("\tJesteś w menu wyświetlania książek - oto możliwe opcje:")
        print("\t1. Pokaż posortowane książki.")
        print("\t2. Pokaż książki przefiltrowane po tytule.")
        print("\t3. Zakończ zarządzanie książkami.")
        return getInput(
            "\tPodaj numer operacji do wykonania: ",
            int,
            errorMessage="\tProszę, podaj tą informację w formie numeru :)."
            )

    def _wyswietl_porzegnanie_wyswietlania_ksiazek(self):
        print("\tKończysz pracę z menu wyświetlania książek.")

    def wyswietl_porzegnanie_aplikacji(self):
        print("Kończysz pracę z aplikacją. Zapraszamy ponownie i życzymy miłego dnia :).")


if __name__ == "__main__":
    aplikacja = Aplikacja()
    is_exit = False

    while not is_exit:
        choice = int(aplikacja._wyswietl_menu_aplikacji())

        if choice == 1:
            is_exit_zarzadzaj = False
            while not is_exit_zarzadzaj:
                choice_zarzadzaj = int(aplikacja._wyswietl_menu_zarzadzania())            

                if choice_zarzadzaj == 1:
                    aplikacja.dodaj_ksiazke()

                elif choice_zarzadzaj == 2:
                    aplikacja.edytuj_ksiazke()

                elif choice_zarzadzaj == 3:
                    aplikacja.usun_ksiazke()

                elif choice_zarzadzaj == 4:
                    aplikacja._wyswietl_porzegnanie_zarzadania()
                    is_exit_zarzadzaj = True

        elif choice == 2:
            is_exit_zarzadzaj = False
            while not is_exit_zarzadzaj:
                choice_wyswietl = int(aplikacja._wyswietl_menu_wyswietlania_ksiazek())            
                if choice_wyswietl == 1:
                    aplikacja.sortuj()

                elif choice_wyswietl == 2:
                    aplikacja.filtruj()

                elif choice_wyswietl == 3:
                    aplikacja._wyswietl_porzegnanie_wyswietlania_ksiazek()
                    is_exit_zarzadzaj = True

        elif choice == 3:
            aplikacja.wyswietl_porzegnanie_aplikacji()
            input("Wciśnij dowolny klawisz, aby zakończyć program.")
            is_exit = True