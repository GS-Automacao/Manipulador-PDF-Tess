from configs.utils.update_functions import check_update
from configs.utils.menu_functions import main_hub
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'configs/tess/tesseract.exe'

VERSION: str = 'v1.0.2'




def run():
    print('Manipulador de PDFs')
    print('V: ', VERSION)
    check_update(VERSION)  # Verifica se há atualizações.
    main_hub()  # inicia o menu.


if __name__ == '__main__':
    try:
        run()
    except Exception as e:
        print(e)
        input()
