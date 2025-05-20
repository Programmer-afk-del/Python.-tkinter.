import tkinter as tk
from tkinter import messagebox, Menu
import random

class ArrayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Робота з масивом")
        self.array = []

        self.setup_ui()
        self.setup_menu()
        self.setup_context_menu()

    def setup_ui(self):
        tk.Label(self.root, text="Розмір масиву:").grid(row=0, column=0)
        self.entry_size = tk.Entry(self.root)
        self.entry_size.grid(row=0, column=1)

        self.btn_generate = tk.Button(self.root, text="Заповнити", command=self.fill_array)
        self.btn_generate.grid(row=0, column=2)

        self.btn_sort = tk.Button(self.root, text="Сортувати", command=self.sort_array)
        self.btn_sort.grid(row=0, column=3)

        self.btn_sum = tk.Button(self.root, text="Обчислити суму", command=self.calculate_sum)
        self.btn_sum.grid(row=0, column=4)

        self.listbox_original = tk.Listbox(self.root)
        self.listbox_original.grid(row=1, column=0, columnspan=2)

        self.listbox_sorted = tk.Listbox(self.root)
        self.listbox_sorted.grid(row=1, column=2, columnspan=2)

        self.label_sum = tk.Label(self.root, text="Сума: ")
        self.label_sum.grid(row=1, column=4)

    def setup_menu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        array_menu = Menu(menubar, tearoff=0)
        array_menu.add_command(label="Заповнити", command=self.fill_array)
        array_menu.add_command(label="Сортувати", command=self.sort_array)
        array_menu.add_command(label="Обчислити суму", command=self.calculate_sum)
        menubar.add_cascade(label="Дії з масивом", menu=array_menu)

        about_menu = Menu(menubar, tearoff=0)
        about_menu.add_command(label="Про автора", command=lambda: messagebox.showinfo("Автор", "Студент групи КІ-21"))
        about_menu.add_command(label="Умова задачі", command=lambda: messagebox.showinfo("Умова", "Обчислити суму додатних парних елементів масиву та відсортувати масив методом обміну."))
        menubar.add_cascade(label="Про програму", menu=about_menu)

    def setup_context_menu(self):
        self.context_menu = Menu(self.root, tearoff=0)
        self.context_menu.add_command(label="Світла тема", command=self.set_light_theme)
        self.context_menu.add_command(label="Темна тема", command=self.set_dark_theme)
        self.context_menu.add_command(label="Початкова тема", command=self.set_default_theme)

        self.root.bind("<Button-3>", self.show_context_menu)

    def show_context_menu(self, event):
        self.context_menu.post(event.x_root, event.y_root)

    def fill_array(self):
        try:
            size = int(self.entry_size.get())
            self.array = [random.randint(-100, 100) for _ in range(size)]
            self.listbox_original.delete(0, tk.END)
            for num in self.array:
                self.listbox_original.insert(tk.END, num)
        except ValueError:
            messagebox.showerror("Помилка", "Введіть коректне число!")

    def sort_array(self):
        sorted_array = self.array.copy()
        n = len(sorted_array)
        for i in range(n):
            for j in range(0, n-i-1):
                if sorted_array[j] > sorted_array[j+1]:
                    sorted_array[j], sorted_array[j+1] = sorted_array[j+1], sorted_array[j]
        self.listbox_sorted.delete(0, tk.END)
        for num in sorted_array:
            self.listbox_sorted.insert(tk.END, num)

    def calculate_sum(self):
        result = sum(x for x in self.array if x > 0 and x % 2 == 0)
        self.label_sum.config(text=f"Сума: {result}")

    def set_light_theme(self):
        self.root.configure(bg='white')

    def set_dark_theme(self):
        self.root.configure(bg='gray20')

    def set_default_theme(self):
        self.root.configure(bg='SystemButtonFace')

if __name__ == "__main__":
    root = tk.Tk()
    app = ArrayApp(root)
    root.mainloop()
