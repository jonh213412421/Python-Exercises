import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

#simple show/hide img
def simple_show_hide_img():
    def show_image():
        label.config(image=img)
        label.image = img
    def hide_img():
        label.config(image='')
        label.image = img
    # Create the main window
    window = tk.Tk()
    window.geometry("300x600")
    window.title("Image Example")
    # Load the image
    img = Image.open("image.jpg").resize((300,600)) #resize img, replace with path to image file
    img = ImageTk.PhotoImage(img)
    # Create a label to display the image
    label = tk.Label(window, text="Click the button to show the image")
    label.place(anchor='nw')
    # Create a button to show the image
    button1 = tk.Button(window, text="Show Image", command=show_image)
    button1.pack(pady=10)
    # Create a button to hide the image
    button2 = tk.Button(window, text="hide image", command=hide_img)
    button2.pack(pady=20)
    # Start the Tkinter event loop
    window.mainloop()

#show array of images
i = 0 #pointer
def show_array_of_images():
    global i
    images = [] #saves all images in array
    def show_img():
        def back():
            label.config(image='') #back to the initial screen
        global i
        img = filedialog.askopenfilename(title="Select an image") #select image file
        images.append(img) #add img path to array
        img = Image.open(img).resize((1920, 1080)) #open img and change size
        img = ImageTk.PhotoImage(img) #converts
        label.config(image=img) #put img
        label.image = img
        i += 1 #update pointer
        button2 = tk.Button(window, text=f'return', command=back)
        button2.place(y=20, x=200) #add return button over img
        button1.config(text=f'show img {i}')
    def back():
        label.config(image='')
    def last():
        #same logic from show_img function
        global i
        i -=1
        if i < 0:
            i = 0
        img = images[i].replace("/", "\\")
        img = Image.open(img).resize((1920, 1080))
        img = ImageTk.PhotoImage(img)
        label.config(image=img)
        label.image = img
    window = tk.Tk() #main window
    window.title("img show")
    window.geometry("300x300")
    #put ico
    ico_path = "image.jpg" #replace with path to image
    ico = Image.open(ico_path)
    ico = ico.convert("RGBA")
    ico.save(ico_path.replace(".jpg", ".ico"), format="ICO", sizes=[(16,16)]) #convert ico file from jpg file
    ico_path = "image.ico" #replace with path of output ico file
    window.iconbitmap(ico_path) #add ico file
    #buttons
    button1 = tk.Button(window, text=f'show img {i}', command=show_img)
    button1.place(y=30, x=100)
    button2 = tk.Button(window, text=f'return', command=back)
    button2.place(y=20, x=200)
    button3 = tk.Button(window, text='last image', command=last)
    button3.place(y=50, x=200)
    label = tk.Label(window, text="Click the button to show the image")
    label.place(anchor='nw')
    window.mainloop()

if __name__ == "__main__":
    show_array_of_images() #test any function you want
