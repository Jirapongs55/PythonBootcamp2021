# GUITranslator.py
from tkinter import *   # จากไลบรารีชื่อ tkinter, * คือให้ดึงความสามารถทั้งหมดมา
from tkinter import ttk # ดึง theme ที่ modern มากขึ้นมา

from googletrans import Translator


translator = Translator()
    

GUI = Tk()  # คำสั่งในการสร้างหน้าต่างหลัก
GUI.geometry("500x300") # .geometry คือคำสั่งขยายขนาดหน้าจอ "กว้างxสูง"
GUI.title("โปรแกรมแปลภาษา by Jirapong's")


# -------Config-------- 
font_1 = ("Century Gothic", 12)
font_2 = ("Century Gothic", 24)


# -------Label 1-------
L1 = ttk.Label(GUI, text = "กรุณากรอกคำศัพท์ที่ต้องการ", font = font_1 )
L1.pack()


# --------Entry(ช่องกรอกข้อความ)-------
v_vocab = StringVar()   # เปรียบเหมือนเป็นกล่องเก็บข้อความ
E1 = ttk.Entry(GUI, textvariable = v_vocab, font = font_1, width = 40)
E1.pack(ipadx = 20, ipady = 10, pady = 10)


# --------Button(ปุ่มกดให้แปล)---------
def translate():
    vocab = v_vocab.get()   # .get() คือคำสั่งให้ดึงข้อมูลที่เก็บจาก StringVar() มาใช้
    meaning = translator.translate(vocab, dest = "th")
    v_result.set(vocab + " : " + meaning.text)  # .set() คือคำสั่งให้ตัวแปร v_result มีค่าเปลี่ยนแปลงไปตามสิ่งที่อยู่ใน .set()
    

B1 = ttk.Button(GUI, text = "Translate", command = translate)    # สร้างปุ่มขึ้นมา
B1.pack(ipadx = 20, ipady = 10, pady = 10)   # Show ปุ่มขึ้นมา โดยวางจาก บน-->ล่าง


# -------Label 2-------
L2 = ttk.Label(GUI,text = "คำแปล", font = font_1)
L2.pack()


# -------Result-------
v_result = StringVar()  # นี่คือกล่องสำหรับเก็บคำแปล
R1 = ttk.Label(GUI, textvariable = v_result, font = font_2, foreground = "blue")
R1.pack()


GUI.mainloop()  # คำสั่งทำให้โปรแกรมรันได้ตลอดเวลาจนกว่าจะปิด (ต้องอยู่บรรทัดจบเท่านั้น!!!)








































































