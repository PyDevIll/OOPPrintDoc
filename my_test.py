import unittest
from unittest.mock import patch
import main


class MyTest(unittest.TestCase):
    def setUp(self):
        self.doc = main.Document()
        self.doc.add_page("-Title Page-")
        self.doc.add_page("Last page")
        self.lines_to_be_printed = 4     # 2 pages x 2 print statements per page

    def test_add_page(self):
        self.doc.add_page("Bonus page")
        self.assertListEqual(
            self.doc._Document__pages,
            ["-Title Page-", "Last page", "Bonus page"]
        )

    @patch('main.print')
    def test_print_page_inkjet(self, print_mock):
        self.doc.print_document(main.InkjetPrinter())
        self.assertEqual(self.lines_to_be_printed, print_mock.call_count)

    @patch('main.print')
    def test_print_page_laser(self, print_mock):
        self.doc.print_document(main.LaserPrinter())
        self.assertEqual(self.lines_to_be_printed, print_mock.call_count)

    @patch('main.print')
    def test_main(self, print_mock):
        main.main()
        lines_total = (self.lines_to_be_printed + 1) * 2 + 1
        self.assertEqual(lines_total, print_mock.call_count)


