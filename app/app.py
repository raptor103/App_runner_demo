import io
from flask import Flask, request, render_template
from keras.applications.mobilenet import (MobileNet, preprocess_input,
                                          decode_predictions)
from keras.preprocessing import image
import numpy as np
from PIL import Image

app = Flask(__name__, template_folder="template")


def load_model():
    """
    Loads ML model
    :return: model
    """
    model = MobileNet(weights="imagenet", include_top=True)
    return model


@app.route("/")
def index():
    return render_template("home.html")


model = load_model()


@app.route("/predict", methods=["GET", "POST"])
def upload_file():
    response = {"success": False}
    if request.method == "POST":
        if request.files.get("file"):
            # read in file with image
            img_requested = request.files["file"].read()
            img = Image.open(io.BytesIO(img_requested))
            # check image model
            if img.mode != "RGB":
                img = img.convert("RGB")
            # transform input image
            img = img.resize((224, 224))
            img = image.img_to_array(img)
            img = np.expand_dims(img, axis=0)
            inputs = preprocess_input(img)
            # prediction
            preds = model.predict(inputs)
            results = decode_predictions(preds)

            response["predictions"] = []
            counter = 0
            for (imagenetID, label, prob) in results[0]:
                if counter > 0:
                    break
                row = {"label": label, "probability": float(prob)}
                response["predictions"].append(row)
                counter += 1

            c = response["predictions"][0]["label"]  # class label
            # probability of class
            # p = str(response["predictions"][0]["probability"])

            # render results on new page
            return render_template(
                "prediction_result.html",
                category=c
            )

    return render_template("predict.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
