class Document:
    def __init__(self):
        self.__pages = []

    def add_page(self, content: str):
        self.__pages.append(content)

    @property
    def content(self):
        return self.__content

    def print_document(self, printer):
        for page in self.__pages:
            printer.print_page(page)


class Printer:
    def __init__(self):
        __consumable = ''
        __kind = ''

    def print_page(self, page_txt:str):
        print(__kind + " printer uses " + __consumable + " to print:")
        print(page_txt+"\n")


class InkjetPrinter(Printer):
    def __init__(self):
        self.__kind = "Inkjet"
        self.__consumable = "black ink"

class LaserPrinter:
    def __init__(self):
        self.__kind = "Laser"
        self.__consumable = "black toner"


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

