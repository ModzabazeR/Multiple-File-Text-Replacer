# Copyright 2021, ModzabazeR <moddaeng.pps@gmail.com>, All rights reserved.
# เอาโค้ดไปแก้ไข ต่อยอด ส่งต่อได้ตามสบายเลยครับ ส่งมาให้ดูกันด้วยนะ :)
# โปรแกรมนี้จะเขียนไฟล์ทับของเก่าไปเลย เพราะฉะนั้นตรวจสอบให้ดีๆก่อนนะครับ

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
subtitles = filedialog.askopenfilenames(initialdir="/", title="เลือกไฟล์เลยจร้าาา", filetypes=[
                                        ("Text Files", ".txt .vtt .ass .ssa .srt .ttml .sbv .dfxp .lrc"), ("All Files", "*.*")])

for sub_path in subtitles:
    f = open(sub_path, "r", encoding="utf8", errors="ignore")
    replace_list = ["835)"]  # จะ replace คำว่าอะไรบ้าง
    lst = []
    for line in f:
        for word in replace_list:
            if word in line:
                # คำที่จะแทนคำเดิม
                line = line.replace(word, "982.5")
        lst.append(line)
        print("Result: " + line)
    f.close()

    f = open(sub_path, "w", encoding="utf8")
    for line in lst:
        f.write(line)
    f.close()
