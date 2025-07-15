from typing import Dict, List
from PyPDF2 import PdfReader
from tqdm import tqdm
from PIL import Image
import fitz
import os
from utils import all_sizes, processa_nfs, processa_outras
import pytesseract
import cv2 as cv

# pytesseract.pytesseract.tesseract_cmd = 'configs/tess/tesseract.exe'

arquivos = [arquivo for arquivo in os.listdir() if ".pdf" in arquivo.lower()]
print(arquivos)

#TRANSFORMAR PDF EM IMAGEM
pdf_document = fitz.open(arquivos[0])  # Abre a Nota Fiscal.
page = pdf_document.load_page(0)  # Carrega a página.
image = page.get_pixmap()  # Converte a página num objeto de imagem.
image.save('img.png')  # Salva a imagem num arquivo.
pdf_document.close()  # Fecha o arquivo.
image = Image.open('img.png')


#DEPOIS DESCREVER O FUNCIONAMENTO
img = cv.imread('img.png')
scale_percent = 15  # Aumentar a imagem em 150%
# Calculando o novo tamanho
new_width = int(img.shape[1] * scale_percent)
new_height = int(img.shape[0] * scale_percent)
# Redimensionar a imagem proporcionalmente
img = cv.resize(img, (new_width, new_height), interpolation=cv.INTER_LANCZOS4)
# 1. Conversão para escala de cinza
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Executar o OCR na imagem processada
text = pytesseract.image_to_string(img, config='--psm 7')
print(text)