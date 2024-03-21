from pprint import PrettyPrinter
from sheet_data import SpreadsheetData

pp= PrettyPrinter(indent = 2)

product_data = SpreadsheetData()

product_info = product_data.get_product_data()

pp.pprint(product_info)
