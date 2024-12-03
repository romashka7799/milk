from tkinter import *
from tkinter.ttk import Notebook, Combobox
from tkinter import filedialog
from tkinter import messagebox as mb

class Windows:
    def __init__(self, title='Ефимова Ангелина Борисовна'):
        self.root = Tk() 
        self.root.title(title)
        self.root.geometry('600x500')

        self.tabs_control = Notebook(self.root,height=100,width=20)
        self.tabs_control.enable_traversal()
        self.tab_1 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_1, text='Калькулятор')

        self.num1_entry = Entry(self.tab_1)
        self.num1_entry.pack(pady=30,anchor=N)

        self.operation_combobox = Combobox(self.tab_1, values=["+", "-", "*", "/"])  # комбокс
        self.operation_combobox.pack(pady=10)

        self.num2_entry = Entry(self.tab_1)
        self.num2_entry.pack(pady=30,anchor=S)

        self.tab_2 = Frame(self.tabs_control)  # вкладка чекбоксы
        self.tabs_control.add(self.tab_2, text='Чекбоксы')

        self.perv_var = IntVar()
        self.vtor_var = IntVar()
        self.tret_var = IntVar()

        self.tab_3 = Frame(self.tabs_control)  # вкладка вывод текста
        self.tabs_control.add(self.tab_3, text='Работа с текстом')
        self.text_box = Text(self.tab_3).pack()
        self.load_text_button = Button(self.tab_3, text="Загрузить текст из файла", command=self.load_text)
        self.load_text_button.pack(pady=10)

    def run(self):
        self.draw_widgets()
        self.draw_widgets1()
        self.draw_menu()
        self.root.mainloop()

    def draw_widgets(self):
        self.tabs_control.pack(fill=BOTH, expand=True)

    def draw_widgets1(self):
        Label(self.tab_1, text='Введите').pack()
        Button(self.tab_1, text="Вычислить", command=self.calculate,bg ='cyan').pack(pady=20,anchor=S)
        Label(self.tab_2, text='выбери вариант:').pack()
        Checkbutton(self.tab_2, text='первый вариант', variable=self.perv_var, fg='green').pack()
        Checkbutton(self.tab_2, text='второй вариант', variable=self.vtor_var, fg='red').pack()
        Checkbutton(self.tab_2, text='третий вариант', variable=self.tret_var, fg='blue').pack()
        Button(self.tab_2, text='нажми если выбрал', width=25, command=self.check_checkbox).pack()

    def calculate(self):
        a = float(self.num1_entry.get())
        b = float(self.num2_entry.get())
        action = self.operation_combobox.get()
        if action == '+':
            result = a + b
        elif action == '-':
            result = a - b
        elif action == '*':
            result = a * b
        elif action == '/':
            result = a / b

        else:
            result = "неправильное действие"
        mb.showinfo('Результат', str(result))
       
    def check_checkbox(self):
        text = ''
        if self.perv_var.get():
            text += 'Вы выбрали первый вариант\n'
        if self.vtor_var.get():
            text += 'Вы выбрали второй вариант\n'
        if self.tret_var.get():
            text += 'Вы выбрали третий вариант\n'
        if not text:
            text = 'Вы еще ничего не выбрали'
        mb.showinfo('Выбор', text)

    def draw_menu(self):
        menu_bar = Menu(self.root)
        file_menu = Menu(menu_bar, tearoff=0)
    
        file_menu.add_command(label='Сохранить', command=self.cmd)
        file_menu.add_command(label='Сохранить как',command=self.load_tex)

        file_menu.add_separator()
        menu_bar.add_cascade(label='Файл', menu=file_menu)
        self.root.configure(menu=menu_bar)

    def cmd(self):
        mb.showinfo('Инфо', 'Сохранение выполнено')

    def load_text(self):  # вывод текста для сохранить как
        file = filedialog.askopenfilename(filetypes=[('файлы', '*.txt')])
        if file:
            with open(file, 'r', encoding='utf-8') as f:
                text = f.read()

    def load_tex(self):  
        file = filedialog.askopenfilename(filetypes=[('файлы', '*.txt')])
        if file:
            with open(file, 'r', encoding='utf-8') as f:
                text = f.read()

if __name__ == "__main__":
    window = Windows()
    window.run()
