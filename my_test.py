import unittest
from unittest.mock import patch
import main


class MyTest(unittest.TestCase):
    def setUp(self):
        self.doc = main.Document("Test text")

    @patch('main.print')
    def test_print_page_inkjet(self, print_mock):
        self.doc.print_document(main.InkjetPrinter)
        self.assertEqual(print_mock.call_count, 3)

    @patch('main.print')
    def test_print_page_laser(self, print_mock):
        self.doc.print_document(main.LaserPrinter)
        self.assertEqual(print_mock.call_count, 3)

    @patch('main.print')
    def test_main(self, print_mock):
        main.main()
        self.assertEqual(print_mock.call_count, 9)


