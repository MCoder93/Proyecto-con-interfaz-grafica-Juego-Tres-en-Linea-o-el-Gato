import tkinter as tk
from tkinter import messagebox

# Variables del juego
player = 'X'
game_over = False

# Función para verificar si hay un ganador
def check_winner(buttons=None):
    for i in range(3):
        # Verifica filas
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != '':
            return True
        # Verifica columnas
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != '':
            return True
    # Verifica diagonales
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        return True
    return False

def button_click(row, col):
    global player, game_over
    if buttons[row][col]['text'] == '' and not game_over:
        buttons[row][col]['text'] = player
        buttons[row][col]['bg'] = '#37474F' if player == 'X' else '#455A64'
        if check_winner(buttons):
            messagebox.showinfo(title='El Gato', message=f'¡Jugador {player} gana!')
            game_over = True
        elif all(buttons[r][c]['text'] != '' for r in range(3) for c in range(3)):
            messagebox.showinfo(title='El Gato', message='¡Es un empate!')
            game_over = True
        else:
            player = 'O' if player == 'X' else 'X'

def reset_game():
    global player, game_over
    player = 'X'
    game_over = False
    for row in range(3):
        for col in range(3):
            buttons[row][col]['text'] = ''
            buttons[row][col]['bg'] = '#263238'

root = tk.Tk()
root.title('Tres en línea')
root.geometry('400x500')
root.configure(bg='#263238')

frame = tk.Frame(root, bg='#263238')
frame.place(relx=0.5, rely=0.4, anchor='center')

buttons = [[tk.Button(frame, text='', font='normal 20 bold', width=5, height=2, bg='#263238', fg='white',
                      command=lambda row=row, col=col: button_click(row, col))
            for col in range(3)] for row in range(3)]

for row in range(3):
    for col in range(3):
        buttons[row][col].grid(row=row, column=col, padx=10, pady=10)

reset_button = tk.Button(root, text='Reiniciar', font='normal 15 bold', command=reset_game, bg='#546E7A', fg='white')
reset_button.place(relx=0.5, rely=0.85, anchor='center')

root.mainloop()



