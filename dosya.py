import sys
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QListWidget, QVBoxLayout, 
                             QPushButton, QHBoxLayout, QLabel, QLineEdit, 
                             QMenu, QAction, QToolBar)

class DosyaYoneticisi(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Dosya Yöneticisi')
        self.setGeometry(100, 100, 800, 600)

        # Adres çubuğu
        self.adres_cubugu = QLineEdit(self)
        self.adres_cubugu.returnPressed.connect(self.dizin_degistir)

        # Geri ve ileri butonları
        geri_butonu = QPushButton('Geri', self)
        geri_butonu.clicked.connect(self.geri_git)
        ileri_butonu = QPushButton('İleri', self)
        ileri_butonu.clicked.connect(self.ileri_git)

        # Dosya listesi
        self.liste_kutusu = QListWidget(self)
        self.liste_kutusu.itemDoubleClicked.connect(self.ogeye_cift_tiklama)
        self.liste_kutusu.setContextMenuPolicy(3)  # Özel context menüsü için
        self.liste_kutusu.customContextMenuRequested.connect(self.context_menu)

        # Araç çubuğu
        toolbar = QToolBar(self)
        kopyala_aksiyon = QAction('Kopyala', self)
        # kopyala_aksiyon.triggered.connect(self.kopyala)  # TODO: Kopyalama fonksiyonunu uygula
        toolbar.addAction(kopyala_aksiyon)
        tasi_aksiyon = QAction('Taşı', self)
        # tasi_aksiyon.triggered.connect(self.tasi)  # TODO: Taşıma fonksiyonunu uygula
        toolbar.addAction(tasi_aksiyon)
        sil_aksiyon = QAction('Sil', self)
        # sil_aksiyon.triggered.connect(self.sil)  # TODO: Silme fonksiyonunu uygula
        toolbar.addAction(sil_aksiyon)

        # Layout
        hbox = QHBoxLayout()
        hbox.addWidget(geri_butonu)
        hbox.addWidget(ileri_butonu)
        hbox.addWidget(self.adres_cubugu)

        vbox = QVBoxLayout()
        vbox.addWidget(toolbar)
        vbox.addLayout(hbox)
        vbox.addWidget(self.liste_kutusu)
        self.setLayout(vbox)

        self.gezinme_gecmisi = []
        self.gecmis_indeks = 0
        self.dizin_degistir(os.getcwd())

        self.show()

    def dizin_degistir(self, dizin=None):
        if dizin is None:
            dizin = self.adres_cubugu.text()
        try:
            os.chdir(dizin)
            self.adres_cubugu.setText(dizin)
            self.dosyalari_listele()
            self.gezinme_gecmisi.append(dizin)
            self.gecmis_indeks = len(self.gezinme_gecmisi) - 1
        except FileNotFoundError:
            print(f"Dizin bulunamadı: {dizin}")

    def dosyalari_listele(self):
        self.liste_kutusu.clear()
        mevcut_dizin = os.getcwd()
        dosyalar = os.listdir(mevcut_dizin)
        self.liste_kutusu.addItems(dosyalar)

    def ogeye_cift_tiklama(self, item):
        oge = item.text()
        yol = os.path.join(os.getcwd(), oge)
        if os.path.isdir(yol):
            self.dizin_degistir(yol)

    def geri_git(self):
        if self.gecmis_indeks > 0:
            self.gecmis_indeks -= 1
            self.dizin_degistir(self.gezinme_gecmisi[self.gecmis_indeks])

    def ileri_git(self):
        if self.gecmis_indeks < len(self.gezinme_gecmisi) - 1:
            self.gecmis_indeks += 1
            self.dizin_degistir(self.gezinme_gecmisi[self.gecmis_indeks])

    def context_menu(self, pos):
        menu = QMenu(self)
        kopyala_aksiyon = QAction('Kopyala', self)
        # kopyala_aksiyon.triggered.connect(self.kopyala)  # TODO: Kopyalama fonksiyonunu uygula
        menu.addAction(kopyala_aksiyon)
        tasi_aksiyon = QAction('Taşı', self)
        # tasi_aksiyon.triggered.connect(self.tasi)  # TODO: Taşıma fonksiyonunu uygula
        menu.addAction(tasi_aksiyon)
        sil_aksiyon = QAction('Sil', self)
        # sil_aksiyon.triggered.connect(self.sil)  # TODO: Silme fonksiyonunu uygula
        menu.addAction(sil_aksiyon)
        menu.exec_(self.liste_kutusu.mapToGlobal(pos))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DosyaYoneticisi()
    sys.exit(app.exec_())