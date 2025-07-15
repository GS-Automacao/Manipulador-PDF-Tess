#CÓDIGO PARA RENOMEAÇÃO DE NFS DE SÃO PAULO QUE SÃO IMAGENS.

from typing import Dict, List
from PyPDF2 import PdfReader
from tqdm import tqdm
from PIL import Image
import fitz
import os
from .utils import all_sizes, processa_nfs, processa_outras, pdf_to_img
from time import sleep


# def f08() -> int:
#     tot_pags = 0
#     files = [file for file in os.listdir() if '.pdf' in file.lower()]
#     cidades = all_sizes.keys()
#     nfs: Dict[str, List[str]] = {cidade: [] for cidade in cidades}
#     nfs['outras'] = []
#     print('Identificando prefeituras...')
#     for file in tqdm(files):
#         # Verificar se contem texto.
#         with open(file, 'rb') as file_b:
#             pdf = PdfReader(file_b).pages[0]
#             rows = pdf.extract_text().split('\n')
#             if len(rows) > 1:
#                 nfs['outras'].append(file)
#                 continue
#         # Verifica de qual prefeitura é.
#         pdf_document = fitz.open(file)  # Abre a Nota Fiscal.
#         page = pdf_document.load_page(0)  # Carrega a página.
#         image = page.get_pixmap()  # Converte a página num objeto de imagem.
#         image.save('img.png')  # Salva a imagem num arquivo.
#         pdf_document.close()  # Fecha o arquivo.
#         image = Image.open('img.png')
#         for cidade in cidades:
#             if image.size in all_sizes[cidade]:
#                 nfs[cidade].append(file)
#                 break
#     # Processa as notas fiscais.
#     for cidade in cidades:
#         if len(nfs[cidade]) > 1:
#             tot_pags += processa_nfs(cidade, nfs[cidade])
#     if nfs['outras']:
#         tot_pags += processa_outras(nfs['outras'])
#     return tot_pags

tot_pags = 0
files = [file for file in os.listdir() if '.pdf' in file.lower()]
cidades = all_sizes.keys()
nfs: Dict[str, List[str]] = {cidade: [] for cidade in cidades}
nfs['outras'] = []
print('Identificando prefeituras...')
for file in tqdm(files):

    # Verificar se contem texto.
    with open(file, 'rb') as file_b:
        pdf = PdfReader(file_b).pages[0]
        rows = pdf.extract_text().split('\n')
        if len(rows) > 1:
            nfs['outras'].append(file)
            continue

    # Verifica de qual prefeitura é.
    pdf_document = fitz.open(file)  # Abre a Nota Fiscal.
    page = pdf_document.load_page(0)  # Carrega a página.
    image = page.get_pixmap()  # Converte a página num objeto de imagem.
    image.save('img.png')  # Salva a imagem num arquivo.
    pdf_document.close()  # Fecha o arquivo.
    image = Image.open('img.png')
    for cidade in cidades:
        if image.size in all_sizes[cidade]:
            nfs[cidade].append(file)
            break
# Processa as notas fiscais.
for cidade in cidades:
    if len(nfs[cidade]) > 1:
        tot_pags += processa_nfs(cidade, nfs[cidade])
if nfs['outras']:
    tot_pags += processa_outras(nfs['outras'])

print(tot_pags)

















tot_pags: int = 0
sizes = all_sizes.get(cidade, None)
# Verifica se a cidade foi encontrada.
if sizes is None:
    raise TypeError('Cidade não cadastrada.')
# Lista as NFs no diretório.
if not files:
    files = [file for file in os.listdir() if '.pdf' in file.lower()]

print(cidade)
sleep(0.1)
# Renomeia as notas.
for file in tqdm(files):
    try:
        pdf_to_img(file, sizes)
    except TypeError:
        continue
    nome: str = extract_text('nome.jpg', config='--psm 7').strip()
    num_nf: str = extract_text('num_nf.jpg', config='--psm 13 -c tessedit_char_whitelist=0123456789').strip()

    novo_nome = f'NF {num_nf[-4:]} - {nome}.pdf'
    shutil.move(file, novo_nome)
try:
    # Apaga as imagens residuais.
    os.remove('img.jpg')
    os.remove('nome.jpg')
    os.remove('num_nf.jpg')
except FileNotFoundError:
    pass

print(tot_pags)