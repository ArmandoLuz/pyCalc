
    """ def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.rows = 3
        self.cols = 1

        self.innergrid = GridLayout()
        self.innergrid2 = GridLayout()

        self.input = TextInput(multiline=False)
        self.hist = Button(text="HIST")
        self.btndelete = Button(text="DEL")
        self.btnc = Button(text="C")
        self.btnParenOpen = Button(text="(")
        self.btnParenClose = Button(text=")")
        self.btnExpo = Button(text="^")
        self.btnmult = Button(text="*")
        
        self.btnequal = Button(text="=")
        self.btndiv = Button(text="/")
        self.btnsum = Button(text="+")
        self.btnsub = Button(text="-")
        self.btn7 = Button(text="7")
        self.btn8 = Button(text="8")
        self.btn9 = Button(text="9")
        self.btn4 = Button(text="4")
        self.btn5 = Button(text="5")
        self.btn6 = Button(text="6")
        self.btn1 = Button(text="1")
        self.btn2 = Button(text="2")
        self.btn3 = Button(text="3")
        self.btn0 = Button(text="0")
        self.btnp = Button(text=".")


        self.add_widget(self.input)
        self.add_widget(self.innergrid2)
        self.add_widget(self.innergrid)

        self.innergrid2.cols = 2
        self.innergrid2.rows = 1

        self.innergrid2.add_widget(self.hist)
        self.innergrid2.add_widget(self.btndelete)

        self.innergrid.cols = 4
        self.innergrid.rows = 5

        
        self.innergrid.add_widget(self.btnExpo)
        self.innergrid.add_widget(self.btnParenOpen)
        self.innergrid.add_widget(self.btnParenClose)
        #self.innergrid.add_widget(self.btnExpo)
        self.innergrid.add_widget(self.btndiv)
        
        self.innergrid.add_widget(self.btn7)
        self.innergrid.add_widget(self.btn8)
        self.innergrid.add_widget(self.btn9)
        self.innergrid.add_widget(self.btnmult)

        self.innergrid.add_widget(self.btn4)
        self.innergrid.add_widget(self.btn5)
        self.innergrid.add_widget(self.btn6)
        self.innergrid.add_widget(self.btnsub)

        self.innergrid.add_widget(self.btn1)
        self.innergrid.add_widget(self.btn2)
        self.innergrid.add_widget(self.btn3)
        self.innergrid.add_widget(self.btnsum)

        self.innergrid.add_widget(self.btnc)
        self.innergrid.add_widget(self.btn0)
        self.innergrid.add_widget(self.btnp)
        self.innergrid.add_widget(self.btnequal)

        self.initialize_events()

    def on_press_btn(self, event):
        #self.input2.text = "A senha ta errada pow"]
        pass

    def initialize_events(self):
        #self.btn.bind(on_press=self.on_press_btn)
        pass """