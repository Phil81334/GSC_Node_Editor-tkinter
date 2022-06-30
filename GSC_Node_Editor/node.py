class Node:
    def __init__(self, canvas, width=50, height=50, node_outline_colour='white', node_outline_thickness=1, node_colour='grey', center=(100,50), text=''):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.node_outline_colour = node_outline_colour
        self.node_outline_thickness = node_outline_thickness
        self.node_colour = node_colour
        self.text = text
        self.center = center
        self.auxlist = []
        self.signal = False

        self.create()

    def create(self):
        self.ID = self.create_round_rectangle( self.center[0]-self.width*0.5, self.center[1]-self.height*0.5, self.center[0]+self.width*0.5, self.center[1]+self.height*0.5,
                                              radius=25, outline=self.node_outline_colour, width=self.node_outline_thickness, fill=self.node_colour)

        #self.canvas.tag_bind(self.ID, '<Enter>', self.enter_node)
        #self.canvas.tag_bind(self.ID, '<Leave>', self.leave_node)

        self.IDtext = self.canvas.create_text(self.center, fill="white", font=("Courier New", 10), text=self.text)

        self.allIDs = [self.ID, self.IDtext]
        self.auxlist = [self.ID, self.IDtext]
        # print(self.ID)
        # print(self.IDtext)
        # print(self.allIDs)
        # print(self.auxlist)

        # self.canvas.bind("<Button-2>", self.click)

    def create_round_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1+radius, y1, x1+radius, y1, x2-radius, y1, x2-radius, y1, x2, y1, x2, y1+radius, x2, y1+radius, x2, y2-radius, x2, y2-radius, x2, y2,
                  x2-radius, y2, x2-radius, y2, x1+radius, y2, x1+radius, y2, x1, y2, x1, y2-radius, x1, y2-radius, x1, y1+radius, x1, y1+radius, x1, y1]

        return self.canvas.create_polygon(points, **kwargs, smooth=True)

    def click(self, event):
        #currently_clicked = canvas.find_withtag("current")
        #if currently_clicked:
        print(self.canvas.gettags('current')) # the first index will contain your desired output

    def getpos(self):
        self.cords = self.canvas.coords(self.ID)
        return (self.cords[0]+self.cords[2])/2, (self.cords[1]+self.cords[3])/2

    def bind_all_to_movement(self):
        for id_ in self.auxlist:
            self.canvas.tag_bind(id_, '<B1-Motion>', self.mouse_mov)

    def mouse_mov(self, event):
        self.x, self.y = self.getpos()
        self.xmove = event.x - self.x
        self.ymove = event.y - self.y

        for id_ in self.allIDs:
            self.canvas.move(id_, self.xmove, self.ymove)

        self.canvas.after(50, self.update)

    def enter_node(self, event):
        self.canvas.itemconfigure(self.ID, outline='#30D5C8', width=2, fill=self.node_colour)
        # print("node: cursor entered")

    def leave_node(self, event):
        self.canvas.itemconfigure(self.ID, outline=self.node_outline_colour, width=self.node_outline_thickness, fill=self.node_colour)
        # print("node: cursor left")
