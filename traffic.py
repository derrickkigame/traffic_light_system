import tkinter as tk


class TrafficLight:
    def __init__(self, master):
        self.master = master
        self.color = "red"
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=150, height=350, bg="white")
        self.canvas.pack()

        # Red light
        self.red_light = self.canvas.create_oval(25, 25, 75, 75, fill="gray")
        # Yellow light
        self.yellow_light = self.canvas.create_oval(25, 100, 75, 150, fill="gray")
        # Green light
        self.green_light = self.canvas.create_oval(25, 175, 75, 225, fill="gray")

        self.change_color()

    def change_color(self):
        if self.color == "red":
            self.canvas.itemconfig(self.red_light, fill="red")
            self.canvas.itemconfig(self.yellow_light, fill="gray")
            self.canvas.itemconfig(self.green_light, fill="gray")
            self.color = "green"
        elif self.color == "green":
            self.canvas.itemconfig(self.red_light, fill="gray")
            self.canvas.itemconfig(self.yellow_light, fill="gray")
            self.canvas.itemconfig(self.green_light, fill="green")
            self.color = "yellow"
        else:
            self.canvas.itemconfig(self.red_light, fill="gray")
            self.canvas.itemconfig(self.yellow_light, fill="yellow")
            self.canvas.itemconfig(self.green_light, fill="gray")
            self.color = "red"

        self.master.after(1000, self.change_color)

if __name__ == "__main__":
    root = tk.Tk()
    width =800
    height= 800
    tl = TrafficLight(root)
    root.mainloop()
