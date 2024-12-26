import PySimpleGUI as sg
tasks = [] # empty list to hold tasks
user_input = {} # empty dictionary to hold user input
def main (): # main layout and window functions are store within this function
    sg.theme("DarkAmber") # set the theme for the window
menu_def = [['&File', ['&Open     Ctrl-O', '&Save       Ctrl-S', '&Properties', 'E&xit']],
                ['&Edit', ['Edit Me', 'Special', 'Normal',['Normal1', 'Normal2'] , 'Undo']],
                ['!Disabled', ['Special', 'Normal',['Normal1', 'Normal2'], 'Undo']],
                ['&Toolbar', ['---', 'Command &1::Command_Key', 'Command &2', '---', 'Command &3', 'Command &4']],
                ['&Help', ['&About...']], ] # menu definition

layout = [[sg.MenubarCustom(menu_def, pad=(0,0), k='-CUST MENUBAR-')],
              [sg.Multiline(size=(70, 20),  reroute_cprint=True, write_only=True, no_scrollbar=True, k='-MLINE-')],
              # buttons!
              [sg.Button(key=f"-APPEND-", button_text="Save", font='bold 14', bind_return_key=True, k='-BUTTON-')],
              [sg.Button(key=f"-CLEAR-", button_text="Clear", font='bold 14', bind_return_key=True, k='-BUTTON-')],
            ] # custom layout definition

user_input = [for {i} in int(input(getattr("user_input", sg.Multiline)))] # user input for tasks
tasks = [f"Task {i}" for i in range(f"{user_input}")] # defining tasks that need to be appended to this list
listItem = [] # numerically ordering said tasks
sg.Multiline.pack(); # printing the tasks to the window

for i, task in enumerate(tasks):
        listItem.append([sg.Text(tasks), sg.Button("Add", key=f"-APPEND_{i}"), sg.Button("Delete", key=f"-DELETE_{i}-")])
    
layout.extend(listItem)

window = sg.Window("Marcs App", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

window.close()

__name__ == "__main__"
main()