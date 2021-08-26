# Copyright 2021, ModzabazeR <moddaeng.pps@gmail.com>, All rights reserved.
# เอาโค้ดไปแก้ไข ต่อยอด ส่งต่อได้ตามสบายเลยครับ ส่งมาให้ดูกันด้วยนะ :)
# โปรแกรมนี้จะเขียนไฟล์ทับของเก่าไปเลย เพราะฉะนั้นตรวจสอบให้ดีๆก่อนนะครับ

from tkinter import *
from tkinter import filedialog


main_window = Tk()
main_window.geometry("300x300")
main_window.title("Python Text Replacer")


def openFileDialog():
    global subtitles
    subtitles = filedialog.askopenfilenames(initialdir="/", title="เลือกไฟล์เลยจร้าาา", filetypes=[(
        "Text Files", ".txt .vtt .ass .ssa .srt .ttml .sbv .dfxp .lrc"), ("All Files", "*.*")])
    text.set(str(len(subtitles)) + " file(s) selected.")

def replaceText():
    to_replace = original_text.get()
    replace_with = new_text.get()

    for sub_path in subtitles:
        f = open(sub_path, "r", encoding="utf8", errors="ignore")
        replace_list = [to_replace]  # จะ replace คำว่าอะไรบ้าง
        lst = []
        counter = 0
        for line in f:
            for word in replace_list:
                if word in line:
                    # คำที่จะแทนคำเดิม
                    line = line.replace(word, replace_with)
                    counter += 1
            lst.append(line)
        print(str(counter) + " line(s) replaced")
        f.close()

        f = open(sub_path, "w", encoding="utf8")
        for line in lst:
            f.write(line)
        f.close()
    
    popup = Tk()
    popup.title("Info")
    popup.geometry("200x80")
    label = Label(popup, text=str(counter) + " line(s) replaced", padx=10, pady=10)
    label.pack()
    button = Button(popup, text="OK", command=popup.destroy)
    button.pack()
    popup.mainloop()

thai_font = "Leelawadee"
title = Label(main_window, text="Python Text Replacer V.1")
title.config(font=("sans 16 bold"), pady=20)
choose_file = Button(main_window, text="Choose file(s)",
                        command=openFileDialog)
text = StringVar()
text.set("0 file(s) selected.")
file_selected = Label(main_window, textvariable=text, foreground="grey")
original_text = StringVar()
original = Label(main_window, text="Original:")
original_entry = Entry(main_window, textvariable=original_text, font=thai_font)
new_text = StringVar()
new = Label(main_window, text="Replace with:")
new_entry = Entry(main_window, textvariable=new_text, font=thai_font)
replace_button = Button(main_window, text="Replace text!", width=20, height=2, command=replaceText)


title.pack()
choose_file.pack()
file_selected.pack()
Label(text="").pack()
original.pack()
original_entry.pack()
new.pack()
new_entry.pack()
Label(text="").pack()
replace_button.pack()

main_window.mainloop()
