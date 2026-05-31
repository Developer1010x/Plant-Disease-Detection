from tkinter import *
from tkinter import filedialog, messagebox
from chat import get_response, bot_name
import imageio
import tensorflow
import numpy as np
from PIL import Image
import cv2
import os

CLASSES = ["Apple scab","Apple Black rot","Apple cedar rust","Apple healthy","Blackgram Anthracnose","Blackgram Leaf crinkle","Blackgram Powdery Mildew","Blackgram Yellow Mosaic","Blackgram healthy","Blueberry healthy","Cherry Powdery Mildew",
           "Cherry Healthy","Corn leaf spot","Corn Common rust","Corn northern leaf blight","Corn healthy","Grape black rot","Grape esca","Grape leaf blight",
           "Grape healthy","Orange Haunglongbing","Peach bacterial spot","Peach healthy","Pepper bell bacterial spot","Pepper bell healthy","Potato early blight",
           "Potato late blight","Potato healthy","Raspberry healthy","Soybean healthy","Squash powdery mildew","Strawberry leaf scotch","Strawberry healthy","Tomato bacterial spot",
           "Tomato early blight","Tomato late blight","Tomato leak mould","Tomato septoria leaf spot","Tomato spider mite","Tomato target spot","Tomato yellow leaf curl virus","Tomato mosaic","Tomato healthy"]

MODEL_FILE = "reseven.h5"

BG_GRAY = "#C9AE5D"
BG_COLOR = "#F7E7CE"
TEXT_COLOR = "#665D1E"
FONT = "Georgia 18"
FONT_BOLD = "Georgia 18 bold"


def load_model():
    """Load the trained ResNet model once and reuse it for every prediction."""
    if not os.path.exists(MODEL_FILE):
        raise FileNotFoundError(
            f"Model file '{MODEL_FILE}' not found. Train the model or place the .h5 file alongside gui.py."
        )
    return tensorflow.keras.models.load_model(MODEL_FILE)


def predict_disease(model, source):
    """Run Otsu-masked preprocessing and return the predicted disease label."""
    image = imageio.imread(source)

    # Otsu thresholding + Gaussian blur preprocessing (kept from the original pipeline).
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    thresh = cv2.bitwise_not(thresh)
    mask = cv2.merge((thresh, thresh, thresh))
    cv2.bitwise_and(image, mask)  # masking step retained for parity with training

    img = Image.fromarray(image).resize((224, 224))
    input_arr = tensorflow.keras.preprocessing.image.img_to_array(img)
    input_arr = np.array([input_arr])
    probability_model = tensorflow.keras.Sequential(
        [model, tensorflow.keras.layers.Softmax()]
    )
    predict = probability_model.predict(input_arr)
    return CLASSES[int(np.argmax(predict[0]))]


class ChatApplication:
    def __init__(self):
        self.model = None
        try:
            self.model = load_model()
        except Exception as exc:  # surface a clear message instead of crashing on launch
            print(f"[warning] could not load model: {exc}")
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Plant Disease Repository")
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
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        bottom_label = Label(self.window, bg=BG_GRAY, height=100)
        bottom_label.place(relwidth=1, rely=0.825)

        self.msg_entry = Entry(bottom_label, bg="#BAB86C", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.55, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, bg=BG_GRAY,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.57, rely=0.008, relheight=0.06, relwidth=0.20)

        upload_button = Button(bottom_label, text="Upload Leaf", font=FONT_BOLD, bg=BG_GRAY,
                               command=self._on_upload)
        upload_button.place(relx=0.78, rely=0.008, relheight=0.06, relwidth=0.21)

        self._post(bot_name, "Upload a leaf image to detect a disease, or ask me about a known disease.")

    def _on_upload(self):
        """Let the user pick a leaf image, classify it, and ask the bot for guidance."""
        if self.model is None:
            messagebox.showerror("Model unavailable", f"'{MODEL_FILE}' could not be loaded.")
            return
        source = filedialog.askopenfilename(
            title="Select a leaf image",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp"), ("All files", "*.*")],
        )
        if not source:
            return
        try:
            disease = predict_disease(self.model, source)
        except Exception as exc:
            messagebox.showerror("Prediction failed", str(exc))
            return
        self._post("Detection", f"Predicted: {disease}")
        # Ask the chatbot for treatment information about the detected disease.
        self._post(bot_name, get_response(disease))

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        if not msg:
            return
        self.msg_entry.delete(0, END)
        self._post("You", msg)
        self._post(bot_name, get_response(msg))

    def _post(self, sender, msg):
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, f"{sender}: {msg}\n\n")
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)


if __name__ == "__main__":
    app = ChatApplication()
    app.run()


# ResNet plantvillage - 96.4 accuracy
# ResNet merged dataset - 95.2 accuracy
# 96.1 without batch normalization but with flatten
# 96.7 with batch normalization
# AlexNet - 85.1 accuracy
# VGG16 - long training time
