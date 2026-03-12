from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from Not_Wikipedia import *
from Course import Ui_MainCourse
from Age import Ui_MainAge
from Discovery import Ui_MainDiscovery
from Failure import Ui_MainFailure
from Histori import Ui_MainHistori
from Ukrain import Ui_MainUkrain
from Work import Ui_MainWork
from The_facts import Ui_MainFacts
from Quotes import Ui_MainQuotes
from Films import Ui_MainFilms
from Cartoons import Ui_MainCartoons
from Series import Ui_MainSeries
from Anime import Ui_MainAnime
from Books import Ui_MainBooks
from Comics import Ui_MainComics
from Manga import Ui_MainManga
from Games import Ui_MainGames
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QSlider, QPushButton
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
# ... ваші існуючі імпорти ...

# 1. Менеджер звуку (щоб керувати звуком з будь-якого вікна)
class SoundManager:
    def __init__(self):
        # Музика
        self.music_player = QMediaPlayer()
        self.music_output = QAudioOutput()
        self.music_player.setAudioOutput(self.music_output)
        
        # Ефекти (SFX)
        self.sfx_player = QMediaPlayer()
        self.sfx_output = QAudioOutput()
        self.sfx_player.setAudioOutput(self.sfx_output)

    def play_bg_music(self, file_path):
        self.music_player.setSource(QUrl.fromLocalFile(file_path))
        self.music_output.setVolume(0.5) # Початкова гучність 50%
        self.music_player.play()

    def set_music_volume(self, volume):
        self.music_output.setVolume(volume / 100)

    def set_sfx_volume(self, volume):
        self.sfx_output.setVolume(volume / 100)

# Глобальний об'єкт менеджера
sound_manager = SoundManager()

# 2. Вікно налаштувань звуку
class WidgetSettings(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Налаштування звуку")
        self.setFixedSize(300, 200)
        
        layout = QVBoxLayout()

        # Повзунок музики
        layout.addWidget(QLabel("Гучність музики:"))
        self.music_slider = QSlider(Qt.Orientation.Horizontal)
        self.music_slider.setRange(0, 100)
        self.music_slider.setValue(int(sound_manager.music_output.volume() * 100))
        self.music_slider.valueChanged.connect(sound_manager.set_music_volume)
        layout.addWidget(self.music_slider)

        # Повзунок ефектів
        layout.addWidget(QLabel("Гучність ефектів:"))
        self.sfx_slider = QSlider(Qt.Orientation.Horizontal)
        self.sfx_slider.setRange(0, 100)
        self.sfx_slider.setValue(int(sound_manager.sfx_output.volume() * 100))
        self.sfx_slider.valueChanged.connect(sound_manager.set_sfx_volume)
        layout.addWidget(self.sfx_slider)

        self.setLayout(layout)

# 3. Модифікація головного вікна
class InternetWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWikipedia()
        self.ui.setupUi(self)
        
        # Запуск фонової музики (вкажіть шлях до свого файлу)
        # sound_manager.play_bg_music("background_music.mp3")

        # Додаємо кнопку налаштувань (якщо її немає в UI, можна створити програмно)
        # Припустимо, у вас є кнопка pushButton_Settings у дизайні:
        # self.ui.pushButton_Settings.clicked.connect(self.open_settings)
        
        # Або просто підключимо до будь-якої вільної кнопки для тесту:
        self.ui.Course.clicked.connect(self.open_second_window)
        # ... ваші коннекти ...
        
        # Додамо можливість відкрити налаштування
        self.settings_window = None

    def open_settings(self):
        if self.settings_window is None:
            self.settings_window = WidgetSettings()
        self.settings_window.show()

    # ... решта ваших методів open_second_window ...

class InternetWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWikipedia()
        self.ui.setupUi(self)

        self.ui.Course.clicked.connect(self.open_second_window)
        self.ui.Age.clicked.connect(self.open_second_window_1)
        self.ui.Quotes.clicked.connect(self.open_second_window_2)
        self.ui.Failure.clicked.connect(self.open_second_window_3)
        self.ui.Histori.clicked.connect(self.open_second_window_4)
        self.ui.Ukrain.clicked.connect(self.open_second_window_5)
        self.ui.Work.clicked.connect(self.open_second_window_6)
        self.ui.TheFacts.clicked.connect(self.open_second_window_7)
        self.ui.Discovery.clicked.connect(self.open_second_window_8)
        self.ui.Films.clicked.connect(self.open_second_window_9)
        self.ui.Cartoons.clicked.connect(self.open_second_window_10)
        self.ui.Series.clicked.connect(self.open_second_window_11)
        self.ui.Anime.clicked.connect(self.open_second_window_12)
        self.ui.Books.clicked.connect(self.open_second_window_13)
        self.ui.Comics.clicked.connect(self.open_second_window_14)
        self.ui.Manga.clicked.connect(self.open_second_window_15)
        self.ui.pushButton_14.clicked.connect(self.open_second_window_16)

    def open_second_window(self):
        self.open_second_window = WidgetCourse()
        self.open_second_window.show()
    def open_second_window_1(self):
        self.open_second_window_1 = WidgetAge()
        self.open_second_window_1.show()
    def open_second_window_2(self):
        self.open_second_window_2 = WidgetQuotes()
        self.open_second_window_2.show()
    def open_second_window_3(self):
        self.open_second_window_3 = WidgetFailure()
        self.open_second_window_3.show()
    def open_second_window_4(self):
        self.open_second_window_4 = WidgetHistori()
        self.open_second_window_4.show()
    def open_second_window_5(self):
        self.open_second_window_5 = WidgetUkrain()
        self.open_second_window_5.show()
    def open_second_window_6(self):
        self.open_second_window_6 = WidgetWork()
        self.open_second_window_6.show()
    def open_second_window_7(self):
        self.open_second_window_7 = WidgetFacts()
        self.open_second_window_7.show()
    def open_second_window_8(self):
        self.open_second_window_8 = WidgetDiscovery()
        self.open_second_window_8.show()
    def open_second_window_9(self):
        self.open_second_window_9 = WidgetFilms()
        self.open_second_window_9.show()
    def open_second_window_10(self):
        self.open_second_window_10 = WidgetCartoons()
        self.open_second_window_10.show()
    def open_second_window_11(self):
        self.open_second_window_11 = WidgetSeries()
        self.open_second_window_11.show()
    def open_second_window_12(self):
        self.open_second_window_12 = WidgetAnime()
        self.open_second_window_12.show()
    def open_second_window_13(self):
        self.open_second_window_13 = WidgetBooks()
        self.open_second_window_13.show()
    def open_second_window_14(self):
        self.open_second_window_14 = WidgetComics()
        self.open_second_window_14.show()
    def open_second_window_15(self):
        self.open_second_window_15 = WidgetManga()
        self.open_second_window_15.show()
    def open_second_window_16(self):
        self.open_second_window_16 = WidgetGames()
        self.open_second_window_16.show()

class WidgetCourse(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainCourse()
        self.ui.setupUi(self)

class WidgetAge(QMainWindow):        
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainAge()
        self.ui.setupUi(self)

class WidgetQuotes(QMainWindow):        
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainQuotes()
        self.ui.setupUi(self)

class WidgetFailure(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainFailure()
        self.ui.setupUi(self)
        
class WidgetHistori(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainHistori()
        self.ui.setupUi(self)

class WidgetUkrain(QMainWindow):        
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainUkrain()
        self.ui.setupUi(self)

class WidgetWork(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWork()
        self.ui.setupUi(self)
        
class WidgetFacts(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainFacts()
        self.ui.setupUi(self)

class WidgetDiscovery(QMainWindow):        
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainDiscovery()
        self.ui.setupUi(self)
        
class WidgetFilms(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainFilms()
        self.ui.setupUi(self)
        
class WidgetCartoons(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainCartoons()
        self.ui.setupUi(self)
        
class WidgetSeries(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainSeries()
        self.ui.setupUi(self)

class WidgetAnime(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainAnime()
        self.ui.setupUi(self)

class WidgetBooks(QMainWindow):        
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainBooks()
        self.ui.setupUi(self)

class WidgetComics(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainComics()
        self.ui.setupUi(self)

class WidgetManga(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainManga()
        self.ui.setupUi(self)

class WidgetGames(QMainWindow):        
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainGames()
        self.ui.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_window = InternetWindow()
    main_window.show()
    sys.exit(app.exec())