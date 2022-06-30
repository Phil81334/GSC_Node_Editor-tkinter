from GSC_Node_Editor.node import Node
from GSC_Node_Editor.node_socket import NodeSocket

class NodeValue(Node):
    def __init__(self, canvas, value=0):
        # Node() accepts multiple keyword args so here is where you pass your custom args to override Node()'s default attributes
        super().__init__(canvas=canvas, width=100, height=150, node_outline_colour='white', node_outline_thickness=1, node_colour='#37373D', center=(100,50), text=str(value))
        # 'self' = Node

        self.output_ = NodeSocket(canvas, value=value, radius=10, center=(150,0))
        self.allIDs = self.allIDs + [self.output_.ID]

        self.bind_all_to_movement()
        self.bindtoclick()

    def getvalue(self):
        return self.output_.value

    def bindtoclick(self):
        self.canvas.tag_bind(self.output_.ID, '<Button-1>', self.b1_output)

    def b1_output(self, event):
        #print("one")
        self.canvas.clickcount += 1
        self.canvas.outputcell = self

        if self.canvas.clickcount == 2:
            self.canvas.clickcount = 0
            self.canvas.conectcells()

    def update(self):
        self.canvas.after(50, self.update)

class NodeOperation(Node):
    def __init__(self, canvas, text=None, width=50):
        # Node() accepts multiple keyword args so here is where you pass your custom args to override Node()'s default attributes
        super().__init__(canvas=canvas, width=100, height=150, node_outline_colour='white', node_outline_thickness=1, node_colour='#37373D', center=(100,50), text=text)
        # self = 'Node'
        self.line1 = None
        self.line2 = None
        self.text = text
        self.canvas = canvas

        self.input_1 = NodeSocket(canvas, radius=10, center=(50,0)) # canter=(left-right, up-down)
        self.input_2 = NodeSocket(canvas, radius=10, center=(50,100))
        self.output_ = NodeSocket(canvas, radius=10, center=(150,0))

        self.cellinput1 = None
        self.cellinput2 = None
        self.celloutput = None
        self.allIDs = self.allIDs + [self.output_.ID, self.input_1.ID, self.input_2.ID]
        self.bind_all_to_movement()
        self.bindtoclick()

    def bindtoclick(self):
        self.canvas.tag_bind(self.input_1.ID, '<Button-1>', self.b1_input1)
        self.canvas.tag_bind(self.input_2.ID, '<Button-1>', self.b1_input2)
        self.canvas.tag_bind(self.output_.ID, '<Button-1>', self.b1_output)

    def b1_output(self,event):
        self.canvas.clickcount += 1
        self.canvas.outputcell = self

        if self.canvas.clickcount == 2:
            self.canvas.clickcount = 0
            self.canvas.conectcells()

    def b1_input1(self,event):
        try: self.canvas.delete(self.line1.ID)
        except: None

        self.canvas.clickcount += 1
        self.canvas.IDc = 'input1'
        self.canvas.inputcell = self

        if self.canvas.clickcount == 2:
            self.canvas.clickcount = 0
            self.canvas.conectcells()

    def b1_input2(self, event):
        try: self.canvas.delete(self.line2.ID)
        except: None

        self.canvas.clickcount += 1
        self.canvas.IDc = 'input2'
        self.canvas.inputcell = self

        if self.canvas.clickcount == 2:
            self.canvas.clickcount = 0
            self.canvas.conectcells()

    def update(self):
        try:
            if self.text == 'SUB': self.output_.value = self.cellinput1.output_.value - self.cellinput2.output_.value
            if self.text == 'ADD': self.output_.value = self.cellinput1.output_.value + self.cellinput2.output_.value
        except: None

        self.canvas.after(50, self.update)

class NodeResult(Node):
    def __init__(self, canvas, text='Compile'):
        # Node() accepts multiple keyword args so here is where you pass your custom args to override Node()'s default attributes
        super().__init__(canvas=canvas, width=100, height=150, node_outline_colour='white', node_outline_thickness=1, node_colour='#37373D', center=(100,50), text=text) # -left, +right | -up, +down
        # 'self' = Node

        self.canvas = canvas
        self.text = text
        self.line1 = None
        self.line2 = None
        self.cellinput1 = None
        self.cellinput2 = None
        self.celloutput = None

        self.input_1 = NodeSocket(canvas, radius=10, center=(50,0))
        self.output_ = NodeSocket(canvas, radius=10, center=(150,0))

        self.allIDs = self.allIDs + [self.output_.ID, self.input_1.ID] # [self.input_1.ID]

        self.bind_all_to_movement()
        self.bindtoclick()

    def bindtoclick(self):
        self.canvas.tag_bind(self.input_1.ID, '<Button-1>', self.b1_input1)
        # self.canvas.tag_bind(self.output_.ID, '<Button-1>', self.b1_output)

    def b1_input1(self, event):
        try: self.canvas.delete(self.line1.ID)
        except: None

        self.canvas.clickcount += 1
        self.canvas.IDc = 'input1'
        self.canvas.inputcell = self

        if self.canvas.clickcount == 2:
            self.canvas.clickcount = 0
            self.canvas.conectcells()

    def b1_output(self, event):
        self.canvas.clickcount += 1
        self.canvas.outputcell = self

        if self.canvas.clickcount == 2:
            self.canvas.clickcount = 0
            self.canvas.conectcells()

    def update(self):
        try:
            self.output_.value = self.cellinput1.output_.value
            self.canvas.itemconfigure(self.IDtext, text=str(self.output_.value))
        except: None

        self.canvas.after(50, self.update)