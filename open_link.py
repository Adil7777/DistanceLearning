import webbrowser


def open_link(link):
    chromedir = 'C:\Рабочий стол\Distance Learning\chromedriver.exe %s'
    webbrowser.get(chromedir)
    webbrowser.open(link)


