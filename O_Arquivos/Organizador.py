import os
from tkinter.filedialog import askdirectory

rota = askdirectory(title="Selecione uma pasta")

lista_arquivos = os.listdir(rota)

locais = {
        "imagens": [".png", ".jpg"],
        "planilhas": [".xlsx"],
        "pdfs": [".pdf"],
        "docx": [".docx"],
        "txt": [".txt"],

    }

for arquivo in lista_arquivos:
     #pdfs
     nome, extensao = os.path.splitext(f"{rota}/{arquivo}")
     for pasta in locais:
          if extensao in locais[pasta]:
              if not os.path.exists(f"{rota}/{pasta}"):
                  os.mkdir(f"{rota}/{pasta}")
              os.rename(f"{rota}/{arquivo}", f"{rota}/{pasta}/{arquivo}")