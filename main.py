class Document:
    def __init__(self):
        self.__pages = []

    def add_page(self, content: str):
        self.__pages.append(content)

    def print_document(self, printer):
        for page in self.__pages:
            printer.print_page(page)


class Printer:
    __consumable = ''
    __kind = ''

    def __init__(self, kind, consumable):
        self.__kind = kind
        self.__consumable = consumable

    def print_page(self, page_txt:str):
        print(self.__kind + " printer uses " + self.__consumable + " to print:")
        print(page_txt+"\n")


class InkjetPrinter(Printer):
    def __init__(self):
        super().__init__("Inkjet", "black ink")

    def print_page(self, page_txt:str):
        super().print_page(page_txt)


class LaserPrinter(Printer):
    def __init__(self):
        super().__init__("Laser", "black toner")

    def print_page(self, page_txt:str):
        super().print_page(page_txt)


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

