import tkinter as tk
from random import *

def mistake(k):
    for i in k:
        if i not in '0123456789ABCDEF':
            return 1
    return 0

def generator():
    inp = str(key_input.get())

    if inp != '' and mistake(inp) == 0 and inp[0] != '0':
        inp = int(inp, 16)
        elems = [0, 0, 0, 0, 0]
        KEY = ""
        alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        for j in range(3):
            elems[0] = str(inp)[j]
            for i in range(1, 5):
                elems[i] = alf[randint(0, 34)]
            shuffle(elems)
            block1 = ''.join(elems)
            KEY += block1 + '-'
        KEY = KEY[:-1] + ' ' + str(inp)[-2:]
        key_output.delete("0", tk.END)
        key_output.insert(0, KEY)

    
if __name__ == "__main__":
    window = tk.Tk()
    window.title('generator')
    window.geometry('1000x600')
    background_img = tk.PhotoImage(file='doodle.png')
    lbl_bg = tk.Label(window, image=background_img)
    lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
    input_label = tk.Label(window, text='Введите 5 символов из букв от A до F или цифр', font=14)
    input_label.place(relx=0.2, rely=0.5)
    key_input = tk.Entry(window, width=5, font=18)
    key_input.insert(0, '00000')
    key_input.place(relx=0.6, rely=0.5)
    
    btn = tk.Button(window, text='Сгенерировать ключ', font=14, width=18, command=generator)
    btn.place(relx=0.2, rely=0.54)
    
    output_label = tk.Label(window, text='Ключ: ', font=14)
    output_label.place(relx=0.2, rely=0.6)
    key_output = tk.Entry(window, width=30, font=16)
    key_output.place(relx=0.2, rely=0.65)

    window.mainloop()
