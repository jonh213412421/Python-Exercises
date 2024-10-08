import tkinter

#Basic Structure
def simple_window():
    window = tkinter.Tk()
    window.geometry('300x300') #edit geometry (300x300 window)
    window.mainloop()

#Add button (without function)
def window_with_button():
    window = tkinter.Tk()
    window.geometry('300x300') #edit geometry (300x300 window)
    Button = tkinter.Button(window, text="test")
    Button.place(x=200, y=100) #button position
    window.mainloop()

#Add Label (simple text)
def window_with_label():
    window = tkinter.Tk()
    window.geometry('300x300+300+300')
    Label = tkinter.Label(window, text="test label") #Label position
    Label.place(x=200, y=100)
    window.mainloop()

#Add button (prints "hi")
def window_with_button_and_function():
    def hi():
        print("hi")
    window = tkinter.Tk()
    window.geometry('300x300+300+300')
    Button = tkinter.Button(window, text="test", command=hi)
    Button.place(x=200, y=100) #button position
    window.mainloop()

i = 0 #global i for window_with_button_Label_and_function()

def window_with_button_Label_and_function():
    def update_label():
        global i
        Label.configure(text=f"you clicked {i} times")
        i+=1
    window = tkinter.Tk()
    window.geometry('300x300+300+300')
    Label = tkinter.Label(window, text="test label") #Label position
    Label.place(x=100, y=100) #label position
    Button = tkinter.Button(window, text="test", command=update_label)
    Button.place(x=200, y=100) #button position
    window.mainloop()

def window_with_entry():
    window = tkinter.Tk()
    window.geometry('300x300+300+300')
    entry = tkinter.Entry(textvariable="test")
    entry.insert(0,"test") #if you wanto to insert text into an entry box
    entry.place(x=100, y=100) #entry position
    window.mainloop()

#more complex implementation
words = [] #array with words
i = 0 #pointer1

def test_window():
    def next_word():
        try:
            global words
            global i
            i = i + 1 #keep track current word
            if i > len(words):
                i = len(words)
            print(f"pointer: {i}")
            word = words[i]
            Bar.delete(0, tkinter.END) #delete what was written before
            Bar.insert(0, word) #write next word
        except Exception as e:
            print(e)
    def last_word():
        try:
            global words
            global i
            if i == len(words):
                i = i -1
            i = i -1 #keep track current word
            print(f"pointer: {i}")
            if i < 0:
                i = 0
            word = words[i]
            Bar.delete(0, tkinter.END) #delete what was written before
            Bar.insert(0, word) #write last word
        except Exception as e:
            print(e)
    def go():
        global words
        global i
        words.append(Bar.get()) #array gets word typed
        i = len(words) #i equals array lenght
        print(f"pointer: {i}")
        print(f"array: {words}")
    window = tkinter.Tk()
    screen_width = window.winfo_screenwidth()
    print(screen_width)
    screen_height = window.winfo_screenheight()
    print(screen_height)
    window.geometry(f"{screen_width}x{screen_height}")
    window.state('normal') #start in small window
    window.title("test window") #title
    Bar = tkinter.Entry(window, justify='left')
    Bar.place(relwidth=0.8) #relative width Bar
    Bar.insert(0,"type a word")
    Button_1 = tkinter.Button(window, text="next", command=next_word) #place next button
    Button_1.place(relx=0.83, rely=0) #relx = relativex and so on
    Button_2 = tkinter.Button(window, text="last", command=last_word) #place last button
    Button_2.place(relx=0.81, rely=0)
    Button_3 = tkinter.Button(window, text="go", command=go, width=10) #place go button
    Button_3.place(relx=0.5, rely=0.03)
    window.mainloop()

if __name__ = '__main__':
    test_window() #test the function you want
