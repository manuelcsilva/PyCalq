from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Label

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\repos\PyCalq\assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Variáveis globais
o = False
n1 = 0
n2 = 0
op = '+'
text_1 = ''

# Função para realizar cálculos
def calq():
    global n1, n2, op, text_1
    if op == '+':
        r = n1 + n2
    elif op == '-':
        r = n1 - n2
    elif op == 'x':
        r = n1 * n2
    else:
        r = n1 / n2
    text_1 = canvas.create_text(
        20.0,
        30.0,
        anchor="nw",
        text=r,
        fill="#FFFFFF",
        font=("JetBrainsMono-Regular", 15 * -1)
    )
    print(r)

# Função para atualizar o valor do número
def number(t):
    global o, n1, n2
    if not o:
        n1 = t
    else:
        n2 = t

# Função para atualizar a operação
def operacao(t):
    global o, op
    o = True
    op = t

# Função para finalizar o cálculo
def fim():
    calq()

def c():
    global r, text_1
    r = ''
    canvas.delete(text_1)
    o = False
    n1 = 0
    n2 = 0
    op = '+'




window = Tk()
window.title("PyCalq")
window.geometry("256x363")
window.configure(bg = "#0E1016")
window.call("wm", "iconphoto", window._w, PhotoImage(file=relative_to_assets("favicon.png")))


canvas = Canvas(
    window,
    bg = "#0E1016",
    height = 363,
    width = 256,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    256.0,
    85.0,
    fill="#181A20",
    outline="")

button_images = []  # Lista para armazenar as imagens dos botões

for i in range(10):
    image = PhotoImage(file=relative_to_assets(f"button_{i}.png"))
    button_images.append(image)  # Adiciona a imagem à lista
    print(f"Caminho do arquivo da imagem do botão {i}: {relative_to_assets(f'button_{i}.png')}")
    button = Button(
        image=image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda i=i: (print(f"Botão {i} clicado"), number(i)),  # Função lambda modificada
        relief="flat",
        background="#0E1016"
    )
    positions = [(20, 288), 
                 (20, 226), 
                 (76, 226), 
                 (132, 226), 
                 (20, 164), 
                 (76, 164), 
                 (132, 164), 
                 (20, 102), 
                 (76, 102), 
                 (132, 102)]
    xx, yy = positions[i]
    button.place(
        x=xx,
        y=yy,
        width=45.0,
        height=45.0
    )

operations = ['+', '-', 'x', '/']
button_op_images = []  # Lista para armazenar as imagens dos botões

for r, operation in enumerate(operations):
    image = PhotoImage(file=relative_to_assets(f"button_{r+10}.png"))
    button_op_images.append(image)  # Adiciona a imagem à lista
    button = Button(
        image=image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda t=operation: operacao(t),
        relief="flat",
        background="#0E1016"
    )
    operation_positions = [(188, 102), (188, 164), (188, 226), (188, 288)]
    xx1, yy1 = operation_positions[r]
    button.place(x=xx1, y=yy1, width=45, height=45)

# Botão de igual
button_image_equal = PhotoImage(file=relative_to_assets("button_17.png"))
button_equal = Button(
    image=button_image_equal,
    borderwidth=0,
    highlightthickness=0,
    command=fim,
    relief="flat",
    background="#0E1016"
)
button_equal.place(x=76, y=288, width=101, height=45)

# Botão de C
button_image_c = PhotoImage(file=relative_to_assets("button_19.png"))
button_c = Button(
    image=button_image_c,
    borderwidth=0,
    highlightthickness=0,
    command=c,
    relief="flat",
    background="#181A21"
)
button_c.place(x=212, y=30.25, width=24, height=16.01)

window.resizable(False, False)
window.mainloop()