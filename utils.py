def get_input(prompt="", cast=None, condition=None, errorMessage=None) -> None:
    while True:
        try:
            response = (cast or str)(input(prompt))
            assert condition is None or condition(response)
            return response
        except:
            print(errorMessage or "Niepoprawna dana wejściowa. Spróbuj ponownie.")

def text_tab(text: str, tab_amount: int) -> str:
    tabs = ""
    if tab_amount > 0:
        for _ in range(tab_amount):
            tabs += '\t'
    return tabs + text

def print_tab(text: str, tab_amount: int) -> None:
    print(text_tab(text, tab_amount))
