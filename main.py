import PySimpleGUI as sg
sg.theme("LightBrown5")

file = open("profits.txt", "r", encoding="utf-8")
file2 = open("expenses.txt", "r", encoding="utf-8")

profits = file.readlines()
expenses = file2.readlines()

label = sg.Text("Трекер финансов", font=("Times New Roman", 25), text_color="black")
label4 = sg.Text("Доходы", font=("Times New Roman", 20), text_color="black")
label5 = sg.Text("                             Расходы", font=("Times New Roman", 20), text_color="black")
listbox = sg.Listbox(values=profits, key="cash", size=(28, 10), font=("Times New Roman", 15))
listbox2 = sg.Listbox(values=expenses, key="cash2", size=(28, 10), font=("Times New Roman", 15))
label2 = sg.Text("Количество рублей", font=("Times New Roman", 25), text_color="black")
input_money = sg.InputText(key="money",  font=("Times New Roman", 25))
label3 = sg.Text("Цель", font=("Times New Roman", 25), text_color="black")
input_target = sg.InputText(key="tar",  font=("Times New Roman", 25))
button = sg.Button("Доход", font=("Times New Roman", 20))
button2 = sg.Button("Расход", font=("Times New Roman", 20))

window = sg.Window("Трекер финансов",
                   layout=[[label],
                    [label4, label5],
                     [listbox, listbox2],
                    [label2],
                    [input_money],
                    [label3],
                    [input_target],
                    [button, button2]], size=(650, 650))

while True:
    event, values = window.read(timeout=10)

    match event:
        case "Доход":
            money = values["money"]
            target = values["tar"]
            result = money + ' рублей' + ' - ' + target
            profits.append(result)
            listbox.update(profits)
            file = open("profits.txt", "a", encoding="utf-8")
            file.write(result + "\n")
            file.close()

        case "Расход":
            money = values["money"]
            target = values["tar"]
            result = money + ' рублей' + ' - ' + target
            expenses.append(result)
            listbox2.update(expenses)
            file = open("expenses.txt", "a", encoding="utf-8")
            file.write(result + "\n")
            file.close()



        case sg.WIN_CLOSED:
            break

window.close()
