class Document:
    def __init__(self, text):
        self.__content = text

    @property
    def content(self):
        return self.__content

    def print_document(self, printer):
        printer.print_page(self)


class InkjetPrinter:
    @staticmethod
    def print_page(doc):
        print("Inkjet printer outputs:")
        print(doc.content)
        print('Printed with black ink')


class LaserPrinter:
    @staticmethod
    def print_page(doc):
        print("Laser printer outputs:")
        print(doc.content)
        print('Printed with black toner')


def main():
    some_doc = Document("Some text on a several pages")

    print("Launching inkjet printer...")
    some_doc.print_document(InkjetPrinter)

    print()
    print("Launching laser printer...")
    some_doc.print_document(LaserPrinter)


if __name__ == "__main__":
    main()

