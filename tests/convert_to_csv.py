from nanonets import NANONETSOCR
model = NANONETSOCR()

model.set_token('841bf15a-cad1-11ed-987a-36465ce69625')

model.convert_to_csv('D:\\Technofinch\\pdfToCSV\ocr-python\\tests\AJAN354.pdf', output_file_name='output.csv')