from ksiazka import Ksiazka
from utils import *
import base64

class Aplikacja:
    ksiazki = list()
    _counter = 0

    def dodaj_ksiazke(self):
        base64_id = base64.b64encode(str(self._counter).encode('ascii')).decode('ascii')
        self._counter += 1
        dane_ksiazki = self._pobierz_dane_ksiazki(2)
        self.ksiazki.append(Ksiazka(base64_id, dane_ksiazki[0], dane_ksiazki[1], dane_ksiazki[2], dane_ksiazki[3]))

    def usun_ksiazke(self):
        self._wybierz_ksiazke(
            function_to_call=self._usun_ksiazke, 
            welcome_text="Wyświetlam listę dostępnych książek do usunięcia: ",
            call_to_action="Podaj numer książki do usunięcia (podanie numeru '0' spowoduje powrót do poprzedniego menu): ",
            successful_prompt="Książka została usunięta pomyślnie.",
            tab_amount=2
        )

    def edytuj_ksiazke(self):
        self._wybierz_ksiazke(
        function_to_call=self._edytuj_ksiazke, 
        welcome_text="Wyświetlam listę dostępnych książek do edycji: ",
        call_to_action="Podaj numer książki do zedytowania (podanie numeru '0' spowoduje powrót do poprzedniego menu): ",
        successful_prompt="Książka została zedytowana pomyślnie.", 
        tab_amount=2
        )

    def sortuj(self):
        self.ksiazki = sorted(self.ksiazki, key=lambda ksiazka: ksiazka.Nazwa) 
        self._wyswietl_wszystkie_ksiazki(None, 2)

    def filtruj(self):
        choice = get_input(
            prompt=text_tab("Podaj tytuł tekst tytułu książki do wyświetlenia: ", 2)
        )
        book_list = []
        for ksiazka in self.ksiazki:
            if str(ksiazka) == choice:
                book_list.append(ksiazka)
        self._wyswietl_wszystkie_ksiazki(book_list, 2)


    def _dodaj_ksiazke(self, id: str, nazwa: str, rozszerzenie_pliku: str, data_modyfikacji: str, link: str):
        temp_ksiazka = Ksiazka()
        try:
            temp_ksiazka.zapisz_dane(id, nazwa, rozszerzenie_pliku, data_modyfikacji, link=link)
            self.ksiazki.append()
        except Exception as e:
            print("Failed to add a book ;< .")

    def _usun_ksiazke(self, index: int, tab_amount):
        self.ksiazki.pop(index)

    def _edytuj_ksiazke(self, index: int, tab_amount: int = 2):
        nowe_dane_ksiazki = self._pobierz_dane_ksiazki(tab_amount)
        self.ksiazki[index].zapisz_dane(
            self.ksiazki[index].ID,
            nowe_dane_ksiazki[0],
            nowe_dane_ksiazki[1],
            nowe_dane_ksiazki[2],
            nowe_dane_ksiazki[3],
        )

    def _wybierz_ksiazke(self, function_to_call, welcome_text: str, call_to_action: str, successful_prompt: str, tab_amount: int = 0):
        should_exit = False 
        while not should_exit:
            print_tab(welcome_text, tab_amount)
            self._wyswietl_wszystkie_ksiazki(None, tab_amount, True)
            choice = None
            while True:
                choice = get_input(
                    text_tab(
                        call_to_action,
                        tab_amount
                    )
                )
                try:
                    choice = int(choice)
                    break
                except:
                    print_tab("Proszę, podaj liczbę :).", tab_amount)
                    continue

            if choice >= 0 and choice <= len(self.ksiazki):
                if choice == 0:
                    should_exit = True
                else:
                    function_to_call(choice - 1)
                    print_tab(successful_prompt, tab_amount)
            else:
                print_tab("Proszę, podaj poprawną liczbę :).", tab_amount)

    def _pobierz_dane_ksiazki(self, tab_amount):
        name = get_input(text_tab("Podaj nazwę książki: ", tab_amount))
        extension = get_input(text_tab("Podaj rozszerzenie książki: ", tab_amount))
        date = get_input(text_tab("Podaj datę wydania książki: ", tab_amount))
        link = get_input(text_tab("Podaj link do książki: ", tab_amount))
        return (name, extension, date, link)

    def _wyswietl_menu_aplikacji(self):
        print("============================================================================")
        print("Witaj w aplikacji! Oto możliwe opcje:")
        print("1. Zarządanie albumem książek.")
        print("2. Zarządanie wyświetlaniem albumu.")
        print("3. Zakończ program.")
        return get_input(
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
        return get_input(
            "\tPodaj numer operacji do wykonania: ",
            int,
            errorMessage="\tProszę, podaj tą informację w formie numeru :)."
            )

    def _wyswietl_porzegnanie_zarzadania(self):
        print("\tKończysz pracę z menu zarządania albumem.")

    def _wyswietl_menu_wyswietlania_ksiazek(self):
        print("\tJesteś w menu wyświetlania książek - oto możliwe opcje:")
        print("\t1. Posortuj książki i pokaż je.")
        print("\t2. Pokaż książki przefiltrowane po tytule.")
        print("\t3. Zakończ wyświetlanie książkami.")
        return get_input(
            "\tPodaj numer operacji do wykonania: ",
            int,
            errorMessage="\tProszę, podaj tą informację w formie numeru :)."
            )

    def _wyswietl_wszystkie_ksiazki(self, book_list = None, tab_amount: int = 0, with_details: bool = False):
        if not book_list:
            book_list = self.ksiazki
        if len(book_list) == 0:
            print_tab("Album nie posiada żadnych książek.", tab_amount)
        else:
            print_tab("Oto książki z twojego albumu:", tab_amount)
            for index in range(len(book_list)):
                temp_ksiazka = book_list[index]
                text_to_print = '#' + str(index+1) + '. Nazwa: ' + str(temp_ksiazka)
                if with_details:
                    print_tab(
                        (
                            text_to_print +
                            " | Rozszerzenie: " + temp_ksiazka.Rozszerzenie_pliku +
                            " | Data Modyfikacji: " + temp_ksiazka.Data_Modyfikacji +
                            " | Link: " + temp_ksiazka.link
                        ),
                        tab_amount
                    )
                else:
                    print_tab(text_to_print, tab_amount)

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
            is_exit_wyswietl = False
            while not is_exit_wyswietl:
                choice_wyswietl = int(aplikacja._wyswietl_menu_wyswietlania_ksiazek())            
                if choice_wyswietl == 1:
                    aplikacja.sortuj()

                elif choice_wyswietl == 2:
                    aplikacja.filtruj()

                elif choice_wyswietl == 3:
                    aplikacja._wyswietl_porzegnanie_wyswietlania_ksiazek()
                    is_exit_wyswietl = True

        elif choice == 3:
            aplikacja.wyswietl_porzegnanie_aplikacji()
            input("Wciśnij dowolny klawisz, aby zakończyć program.")
            is_exit = True