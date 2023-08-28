from pytube import YouTube
from PyQt5 import uic, QtWidgets

def main():

    link = tela.lineEdit_link.text()
    path = tela.label_diretorio.text()
    yt = YouTube(link)

    print("Título: ", yt.title)
    print("Número de views: ", yt.views)
    print("Tamanho do vídeo: ", yt.length, "segundos")
    print("Avaliação do vídeo: ", yt.rating)

    # Usa a maior resolucao #
    ys = yt.streams.get_highest_resolution()
    # ys = yt.streams.get_audio_only()

    # Começa o Download do vídeo #
    print("Baixando...")
    ys.download(path)
    print("Download completo!")

app=QtWidgets.QApplication([])
tela=uic.loadUi(r'tela.ui')

# tela.pushButton_abrir.clicked.connect(abrir_diretorio)
tela.pushButton_confirmar.clicked.connect(main)

tela.show()
app.exec()