import cv2
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

def load_image():
    global image_path, original_image
    image_path = filedialog.askopenfilename(initialdir='./', title='Open file',
                                            filetypes=(('JPEG files', '*.jpg'), ('All files', '*.*')))
    if image_path:
        update_image()

def update_image():
    global image_path, original_image
    original_image = cv2.imread(image_path)
    show_image(original_image)

def show_image(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)

    panel.configure(image=img)
    panel.image = img

def apply_patterns():
    global original_image, image_path

    if not image_path:
        messagebox.showerror('Error', 'No image loaded!')
        return

    cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
    cat_face = cat_face_cascade.detectMultiScale(original_image)

    for (x, y, w, h) in cat_face:
        pattern1 = Image.open('pattern1.png')
        pattern1 = pattern1.convert("RGBA")
        pattern1 = pattern1.resize((w, h))
        cv2.rectangle(image, (x, y),(x+w, y+h), (0,0,255), 3)

        pattern2 = Image.open('pattern2.png')
        pattern2 = pattern2.convert("RGBA")
        pattern2 = pattern2.resize((w, h))
        cv2.rectangle(image, (x, y),(x+w, y+h), (0,0,255), 3)

    show_image(original_image)

root = Tk()
root.title("Image Processing")

panel = Label(root)
panel.pack(padx=10, pady=10)

load_button = Button(root, text="Load Image", command=load_image)
load_button.pack(pady=5)

apply_button = Button(root, text="Apply Patterns", command=apply_patterns)
apply_button.pack(pady=5)

exit_button = Button(root, text="Exit", command=root.destroy)
exit_button.pack(pady=5)

root.mainloop()