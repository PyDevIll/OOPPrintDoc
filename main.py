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


class InkjetPrinter:
    def print_page(self, page_txt: str):
        print("Inkjet printer uses black ink to print:")
        print(page_txt+"\n")


class LaserPrinter:
    def print_page(self, page_txt: str):
        print("Laser printer uses black toner to print:")
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

