class NodeSocket:
    def __init__(self, canvas, radius=10, center=(50,50), value=0, connecter_outline_colour='white', connecter_outline_thickness=1, connecter_colour='green'):

        self.canvas = canvas
        self.radius = radius
        self.center = center
        self.value = value

        self.create(connecter_outline_colour, connecter_outline_thickness, connecter_colour)
        self.update()
        self.signal = False

    def getpos(self):
        self.cords = self.canvas.coords(self.ID)
        return (self.cords[0]+self.cords[2])/2, (self.cords[1]+self.cords[3])/2

    def create(self, connecter_outline_colour, connecter_outline_thickness, connecter_colour):
        self.ID = self.canvas.create_oval(
            (self.center[0]-self.radius, self.center[1]-self.radius),
            (self.center[0]+self.radius, self.center[1]+self.radius),
            outline=connecter_outline_colour, width=connecter_outline_thickness, fill=connecter_colour)

        self.canvas.tag_bind(self.ID, '<Enter>', self.enter_socket)
        self.canvas.tag_bind(self.ID, '<Leave>', self.leave_socket)

    def update(self):
        self.cords = self.canvas.coords(self.ID)
        self.center = (self.cords[0]+self.cords[2])/2, (self.cords[1]+self.cords[3])/2

        try:
            if self.signal is False: self.canvas.itemconfigure(self.ID, fill='green')
            if self.signal is True: self.canvas.itemconfigure(self.ID, fill='#B91428')
        except: None

        self.canvas.after(50, self.update)

    def enter_socket(self, event):
        self.signal = True
        # print("socket: cursor entered")

    def leave_socket(self, event):
        self.signal = False
        # print("socket: cursor left")
