from PyPDF2 import PdfReader, PdfWriter
from typing import List, Dict
from time import sleep
from tqdm import tqdm
from PIL import Image
import pytesseract
import cv2 as cv
import shutil
import fitz
import os


arquivos = [arquivo for arquivo in os.listdir() if '.pdf' in arquivo.lower()]

i = 0
for arquivo in arquivos:
    pdf_document = fitz.open(arquivo)  # Abre a Nota Fiscal.
    page = pdf_document.load_page(0)  # Carrega a página.
    image = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # Converte a página num objeto de imagem.
    image.save(f'img{i}.jpg')  # Salva a imagem num arquivo.
    pdf_document.close()  # Fechar o PDF para garantir que o arquivo seja liberado.
    image = Image.open(f'img{i}.jpg')
    print(image.size)
    i+=1