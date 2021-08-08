"""
                        TIC-TAC-TOE
                =========================
                |   a1  |   a2  |   a3  |
                =========================
                |   b1  |   b2  |   b3  |
                =========================
                |   c1  |   c2  |   c3  |
                =========================
"""
import PySimpleGUI as sg

sg.theme("DarkAmber")

while True:
    layout = [[sg.Button(key="a1", size=(10, 6)), sg.Button(key="a2", size=(10, 6)), sg.Button(key="a3", size=(10, 6))],
              [sg.Button(key="b1", size=(10, 6)), sg.Button(key="b2", size=(10, 6)), sg.Button(key="b3", size=(10, 6))],
              [sg.Button(key="c1", size=(10, 6)), sg.Button(key="c2", size=(10, 6)), sg.Button(key="c3", size=(10, 6))]]

    event , values = sg.Window("Tic-Tac-Toe",font=("Times New Roman",11),
                               layout=[[sg.T("Enter Names of the Players")],
                                       [sg.T("Player 1 :"),sg.In(key="p1",default_text="Player 1")],
                                       [sg.T("Player 2 :"),sg.In(key="p2",default_text="Player 2")],
                                       [sg.Submit()]],element_justification="center").read(close=True)
    if event == sg.WIN_CLOSED :
        exit()
    player1 = values["p1"]
    player2 = values["p2"]

    window = sg.Window("Tic-Tac-Toe", layout,size=(310,350),font=("Times New Roman",11))

    winning_moves = [["a1", "a2", "a3"], ["b1", "b2", "b3"], ["c1", "c2", "c3"],
                     ["a1", "b1", "c1"], ["a2", "b2", "c2"], ["a3", "b3", "c3"],
                     ["a1", "b2", "c3"], ["c1", "b2", "a3"]]
    victory = False
    p1_moves = []
    p2_moves = []
    moves_available = ["a1","a2","a3","b1","b2","b3","c1","c2","c3"]

    while True :
        event, values = window.read()
        if event == sg.WIN_CLOSED :
            break
        print(event)
        if event not in p2_moves :
            p1_moves.append(event)
            moves_available.remove(event)
            window[event].update("X")
            print("p1_moves =", p1_moves)
        else :
            continue
        for x in winning_moves :
            if all(item in p1_moves for item in x):
                victory = True
                sg.popup("Congrats "+player1+" won.")
        if victory:
            break
        elif len(moves_available) == 0 :
            sg.popup("That's a Tie")
            break
        event, values = window.read()
        if event == sg.WIN_CLOSED :
            break
        print(event)
        if event not in p1_moves :
            p2_moves.append(event)
            moves_available.remove(event)
            window[event].update("O")
            print("p2_moves =", p2_moves)
        else :
            continue
        for x in winning_moves :
            if all(item in p2_moves for item in x):
                victory = True
                sg.popup("Congrats "+player2+" won.")
        if victory:
            break
        elif len(moves_available) == 0 :
            sg.popup("That's a Tie")
            break
    window.close()

    event, values = sg.Window("Tic-Tac-Toe", font=("Times New Roman", 11),
                              layout=[[sg.T("Do you want to play again?")],
                                      [sg.B("Yes"),sg.B("No")]],element_justification="center").read(close=True)
    if event == "Yes" :
        continue
    else:
        break
