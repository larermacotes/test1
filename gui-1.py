import PySimpleGUI as sg # først må dette installeres ved å kjøre (fra CMD):
# pip install pysimplegui
# or
# pip3 install pysimplegui

# Oppsett av layoutet
layout = [[sg.Text("Skriv inn tekst:"), sg.InputText(key="-INPUT-")],
          [sg.Text(size=(40,1), key="-OUTPUT-")],
          [sg.Button('Lukk')]]

# Opprett et vindu med layoutet
window = sg.Window('Tekstboks eksempel', layout, finalize=True)
window['-INPUT-'].bind("<Return>", "_Enter")

# Hovedløkken
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Lukk':
        break
    elif event == "-INPUT-" + "_Enter":
        print(values["-INPUT-"]) 
        window["-OUTPUT-"].update(values["-INPUT-"])
# Lukk vinduet
window.close()
