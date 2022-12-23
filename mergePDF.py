import os
from PyPDF2 import PdfFileMerger, PdfFileReader
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)8.8s] %(message)s",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger(__name__)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    logging.info('Program starts')

    src = os.getcwd()
    merger = PdfFileMerger()
    file_list = [file for file in os.listdir(f"{src}\\input") if file.endswith('.pdf')]

    for file in file_list:
        logging.info(f"file name: {file}")
        merger.append(PdfFileReader(f"{src}\\input\\{file}", "rb"))

    if len(file_list) > 0:
        merger.write(".\\output\\combined.pdf")
        merger.close()
    else:
        logging.info("*** Nothing to merge ***")
 
