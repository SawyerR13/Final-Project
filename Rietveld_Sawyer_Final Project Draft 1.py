import tkinter as tk
import tkinter.font as tkFont
enemyHealth = 100
playerHealth = 100
displayMessage = "Press a button"
class App:
    def __init__(self, root):
        #setting title
        root.title("Turn Based Game")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        specialButton=tk.Button(root, state="normal", bg="#555555", fg="#ffff00", text= "Special", command=self.specialButton_command)
        ft = tkFont.Font(family='Times',size=22)
        specialButton["font"] = ft
        specialButton["justify"] = "center"
        specialButton.place(x=20,y=440,width=250,height=40)

        healButton=tk.Button(root)
        healButton["bg"] = "#555555"
        ft = tkFont.Font(family='Times',size=22)
        healButton["font"] = ft
        healButton["fg"] = "#00ff00"
        healButton["justify"] = "center"
        healButton["text"] = "Heal"
        healButton.place(x=330,y=440,width=250,height=40)
        healButton["command"] = self.healButton_command

        attackButton=tk.Button(root)
        attackButton["bg"] = "#555555"
        ft = tkFont.Font(family='Times',size=22)
        attackButton["font"] = ft
        attackButton["fg"] = "#ff0000"
        attackButton["justify"] = "center"
        attackButton["text"] = "Attack"
        attackButton.place(x=20,y=390,width=250,height=40)
        attackButton["command"] = self.attackButton_command

        defendButton=tk.Button(root)
        defendButton["bg"] = "#555555"
        ft = tkFont.Font(family='Times',size=22)
        defendButton["font"] = ft
        defendButton["fg"] = "#0000ff"
        defendButton["justify"] = "center"
        defendButton["text"] = "Defend"
        defendButton.place(x=330,y=390,width=250,height=40)
        defendButton["command"] = self.defendButton_command

        messageBox=tk.Message(root)
        messageBox["anchor"] = "w"
        ft = tkFont.Font(family='Times',size=18)
        messageBox["font"] = ft
        messageBox["fg"] = "#333333"
        messageBox["justify"] = "left"
        messageBox["text"] = displayMessage
        messageBox["relief"] = "flat"
        messageBox.place(x=0,y=300,width=600,height=80)

        GMessage_670=tk.Message(root)
        GMessage_670["anchor"] = "e"
        ft = tkFont.Font(family='Times',size=10)
        GMessage_670["font"] = ft
        GMessage_670["fg"] = "#ff0000"
        GMessage_670["justify"] = "right"
        GMessage_670["text"] = "Enemy"
        GMessage_670.place(x=500,y=0,width=100,height=25)

        GMessage_893=tk.Message(root)
        GMessage_893["anchor"] = "e"
        ft = tkFont.Font(family='Times',size=10)
        GMessage_893["font"] = ft
        GMessage_893["fg"] = "#333333"
        GMessage_893["justify"] = "right"
        GMessage_893["text"] = enemyHealth
        GMessage_893.place(x=500,y=30,width=100,height=25)

        GMessage_604=tk.Message(root)
        GMessage_604["anchor"] = "w"
        ft = tkFont.Font(family='Times',size=10)
        GMessage_604["font"] = ft
        GMessage_604["fg"] = "#0000ff"
        GMessage_604["justify"] = "left"
        GMessage_604["text"] = "Player"
        GMessage_604.place(x=0,y=0,width=100,height=25)

        GMessage_462=tk.Message(root)
        GMessage_462["anchor"] = "w"
        ft = tkFont.Font(family='Times',size=10)
        GMessage_462["font"] = ft
        GMessage_462["fg"] = "#333333"
        GMessage_462["justify"] = "left"
        GMessage_462["text"] = playerHealth
        GMessage_462.place(x=0,y=30,width=100,height=25)


    def specialButton_command(self):
        print("Button was pressed")
        displayMessage = "Player used Special"
        return displayMessage

    def healButton_command(self):
        print("Button was pressed")
        displayMessage = "Player Healed"
        return displayMessage

    def attackButton_command(self):
        print("Button was pressed")
        displayMessage = "Player Attacked"
        return displayMessage

    def defendButton_command(self):
        print("Button was pressed")
        displayMessage = "Player Defended"
        return displayMessage

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
    print(displayMessage)
