from tkinter import *
from chat import get_response, bot_name
import imageio
import tensorflow
import numpy as np
from PIL import Image
import cv2
CLASSES = ["Apple scab","Apple Black rot","Apple cedar rust","Apple healthy","Blackgram Anthracnose","Blackgram Leaf crinkle","Blackgram Powdery Mildew","Blackgram Yellow Mosaic","Blackgram healthy","Blueberry healthy","Cherry Powdery Mildew",
           "Cherry Healthy","Corn leaf spot","Corn Common rust","Corn northern leaf blight","Corn healthy","Grape black rot","Grape esca","Grape leaf blight",
           "Grape healthy","Orange Haunglongbing","Peach bacterial spot","Peach healthy","Pepper bell bacterial spot","Pepper bell healthy","Potato early blight",
           "Potato late blight","Potato healthy","Raspberry healthy","Soybean healthy","Squash powdery mildew","Strawberry leaf scotch","Strawberry healthy","Tomato bacterial spot",
           "Tomato early blight","Tomato late blight","Tomato leak mould","Tomato septoria leaf spot","Tomato spider mite","Tomato target spot","Tomato yellow leaf curl virus","Tomato mosaic","Tomato healthy"]

BG_GRAY = "#C9AE5D"
BG_COLOR = "#F7E7CE"
TEXT_COLOR = "#665D1E"
FONT = "Georgia 18"
FONT_BOLD = "Georgia 18 bold"

class ChatApplication:
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
    def run(self):
        self.window.mainloop()
    def _setup_main_window(self):
        self.window.title("MAIN")
        self.window.resizable(width=True, height=True)
        self.window.configure(width=1920, height=1080, bg=BG_COLOR)
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Plant Disease Repository", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow")

        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)
        bottom_label = Label(self.window, bg=BG_GRAY, height=100)
        bottom_label.place(relwidth=1, rely=0.825)
        self.msg_entry = Entry(bottom_label, bg="#BAB86C", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        send_button = Button(bottom_label, text="Submit", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

        m="You"
        self.msg_entry.delete(0, END)
        msg1 = f"{m}: {res}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"{bot_name}: {get_response(res)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")
    def _insert_message(self, msg, sender):
        if not msg:
            return
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)

def run(source=None):
    model = tensorflow.keras.models.load_model('reseven.h5')
    image = imageio.imread(source)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    thresh = cv2.bitwise_not(thresh)
    mask = cv2.merge((thresh, thresh, thresh))
    result = cv2.bitwise_and(image, mask)
    cv2.imshow('hi',result)

    img = Image.fromarray(image).resize((224, 224))
    input_arr = tensorflow.keras.preprocessing.image.img_to_array(img)
    input_arr = np.array([input_arr])
    result = model.predict(input_arr)
    probability_model = tensorflow.keras.Sequential([model,tensorflow.keras.layers.Softmax()])
    predict = probability_model.predict(input_arr)
    p = np.argmax(predict[0])
    global res
    res= CLASSES[p]

if __name__ == "__main__":
    run(source='AppleScab1.jpg')
    app = ChatApplication()
    app.run()


#ResNet plantvillage - 96.4 accuracy
#ResNet merged dataset - 95.2 accuracy
#96.1 without batch normalization but with flatten
#96.7 with batch normalization
#AlexNet - 85.1 accuracy
#VGG16 - long training time