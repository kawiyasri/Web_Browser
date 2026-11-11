# Python Web Browser 🌐

A simple desktop web browser developed using **Python, PyQt5, and Qt WebEngine**. This application provides a graphical interface for browsing websites with essential navigation features such as Back, Forward, Reload, Home, and URL navigation.

## 📌 Project Overview

The Python Web Browser is a desktop application that uses PyQt5 to create a graphical user interface and Qt WebEngine to render web pages.

It provides a basic browser experience within a standalone desktop application, allowing users to visit websites and navigate between web pages.

## ✨ Features

- **Back Navigation:** Navigate to the previously visited webpage.
- **Forward Navigation:** Move forward through browsing history.
- **Reload:** Refresh the currently opened webpage.
- **Home:** Navigate to the default Google homepage.
- **URL Navigation:** Enter a website URL in the address bar to visit a webpage.
- **Address Bar Synchronization:** Automatically updates the URL bar when the webpage changes.
- **Maximized Window:** Opens the browser in a maximized desktop window.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| PyQt5 | Creating the desktop graphical user interface |
| Qt WebEngine | Rendering and displaying web pages |
| PyQt5.QtWidgets | Building browser components such as buttons and toolbars |
| PyQt5.QtCore | Handling URLs and application functionality |

## 📂 Project Structure

```text
Python-Web-Browser/
│
├── main.py          # Main application source code
├── README.md        # Project documentation
└── requirements.txt # Required Python packages
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the Project Directory

```bash
cd Python-Web-Browser
```

### 3. Install Dependencies

Make sure Python is installed on your system.

Install the required packages:

```bash
pip install PyQt5 PyQtWebEngine
```

Alternatively, install dependencies using:

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python main.py
```

The browser window will open, displaying the Google homepage.

## 🖥️ How It Works

1. The application initializes a PyQt5 GUI using `QMainWindow`.
2. `QWebEngineView` loads and displays web pages.
3. A toolbar provides navigation controls.
4. Back and Forward buttons navigate through browsing history.
5. Reload refreshes the current webpage.
6. The Home button redirects the browser to Google.
7. Users can enter a URL in the address bar and press Enter to navigate.
8. The `urlChanged` signal synchronizes the address bar with the currently loaded webpage.

## 🚀 Future Enhancements

- Add multiple tabs for browsing different websites.
- Implement bookmarks and browsing history.
- Add a search engine selection option.
- Include a download manager.
- Improve the browser interface with modern styling.
- Add a customizable homepage.
- Implement proper URL validation and automatic HTTPS handling.

## 🎯 Learning Outcomes

- Understanding desktop GUI development using PyQt5.
- Working with Qt WebEngine for web content rendering.
- Implementing event handling and signal-slot connections.
- Creating navigation functionality in Python applications.
- Understanding URL handling and browser navigation.
