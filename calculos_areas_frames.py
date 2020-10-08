from tkinter import *
from PIL import Image, ImageTk
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle
import math


def chama_pt_br():
    root.destroy()

    def calcular_quadrado():
        try:
            rep = int(q.get())**2
            resultado_quadrado.configure(text=rep)
        except:
            resultado_quadrado.configure(text='VALOR INVÁLIDO!')

    def calcular_triangulo():
        try:
            baseVar = int(t_base.get())
            alturaVar = int(t_altura.get())
            rep = str((baseVar * alturaVar)/2)
            resultado_triangulo.configure(text=rep)
        except:
            resultado_triangulo.configure(text='VALOR INVÁLIDO!')

    def calcular_circulo():
        try:
            raioVar = int(c.get())
            piVar = math.pi
            rep = str(raioVar * piVar)
            resultado_circulo.configure(text=rep)
        except:
            resultado_circulo.configure(text='VALOR INVÁLIDO!')

    def calcular_retangulo():
        try:
            baseVar = int(r_base.get())
            alturaVar = int(r_altura.get())
            rep = str(baseVar * alturaVar)
            resultado_retangulo.configure(text=rep)
        except:
            resultado_retangulo.configure(text='VALOR INVÁLIDO!')

    def rtrn():
        root_pt_BR.destroy()
        root.withdraw()

    root_pt_BR = Tk()
    root_pt_BR.title('Cálculo Área')
    root_pt_BR.resizable(False, False)

    style = ThemedStyle(root_pt_BR)
    style.set_theme('scidpurple')

    largura_medida_janela = 460
    altura_medida_janela = 420

    largura_janela = root_pt_BR.winfo_screenwidth()
    altura_janela = root_pt_BR.winfo_screenheight()
    x = int((largura_janela/2) - (largura_medida_janela/2))
    y = int((altura_janela/2) - (altura_medida_janela/2))
    root_pt_BR.geometry(
        f'{largura_medida_janela}x{altura_medida_janela}+{x}+{y}')

    # FRAMES
    quadrado = ttk.LabelFrame(root_pt_BR, text='Quadrado', width=220, height=190)
    quadrado.grid(row=1, column=0, padx=5)
    triangulo = ttk.LabelFrame(root_pt_BR, text='Triângulo', width=220, height=190)
    triangulo.grid(row=1, column=1, padx=5)
    circulo = ttk.LabelFrame(root_pt_BR, text='Circulo', width=220, height=190)
    circulo.grid(row=2, column=0, padx=5, pady=5)
    retangulo = ttk.LabelFrame(root_pt_BR, text='Retângulo', width=220, height=190)
    retangulo.grid(row=2, column=1, padx=5, pady=5)

    quadrado.grid_propagate(False)
    triangulo.grid_propagate(False)
    circulo.grid_propagate(False)
    retangulo.grid_propagate(False)

    root_pt_BR = Label(root_pt_BR, text='CÁLCULO DE ÁREAS', font=('Arial', 16, 'bold'))
    root_pt_BR.grid(row=0, columnspan=2)

    # QUADRADO
    quadrado_img = Image.open('IMGS/formas_geometricas/square.png')
    quadrado_renderizado = ImageTk.PhotoImage(quadrado_img)
    imagem_quadrado = Label(quadrado, image=quadrado_renderizado)
    imagem_quadrado.grid(rowspan=2, column=0)

    label_lado_quadrado = ttk.Label(quadrado, text='Lado')
    label_lado_quadrado.grid(row=3, columnspan=2)

    q = StringVar()

    input_lado_quadrado = ttk.Entry(quadrado, textvariable=q)
    input_lado_quadrado.grid(row=1, column=1)

    botao_quadrado = ttk.Button(
        quadrado, text='Calcular', command=calcular_quadrado)
    botao_quadrado.grid(row=2, columnspan=3, pady=5)

    resultado_quadrado = ttk.Label(
        quadrado, text='', font=('Arial', 16, 'bold'))
    resultado_quadrado.grid(row=3, columnspan=3)

    # TRIÂNGULO
    triangulo_img = Image.open('IMGS/formas_geometricas/triangle-2.png')
    triangulo_renderizado = ImageTk.PhotoImage(triangulo_img)
    imagem_triangulo = Label(triangulo, image=triangulo_renderizado)
    imagem_triangulo.grid(rowspan=4, column=0)

    t_base = StringVar()
    t_altura = StringVar()

    label_base_triangulo = ttk.Label(triangulo, text='Base')
    label_base_triangulo.grid(row=0, column=1)
    input_base_triangulo = ttk.Entry(triangulo, textvariable=t_base)
    input_base_triangulo.grid(row=1, column=1)

    label_altura_triangulo = ttk.Label(triangulo, text='Altura')
    label_altura_triangulo.grid(row=2, column=1)
    input_altura_triangulo = ttk.Entry(triangulo, textvariable=t_altura)
    input_altura_triangulo.grid(row=3, column=1)

    botao_triangulo = ttk.Button(
        triangulo, text='Calcular', command=calcular_triangulo)
    botao_triangulo.grid(row=4, columnspan=3, pady=5)

    resultado_triangulo = ttk.Label(
        triangulo, text='', font=('Arial', 16, 'bold'))
    resultado_triangulo.grid(row=5, columnspan=3)

    # CIRCULO
    circulo_img = Image.open('IMGS/formas_geometricas/circle.png')
    circulo_renderizado = ImageTk.PhotoImage(circulo_img)
    imagem_circulo = Label(circulo, image=circulo_renderizado)
    imagem_circulo.grid(rowspan=2, column=0)

    label_lado_circulo = ttk.Label(circulo, text='Raio')
    label_lado_circulo.grid(row=0, column=1)

    c = StringVar()

    input_lado_circulo = ttk.Entry(circulo, textvariable=c)
    input_lado_circulo.grid(row=1, column=1)

    botao_circulo = ttk.Button(
        circulo, text='Calcular', command=calcular_circulo)
    botao_circulo.grid(row=2, columnspan=3, pady=5)

    resultado_circulo = ttk.Label(circulo, text='', font=('Arial', 16, 'bold'))
    resultado_circulo.grid(row=3, columnspan=3)

    # RETÂNGULO
    retangulo_img = Image.open('IMGS/formas_geometricas/rectangle.png')
    retangulo_renderizado = ImageTk.PhotoImage(retangulo_img)
    imagem_retangulo = Label(retangulo, image=retangulo_renderizado)
    imagem_retangulo.grid(rowspan=4, column=0)

    r_base = StringVar()
    r_altura = StringVar()

    label_base_retangulo = ttk.Label(retangulo, text='Base')
    label_base_retangulo.grid(row=0, column=1)
    input_base_retangulo = ttk.Entry(retangulo, textvariable=r_base)
    input_base_retangulo.grid(row=1, column=1)

    label_altura_retangulo = ttk.Label(retangulo, text='Altura')
    label_altura_retangulo.grid(row=2, column=1)
    input_altura_retangulo = ttk.Entry(retangulo, textvariable=r_altura)
    input_altura_retangulo.grid(row=3, column=1)

    botao_retangulo = ttk.Button(
        retangulo, text='Calcular', command=calcular_retangulo)
    botao_retangulo.grid(row=4, columnspan=3, pady=5)

    resultado_retangulo = ttk.Label(
        retangulo, text='', font=('Arial', 16, 'bold'))
    resultado_retangulo.grid(row=5, columnspan=3)

    bt_return_menu_ptbr = ttk.Button(root_pt_BR, text='Voltar', command=rtrn)
    bt_return_menu_ptbr.grid()

    root_pt_BR.mainloop()


def chama_jp():
    root.destroy()

    def calcular_quadrado():
        try:
            rep = int(q.get())**2
            resultado_quadrado.configure(text=rep)
        except:
            resultado_quadrado.configure(text='無効な値です！')

    def calcular_triangulo():
        try:
            baseVar = int(t_base.get())
            alturaVar = int(t_altura.get())
            rep = str((baseVar * alturaVar)/2)
            resultado_triangulo.configure(text=rep)
        except:
            resultado_triangulo.configure(text='無効な値です！')

    def calcular_circulo():
        try:
            raioVar = int(c.get())
            piVar = math.pi
            rep = str(raioVar * piVar)
            resultado_circulo.configure(text=rep)
        except:
            resultado_circulo.configure(text='無効な値です！')

    def calcular_retangulo():
        try:
            baseVar = int(r_base.get())
            alturaVar = int(r_altura.get())
            rep = str(baseVar * alturaVar)
            resultado_retangulo.configure(text=rep)
        except:
            resultado_retangulo.configure(text='無効な値です！')

    root_jp = Tk()
    root_jp.title('面積計算')
    root_jp.resizable(False, False)

    style = ThemedStyle(root_jp)
    style.set_theme('scidpurple')

    largura_medida_janela = 460
    altura_medida_janela = 420

    largura_janela = root_jp.winfo_screenwidth()
    altura_janela = root_jp.winfo_screenheight()
    x = int((largura_janela/2) - (largura_medida_janela/2))
    y = int((altura_janela/2) - (altura_medida_janela/2))
    root_jp.geometry(f'{largura_medida_janela}x{altura_medida_janela}+{x}+{y}')

    # FRAMES
    quadrado = ttk.LabelFrame(root_jp, text='四角形', width=220, height=190)
    quadrado.grid(row=1, column=0, padx=5)
    triangulo = ttk.LabelFrame(root_jp, text='三角形', width=220, height=190)
    triangulo.grid(row=1, column=1, padx=5)
    circulo = ttk.LabelFrame(root_jp, text='円形', width=220, height=190)
    circulo.grid(row=2, column=0, padx=5, pady=5)
    retangulo = ttk.LabelFrame(root_jp, text='長方形', width=220, height=190)
    retangulo.grid(row=2, column=1, padx=5, pady=5)

    quadrado.grid_propagate(False)
    triangulo.grid_propagate(False)
    circulo.grid_propagate(False)
    retangulo.grid_propagate(False)

    root_jp = Label(root_jp, text='面積計算', font=('Arial', 16, 'bold'))
    root_jp.grid(row=0, columnspan=2)

    # QUADRADO
    quadrado_img = Image.open('IMGS/formas_geometricas/square.png')
    quadrado_renderizado = ImageTk.PhotoImage(quadrado_img)
    imagem_quadrado = Label(quadrado, image=quadrado_renderizado)
    imagem_quadrado.grid(rowspan=2, column=0)

    label_lado_quadrado = ttk.Label(quadrado, text='側面')
    label_lado_quadrado.grid(row=0, column=1)

    q = StringVar()

    input_lado_quadrado = ttk.Entry(quadrado, textvariable=q)
    input_lado_quadrado.grid(row=1, column=1)

    botao_quadrado = ttk.Button(
        quadrado, text='計算する', command=calcular_quadrado)
    botao_quadrado.grid(row=2, columnspan=3, pady=5)

    resultado_quadrado = ttk.Label(
        quadrado, text='', font=('Arial', 16, 'bold'))
    resultado_quadrado.grid(row=3, columnspan=3)

    # TRIÂNGULO
    triangulo_img = Image.open('IMGS/formas_geometricas/triangle-2.png')
    triangulo_renderizado = ImageTk.PhotoImage(triangulo_img)
    imagem_triangulo = Label(triangulo, image=triangulo_renderizado)
    imagem_triangulo.grid(rowspan=4, column=0)

    t_base = StringVar()
    t_altura = StringVar()

    label_base_triangulo = ttk.Label(triangulo, text='ベース')
    label_base_triangulo.grid(row=0, column=1)
    input_base_triangulo = ttk.Entry(triangulo, textvariable=t_base)
    input_base_triangulo.grid(row=1, column=1)

    label_altura_triangulo = ttk.Label(triangulo, text='高さ')
    label_altura_triangulo.grid(row=2, column=1)
    input_altura_triangulo = ttk.Entry(triangulo, textvariable=t_altura)
    input_altura_triangulo.grid(row=3, column=1)

    botao_triangulo = ttk.Button(
        triangulo, text='計算する', command=calcular_triangulo)
    botao_triangulo.grid(row=4, columnspan=3, pady=5)

    resultado_triangulo = ttk.Label(
        triangulo, text='', font=('Arial', 16, 'bold'))
    resultado_triangulo.grid(row=5, columnspan=3)

    # CIRCULO
    circulo_img = Image.open('IMGS/formas_geometricas/circle.png')
    circulo_renderizado = ImageTk.PhotoImage(circulo_img)
    imagem_circulo = Label(circulo, image=circulo_renderizado)
    imagem_circulo.grid(rowspan=2, column=0)

    label_lado_circulo = ttk.Label(circulo, text='半径')
    label_lado_circulo.grid(row=0, column=1)

    c = StringVar()

    input_lado_circulo = ttk.Entry(circulo, textvariable=c)
    input_lado_circulo.grid(row=1, column=1)

    botao_circulo = ttk.Button(
        circulo, text='計算する', command=calcular_circulo)
    botao_circulo.grid(row=2, columnspan=3, pady=5)

    resultado_circulo = ttk.Label(circulo, text='', font=('Arial', 16, 'bold'))
    resultado_circulo.grid(row=3, columnspan=3)

    # RETÂNGULO
    retangulo_img = Image.open('IMGS/formas_geometricas/rectangle.png')
    retangulo_renderizado = ImageTk.PhotoImage(retangulo_img)
    imagem_retangulo = Label(retangulo, image=retangulo_renderizado)
    imagem_retangulo.grid(rowspan=4, column=0)

    r_base = StringVar()
    r_altura = StringVar()

    label_base_retangulo = ttk.Label(retangulo, text='ベース')
    label_base_retangulo.grid(row=0, column=1)
    input_base_retangulo = ttk.Entry(retangulo, textvariable=r_base)
    input_base_retangulo.grid(row=1, column=1)

    label_altura_retangulo = ttk.Label(retangulo, text='高さ')
    label_altura_retangulo.grid(row=2, column=1)
    input_altura_retangulo = ttk.Entry(retangulo, textvariable=r_altura)
    input_altura_retangulo.grid(row=3, column=1)

    botao_retangulo = ttk.Button(
        retangulo, text='計算する', command=calcular_retangulo)
    botao_retangulo.grid(row=4, columnspan=3, pady=5)

    resultado_retangulo = ttk.Label(
        retangulo, text='', font=('Arial', 16, 'bold'))
    resultado_retangulo.grid(row=5, columnspan=3)

    root_jp.mainloop()


def chama_en():
    root.destroy()

    def calcular_quadrado():
        try:
            rep = int(q.get())**2
            resultado_quadrado.configure(text=rep)
        except:
            resultado_quadrado.configure(text='INVALID VALUE!')

    def calcular_triangulo():
        try:
            baseVar = int(t_base.get())
            alturaVar = int(t_altura.get())
            rep = str((baseVar * alturaVar)/2)
            resultado_triangulo.configure(text=rep)
        except:
            resultado_triangulo.configure(text='INVALID VALUE!')

    def calcular_circulo():
        try:
            raioVar = int(c.get())
            piVar = math.pi
            rep = str(raioVar * piVar)
            resultado_circulo.configure(text=rep)
        except:
            resultado_circulo.configure(text='INVALID VALUE!')

    def calcular_retangulo():
        try:
            baseVar = int(r_base.get())
            alturaVar = int(r_altura.get())
            rep = str(baseVar * alturaVar)
            resultado_retangulo.configure(text=rep)
        except:
            resultado_retangulo.configure(text='INVALID VALUE!')

    root_en = Tk()
    root_en.title('Area Calculation')
    root_en.resizable(False, False)

    style = ThemedStyle(root_en)
    style.set_theme('scidpurple')

    largura_medida_janela = 460
    altura_medida_janela = 420

    largura_janela = root_en.winfo_screenwidth()
    altura_janela = root_en.winfo_screenheight()
    x = int((largura_janela/2) - (largura_medida_janela/2))
    y = int((altura_janela/2) - (altura_medida_janela/2))
    root_en.geometry(f'{largura_medida_janela}x{altura_medida_janela}+{x}+{y}')

    # FRAMES
    quadrado = ttk.LabelFrame(root_en, text='Square', width=220, height=190)
    quadrado.grid(row=1, column=0, padx=5)
    triangulo = ttk.LabelFrame(root_en, text='Triangle', width=220, height=190)
    triangulo.grid(row=1, column=1, padx=5)
    circulo = ttk.LabelFrame(root_en, text='Circle', width=220, height=190)
    circulo.grid(row=2, column=0, padx=5, pady=5)
    retangulo = ttk.LabelFrame(
        root_en, text='Rectangle', width=220, height=190)
    retangulo.grid(row=2, column=1, padx=5, pady=5)

    quadrado.grid_propagate(False)
    triangulo.grid_propagate(False)
    circulo.grid_propagate(False)
    retangulo.grid_propagate(False)

    root_en = Label(root_en, text='Area Calculation',
                    font=('Arial', 16, 'bold'))
    root_en.grid(row=0, columnspan=2)

    # QUADRADO
    quadrado_img = Image.open('IMGS/formas_geometricas/square.png')
    quadrado_renderizado = ImageTk.PhotoImage(quadrado_img)
    imagem_quadrado = Label(quadrado, image=quadrado_renderizado)
    imagem_quadrado.grid(rowspan=2, column=0)

    label_lado_quadrado = ttk.Label(quadrado, text='Side')
    label_lado_quadrado.grid(row=0, column=1)

    q = StringVar()

    input_lado_quadrado = ttk.Entry(quadrado, textvariable=q)
    input_lado_quadrado.grid(row=1, column=1)

    botao_quadrado = ttk.Button(
        quadrado, text='Calculate', command=calcular_quadrado)
    botao_quadrado.grid(row=2, columnspan=3, pady=5)

    resultado_quadrado = ttk.Label(
        quadrado, text='', font=('Arial', 16, 'bold'))
    resultado_quadrado.grid(row=3, columnspan=3)

    # TRIÂNGULO
    triangulo_img = Image.open('IMGS/formas_geometricas/triangle-2.png')
    triangulo_renderizado = ImageTk.PhotoImage(triangulo_img)
    imagem_triangulo = Label(triangulo, image=triangulo_renderizado)
    imagem_triangulo.grid(rowspan=4, column=0)

    t_base = StringVar()
    t_altura = StringVar()

    label_base_triangulo = ttk.Label(triangulo, text='Base')
    label_base_triangulo.grid(row=0, column=1)
    input_base_triangulo = ttk.Entry(triangulo, textvariable=t_base)
    input_base_triangulo.grid(row=1, column=1)

    label_altura_triangulo = ttk.Label(triangulo, text='Height')
    label_altura_triangulo.grid(row=2, column=1)
    input_altura_triangulo = ttk.Entry(triangulo, textvariable=t_altura)
    input_altura_triangulo.grid(row=3, column=1)

    botao_triangulo = ttk.Button(
        triangulo, text='Calculate', command=calcular_triangulo)
    botao_triangulo.grid(row=4, columnspan=3, pady=5)

    resultado_triangulo = ttk.Label(
        triangulo, text='', font=('Arial', 16, 'bold'))
    resultado_triangulo.grid(row=5, columnspan=3)

    # CIRCULO
    circulo_img = Image.open('IMGS/formas_geometricas/circle.png')
    circulo_renderizado = ImageTk.PhotoImage(circulo_img)
    imagem_circulo = Label(circulo, image=circulo_renderizado)
    imagem_circulo.grid(rowspan=2, column=0)

    label_lado_circulo = ttk.Label(circulo, text='Radius')
    label_lado_circulo.grid(row=0, column=1)

    c = StringVar()

    input_lado_circulo = ttk.Entry(circulo, textvariable=c)
    input_lado_circulo.grid(row=1, column=1)

    botao_circulo = ttk.Button(
        circulo, text='Calculate', command=calcular_circulo)
    botao_circulo.grid(row=2, columnspan=3, pady=5)

    resultado_circulo = ttk.Label(circulo, text='', font=('Arial', 16, 'bold'))
    resultado_circulo.grid(row=3, columnspan=3)

    # RETÂNGULO
    retangulo_img = Image.open('IMGS/formas_geometricas/rectangle.png')
    retangulo_renderizado = ImageTk.PhotoImage(retangulo_img)
    imagem_retangulo = Label(retangulo, image=retangulo_renderizado)
    imagem_retangulo.grid(rowspan=4, column=0)

    r_base = StringVar()
    r_altura = StringVar()

    label_base_retangulo = ttk.Label(retangulo, text='Base')
    label_base_retangulo.grid(row=0, column=1)
    input_base_retangulo = ttk.Entry(retangulo, textvariable=r_base)
    input_base_retangulo.grid(row=1, column=1)

    label_altura_retangulo = ttk.Label(retangulo, text='Height')
    label_altura_retangulo.grid(row=2, column=1)
    input_altura_retangulo = ttk.Entry(retangulo, textvariable=r_altura)
    input_altura_retangulo.grid(row=3, column=1)

    botao_retangulo = ttk.Button(
        retangulo, text='Calculate', command=calcular_retangulo)
    botao_retangulo.grid(row=4, columnspan=3, pady=5)

    resultado_retangulo = ttk.Label(
        retangulo, text='', font=('Arial', 16, 'bold'))
    resultado_retangulo.grid(row=5, columnspan=3)

    root_en.mainloop()


def chama_kr():
    root.destroy()

    def calcular_quadrado():
        try:
            rep = int(q.get())**2
            resultado_quadrado.configure(text=rep)
        except:
            resultado_quadrado.configure(text='잘못된 값!')

    def calcular_triangulo():
        try:
            baseVar = int(t_base.get())
            alturaVar = int(t_altura.get())
            rep = str((baseVar * alturaVar)/2)
            resultado_triangulo.configure(text=rep)
        except:
            resultado_triangulo.configure(text='잘못된 값!')

    def calcular_circulo():
        try:
            raioVar = int(c.get())
            piVar = math.pi
            rep = str(raioVar * piVar)
            resultado_circulo.configure(text=rep)
        except:
            resultado_circulo.configure(text='잘못된 값!')

    def calcular_retangulo():
        try:
            baseVar = int(r_base.get())
            alturaVar = int(r_altura.get())
            rep = str(baseVar * alturaVar)
            resultado_retangulo.configure(text=rep)
        except:
            resultado_retangulo.configure(text='잘못된 값!')

    root_kr = Tk()
    root_kr.title('면적 계산')
    root_kr.resizable(False, False)

    style = ThemedStyle(root_kr)
    style.set_theme('scidpurple')

    largura_medida_janela = 460
    altura_medida_janela = 420

    largura_janela = root_kr.winfo_screenwidth()
    altura_janela = root_kr.winfo_screenheight()
    x = int((largura_janela/2) - (largura_medida_janela/2))
    y = int((altura_janela/2) - (altura_medida_janela/2))
    root_kr.geometry(f'{largura_medida_janela}x{altura_medida_janela}+{x}+{y}')

    # FRAMES
    quadrado = ttk.LabelFrame(root_kr, text='광장', width=220, height=190)
    quadrado.grid(row=1, column=0, padx=5)
    triangulo = ttk.LabelFrame(root_kr, text='삼각형', width=220, height=190)
    triangulo.grid(row=1, column=1, padx=5)
    circulo = ttk.LabelFrame(root_kr, text='원', width=220, height=190)
    circulo.grid(row=2, column=0, padx=5, pady=5)
    retangulo = ttk.LabelFrame(root_kr, text='직사각형', width=220, height=190)
    retangulo.grid(row=2, column=1, padx=5, pady=5)

    quadrado.grid_propagate(False)
    triangulo.grid_propagate(False)
    circulo.grid_propagate(False)
    retangulo.grid_propagate(False)

    root_kr = Label(root_kr, text='면적 계산', font=('Arial', 16, 'bold'))
    root_kr.grid(row=0, columnspan=2)

    # QUADRADO
    quadrado_img = Image.open('IMGS/formas_geometricas/square.png')
    quadrado_renderizado = ImageTk.PhotoImage(quadrado_img)
    imagem_quadrado = Label(quadrado, image=quadrado_renderizado)
    imagem_quadrado.grid(rowspan=2, column=0)

    label_lado_quadrado = ttk.Label(quadrado, text='측면')
    label_lado_quadrado.grid(row=0, column=1)

    q = StringVar()

    input_lado_quadrado = ttk.Entry(quadrado, textvariable=q)
    input_lado_quadrado.grid(row=1, column=1)

    botao_quadrado = ttk.Button(
        quadrado, text='계산하다', command=calcular_quadrado)
    botao_quadrado.grid(row=2, columnspan=3, pady=5)

    resultado_quadrado = ttk.Label(
        quadrado, text='', font=('Arial', 16, 'bold'))
    resultado_quadrado.grid(row=3, columnspan=3)

    # TRIÂNGULO
    triangulo_img = Image.open('IMGS/formas_geometricas/triangle-2.png')
    triangulo_renderizado = ImageTk.PhotoImage(triangulo_img)
    imagem_triangulo = Label(triangulo, image=triangulo_renderizado)
    imagem_triangulo.grid(rowspan=4, column=0)

    t_base = StringVar()
    t_altura = StringVar()

    label_base_triangulo = ttk.Label(triangulo, text='기지')
    label_base_triangulo.grid(row=0, column=1)
    input_base_triangulo = ttk.Entry(triangulo, textvariable=t_base)
    input_base_triangulo.grid(row=1, column=1)

    label_altura_triangulo = ttk.Label(triangulo, text='높이')
    label_altura_triangulo.grid(row=2, column=1)
    input_altura_triangulo = ttk.Entry(triangulo, textvariable=t_altura)
    input_altura_triangulo.grid(row=3, column=1)

    botao_triangulo = ttk.Button(
        triangulo, text='계산하다', command=calcular_triangulo)
    botao_triangulo.grid(row=4, columnspan=3, pady=5)

    resultado_triangulo = ttk.Label(
        triangulo, text='', font=('Arial', 16, 'bold'))
    resultado_triangulo.grid(row=5, columnspan=3)

    # CIRCULO
    circulo_img = Image.open('IMGS/formas_geometricas/circle.png')
    circulo_renderizado = ImageTk.PhotoImage(circulo_img)
    imagem_circulo = Label(circulo, image=circulo_renderizado)
    imagem_circulo.grid(rowspan=2, column=0)

    label_lado_circulo = ttk.Label(circulo, text='반경')
    label_lado_circulo.grid(row=0, column=1)

    c = StringVar()

    input_lado_circulo = ttk.Entry(circulo, textvariable=c)
    input_lado_circulo.grid(row=1, column=1)

    botao_circulo = ttk.Button(
        circulo, text='계산하다', command=calcular_circulo)
    botao_circulo.grid(row=2, columnspan=3, pady=5)

    resultado_circulo = ttk.Label(circulo, text='', font=('Arial', 16, 'bold'))
    resultado_circulo.grid(row=3, columnspan=3)

    # RETÂNGULO
    retangulo_img = Image.open('IMGS/formas_geometricas/rectangle.png')
    retangulo_renderizado = ImageTk.PhotoImage(retangulo_img)
    imagem_retangulo = Label(retangulo, image=retangulo_renderizado)
    imagem_retangulo.grid(rowspan=4, column=0)

    r_base = StringVar()
    r_altura = StringVar()

    label_base_retangulo = ttk.Label(retangulo, text='기지')
    label_base_retangulo.grid(row=0, column=1)
    input_base_retangulo = ttk.Entry(retangulo, textvariable=r_base)
    input_base_retangulo.grid(row=1, column=1)

    label_altura_retangulo = ttk.Label(retangulo, text='높이')
    label_altura_retangulo.grid(row=2, column=1)
    input_altura_retangulo = ttk.Entry(retangulo, textvariable=r_altura)
    input_altura_retangulo.grid(row=3, column=1)

    botao_retangulo = ttk.Button(
        retangulo, text='계산하다', command=calcular_retangulo)
    botao_retangulo.grid(row=4, columnspan=3, pady=5)

    resultado_retangulo = ttk.Label(
        retangulo, text='', font=('Arial', 16, 'bold'))
    resultado_retangulo.grid(row=5, columnspan=3)

    root_kr.mainloop()

root = Tk()

style = ThemedStyle(root)
style.set_theme('scidpurple')

# IMAGENS BOTÕES
bt_img_ptbr = ImageTk.PhotoImage(Image.open(
    "IMGS/formas_geometricas/linguas/portugues.png"))
bt_img_jp = ImageTk.PhotoImage(Image.open(
    "IMGS/formas_geometricas/linguas/japones.png"))
bt_img_en = ImageTk.PhotoImage(Image.open(
    "IMGS/formas_geometricas/linguas/ingles.png"))
bt_img_es = ImageTk.PhotoImage(Image.open(
    "IMGS/formas_geometricas/linguas/espanhol.png"))
bt_img_it = ImageTk.PhotoImage(Image.open(
    "IMGS/formas_geometricas/linguas/italiano.png"))
bt_img_kr = ImageTk.PhotoImage(Image.open(
    "IMGS/formas_geometricas/linguas/coreano.png"))

# ESTILOS BOTÕES
bt_style = ttk.Style()
bt_style.configure('estilo_bt.TButton', font=('Arial', 16, 'bold'))

# BOTÕES MENU PRINCIPAL
botao_pt_br = ttk.Button(
    root, text='Português Brasileiro', command=chama_pt_br, image=bt_img_ptbr, compound="left", style='estilo_bt.TButton', width=20)
botao_pt_br.grid(row=0, column=0)

botao_jp = ttk.Button(root, text='日本語', command=chama_jp,
                      image=bt_img_jp, compound="left", style='estilo_bt.TButton', width=20)
botao_jp.grid(row=1, column=0)

botao_en = ttk.Button(root, text='English', command=chama_en, image=bt_img_en,
                      compound="left", style='estilo_bt.TButton', width=20)
botao_en.grid(row=2, column=0)

botao_kr = ttk.Button(root, text='한국어', command=chama_kr, image=bt_img_kr,
                      compound="left", style='estilo_bt.TButton', width=20)
botao_kr.grid(row=3, column=0)


root.mainloop()
