
import sys
from urllib.parse import quote_plus

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QToolBar,
    QAction,
    QLineEdit,
    QProgressBar,
    QLabel,
    QSizePolicy,
    QStyle
)
from PyQt5.QtWebEngineWidgets import QWebEngineView


class NexaView(QMainWindow):

    def __init__(self):
        super().__init__()

        # -------------------------------
        # Window Configuration
        # -------------------------------
        self.setWindowTitle("Modern Web Browser")
        self.setMinimumSize(900, 600)
        self.resize(1280, 800)

        self.home_url = "https://www.google.com"

        # -------------------------------
        # Main Browser Widget
        # -------------------------------
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(self.home_url))

        self.setCentralWidget(self.browser)

        # -------------------------------
        # Navigation Toolbar
        # -------------------------------
        self.navbar = QToolBar("Navigation")
        self.navbar.setMovable(False)
        self.navbar.setFloatable(False)
        self.navbar.setIconSize(self.style().standardIcon(
            QStyle.SP_ArrowBack
        ).availableSizes()[0] if self.style().standardIcon(
            QStyle.SP_ArrowBack
        ).availableSizes() else self.navbar.iconSize())

        self.addToolBar(self.navbar)

        # Back Button
        self.back_action = QAction(
            self.style().standardIcon(QStyle.SP_ArrowBack),
            "Back", self
        )
        self.back_action.setShortcut(QKeySequence("Alt+Left"))
        self.back_action.setToolTip("Go to previous page")
        self.back_action.triggered.connect(self.browser.back)
        self.navbar.addAction(self.back_action)

        # Forward Button
        self.forward_action = QAction(
            self.style().standardIcon(QStyle.SP_ArrowForward),
            "Forward", self
        )
        self.forward_action.setShortcut(QKeySequence("Alt+Right"))
        self.forward_action.setToolTip("Go to next page")
        self.forward_action.triggered.connect(self.browser.forward)
        self.navbar.addAction(self.forward_action)

        # Reload Button
        self.reload_action = QAction(
            self.style().standardIcon(QStyle.SP_BrowserReload),
            "Reload", self
        )
        self.reload_action.setShortcut(QKeySequence("Ctrl+R"))
        self.reload_action.setToolTip("Refresh current page")
        self.reload_action.triggered.connect(self.browser.reload)
        self.navbar.addAction(self.reload_action)

        # Stop Button
        self.stop_action = QAction(
            self.style().standardIcon(QStyle.SP_BrowserStop),
            "Stop", self
        )
        self.stop_action.setToolTip("Stop loading")
        self.stop_action.triggered.connect(self.browser.stop)
        self.navbar.addAction(self.stop_action)

        self.navbar.addSeparator()

        # Home Button
        self.home_action = QAction(
            self.style().standardIcon(QStyle.SP_DirHomeIcon),
            "Home", self
        )
        self.home_action.setToolTip("Go to homepage")
        self.home_action.triggered.connect(self.navigate_home)
        self.navbar.addAction(self.home_action)

        self.navbar.addSeparator()

        # -------------------------------
        # Address Bar
        # -------------------------------
        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText(
            "Search Google or enter a website address..."
        )
        self.url_bar.setClearButtonEnabled(True)
        self.url_bar.setMinimumHeight(36)
        self.url_bar.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Fixed
        )

        self.url_bar.returnPressed.connect(self.navigate_to_url)

        self.navbar.addWidget(self.url_bar)

        # Focus address bar using Ctrl + L
        focus_action = QAction(self)
        focus_action.setShortcut(QKeySequence("Ctrl+L"))
        focus_action.triggered.connect(self.focus_url_bar)
        self.addAction(focus_action)

        # -------------------------------
        # Status Bar
        # -------------------------------
        self.status_bar = self.statusBar()
        self.status_bar.showMessage("Welcome to Web Browser")

        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximumWidth(160)
        self.progress_bar.setMaximumHeight(12)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.hide()

        self.status_bar.addPermanentWidget(self.progress_bar)

        self.security_label = QLabel("  ● Ready  ")
        self.status_bar.addPermanentWidget(self.security_label)

        # -------------------------------
        # Browser Event Connections
        # -------------------------------
        self.browser.urlChanged.connect(self.update_url)
        self.browser.titleChanged.connect(self.update_title)
        self.browser.loadStarted.connect(self.load_started)
        self.browser.loadProgress.connect(self.load_progress)
        self.browser.loadFinished.connect(self.load_finished)

        # Enable and disable navigation actions
        self.browser.urlChanged.connect(self.update_navigation)

        # -------------------------------
        # Apply Modern UI Theme
        # -------------------------------
        self.apply_styles()

    # ===================================
    # Navigation Functions
    # ===================================

    def navigate_home(self):
        self.browser.setUrl(QUrl(self.home_url))

    def navigate_to_url(self):
        text = self.url_bar.text().strip()

        if not text:
            return

        # Search Google if the input is not a website URL
        if " " in text or (
            "." not in text
            and "://" not in text
            and text.lower() != "localhost"
        ):
            search_url = (
                "https://www.google.com/search?q="
                + quote_plus(text)
            )
            url = QUrl(search_url)

        else:
            url = QUrl.fromUserInput(text)

        if url.isValid() and not url.isEmpty():
            self.browser.setUrl(url)

    def update_url(self, url):
        self.url_bar.setText(url.toString())
        self.url_bar.setCursorPosition(0)

    def update_title(self, title):
        if title:
            self.setWindowTitle(f"{title} | Modern Web Browser")
        else:
            self.setWindowTitle("Modern Web Browser")

    def focus_url_bar(self):
        self.url_bar.setFocus()
        self.url_bar.selectAll()

    def update_navigation(self, url):
        self.back_action.setEnabled(self.browser.history().canGoBack())
        self.forward_action.setEnabled(
            self.browser.history().canGoForward()
        )

    # ===================================
    # Loading Functions
    # ===================================

    def load_started(self):
        self.progress_bar.setValue(0)
        self.progress_bar.show()
        self.security_label.setText("  ● Loading  ")
        self.status_bar.showMessage("Loading webpage...")

    def load_progress(self, progress):
        self.progress_bar.setValue(progress)

    def load_finished(self, success):
        self.progress_bar.hide()

        if success:
            self.security_label.setText("  ● Ready  ")
            self.status_bar.showMessage(
                "Webpage loaded successfully.", 4000
            )
        else:
            self.security_label.setText("  ● Error  ")
            self.status_bar.showMessage(
                "Unable to load webpage. Check your internet connection.",
                6000
            )

    # ===================================
    # UI Styling
    # ===================================

    def apply_styles(self):

        self.setStyleSheet("""
            QMainWindow {
                background-color: #111827;
            }

            QToolBar {
                background-color: #1F2937;
                border: none;
                border-bottom: 1px solid #374151;
                spacing: 8px;
                padding: 10px;
            }

            QToolButton {
                background-color: transparent;
                color: #E5E7EB;
                border: none;
                border-radius: 7px;
                padding: 8px 12px;
                font-size: 13px;
                font-weight: 600;
            }

            QToolButton:hover {
                background-color: #374151;
            }

            QToolButton:pressed {
                background-color: #4B5563;
            }

            QToolButton:disabled {
                color: #6B7280;
            }

            QToolBar::separator {
                background-color: #4B5563;
                width: 1px;
                margin: 5px;
            }

            QLineEdit {
                background-color: #111827;
                color: #F9FAFB;
                border: 1px solid #4B5563;
                border-radius: 10px;
                padding: 8px 14px;
                font-size: 14px;
                selection-background-color: #2563EB;
            }

            QLineEdit:focus {
                border: 1px solid #3B82F6;
                background-color: #172033;
            }

            QLineEdit::placeholder {
                color: #9CA3AF;
            }

            QStatusBar {
                background-color: #1F2937;
                color: #D1D5DB;
                border-top: 1px solid #374151;
                font-size: 11px;
            }

            QProgressBar {
                background-color: #374151;
                border: none;
                border-radius: 5px;
            }

            QProgressBar::chunk {
                background-color: #3B82F6;
                border-radius: 5px;
            }
        """)

    # ===================================
    # Close Event
    # ===================================

    def closeEvent(self, event):
        self.browser.stop()
        event.accept()


# =======================================
# Application Entry Point
# =======================================

if __name__ == "__main__":

    app = QApplication(sys.argv)

    app.setApplicationName("Web Browser")
    app.setOrganizationName("Web Browser Inc.")
    app.setStyle("Fusion")

    window = NexaView()
    window.show()

    sys.exit(app.exec_())
