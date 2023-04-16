import csv
from tkinter import *
from tkinter import filedialog
CSV_FILE = ""
HTML_FILE = ""
MAIL_THEMES = ""


def get_data():
    file_name, sample, themes = create_gui()
    users = []
    a = file_name.split('/')[-1]
    if a.count('.') != -1:
        b = a.split('.')
        if b[0] and b[1] == 'csv':
            try:
                f = open(file_name)
                reader = csv.reader(f)
                for row in reader:
                    users.append(row)
            except FileNotFoundError:
                print('Такого файла не существует')
        else:
            print('Выберите csv файл')
    return users, sample, themes


def create_gui():
    global CSV_FILE, HTML_FILE, MAIL_THEMES

    def choose_csv_file():
        global CSV_FILE
        CSV_FILE = filedialog.askopenfilename(filetypes=(("csv-file", "*.csv"), ("all files", "*.*")))
        lbl_name1.configure(text=CSV_FILE)

    def choose_html_sample():
        global HTML_FILE
        HTML_FILE = filedialog.askopenfilename(filetypes=(("html-file", "*.html"), ("all files", "*.*")))
        lbl_name2.configure(text=HTML_FILE)

    def submit():
        global MAIL_THEMES
        MAIL_THEMES = txt1.get()
        if not MAIL_THEMES:
            warning_lbl.configure(text='Введите тему письма', bg='red')
            return 1
        if not CSV_FILE:
            warning_lbl.configure(text='Выберите csv-файл', bg='red')
            return 1
        if not HTML_FILE:
            warning_lbl.configure(text='Выберите html-файл', bg='red')
            return 1
        window.destroy()
    window = Tk()
    window.title("Рассылка")
    window.geometry("800x400")
    themes = Label(window, text="Введите тему письма", font=("Arial", 16))
    themes.grid(column=0, row=0)
    txt1 = Entry(window, width=40, font=('Arial', 16))
    txt1.grid(column=1, row=0)
    lbl = Label(window, text="Выберите csv-файл", font=("Arial", 16))
    lbl.grid(column=0, row=3)
    btn = Button(window, text="Выбрать", command=choose_csv_file, font=("Arial", 16))
    btn.grid(column=0, row=4)
    lbl_name1 = Label(window, text="")
    lbl_name1.grid(column=1, row=4)
    lbl = Label(window, text="Выберите html-шаблон", font=("Arial", 16))
    lbl.grid(column=0, row=6)
    btn = Button(window, text="Выбрать", command=choose_html_sample, font=("Arial", 16))
    btn.grid(column=0, row=7)
    lbl_name2 = Label(window, text="")
    lbl_name2.grid(column=1, row=7)
    submit_button = Button(window, text="Подтвердить", command=submit, font=('Arial', 16))
    submit_button.grid(column=0, row=12)
    warning_lbl = Label(window, text="", font=('Arial', 20))
    warning_lbl.grid(column=1, row=15)
    window.mainloop()
    return CSV_FILE, HTML_FILE, MAIL_THEMES


def main():
    print(get_data())


if __name__ == '__main__':
    main()
