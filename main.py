class Document:
    def __init__(self):
        self.__pages = []

    def add_page(self, content: str):
        self.__pages.append(content)

    def print_document(self, printer):
        for page in self.__pages:
            printer.print_page(page)


# Родительский класс - практически пустой и наверное не нужен теперь
class Printer:
    _consumable = ''
    _kind = ''

    def print_page(self, page_txt:str):
        pass


class InkjetPrinter(Printer):
    def __init__(self):
        self._kind = "Inkjet"
        self._consumable = "black ink"

    # Код в методах повторяется!
    def print_page(self, page_txt: str):
        print(self._kind + " printer uses " + self._consumable + " to print:")
        print(page_txt+"\n")


class LaserPrinter(Printer):
    def __init__(self):
        self._kind = "Laser"
        self._consumable = "black toner"

    # Код в методах повторяется!
    def print_page(self, page_txt: str):
        print(self._kind + " printer uses " + self._consumable + " to print:")
        print(page_txt+"\n")


def main():
    some_doc = Document()
    some_doc.add_page("-Title Page-")
    some_doc.add_page("Last page")

    ink_printer = InkjetPrinter()
    laser_printer = LaserPrinter()

    print("Launching inkjet printer...")
    some_doc.print_document(ink_printer)

    print()
    print("Launching laser printer...")
    some_doc.print_document(laser_printer)


if __name__ == "__main__":
    main()

