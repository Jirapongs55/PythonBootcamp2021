# GUI Library
from tkinter import *
from tkinter import ttk

# Googletrans Library
from googletrans import Translator


translator = Translator()


GUI = Tk()
GUI.geometry("500x300")
GUI.title("โปรแกรมแปลคำศัพท์ by K'Jirapong")


# ------Config-------
font_1 = ("Century Gothic", 12)
font_2 = ("Century Gothic", 24)


# ------Label 1------
L1 = ttk.Label(GUI, text = "กรุณากรอกคำศัพท์ที่ต้องการ", font = font_1)
L1.pack()


# ------Entry (ปุ่มให้ user กรอกคำที่ต้องการแปล)------
v_vocab = StringVar()
E1 = ttk.Entry(GUI, textvariable = v_vocab, font = font_1, width = 24)
E1.pack(pady = 10)


def translate():
    vocab = v_vocab.get()   # ดึงข้อมูลจากตัวแปรที่เก็บค่าที่ u ser กรอกเข้ามา
    meaning = translator.translate(vocab, dest = "th")  # ใช้ฟังก์ชันแปลคำศัพท์จาก googletrans
    v_result.set(meaning.text)   # assign ค่าที่แปลได้เข้าไปในตัวแปรที่แสดงผลใน Label 2


# ------Button (ปุ่มคำสั่งให้กดแปล)------
B1 = ttk.Button(GUI, text = "Translate", command = translate)
B1.pack(ipadx = 20, ipady = 10)


# ------Label 2------
v_result = StringVar()
L2 = ttk.Label(GUI, textvariable = v_result, font = font_2, foreground = "crimson" )
L2.pack()


GUI.mainloop()  # คำสั่งในการให้ GUI รันตลอดเวลา (ใช้เป็นบรรทัดจบ)


































































