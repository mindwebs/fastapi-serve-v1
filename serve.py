from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse
from pydantic import BaseModel


import uvicorn
import tensorflow as tf
from tensorflow.keras.models import load_model
import os
import base64
import calendar
import time
from PIL import Image
import numpy as np


# Creating FastAPI instance
app = FastAPI()

# Creating class to define the request body and the type hints of each attribute
class request_body(BaseModel):
	instance : str

model_name = os.path.join(os.path.join(os.path.dirname( __file__ ), 'models'), 'model.h5')
model = load_model(model_name, compile=False)

# Defining path operation for root endpoint
@app.get('/')
def main():
    return {'message': 'Welcome to Model Predict!'}


# Creating an Endpoint to receive the data to make prediction on.
@app.post('/predict/image')
def predict(data : request_body):
	# Making the data in a form suitable for prediction
    ts = calendar.timegm(time.gmtime())

    if data.instance:
        path = os.path.join(os.path.join(os.path.dirname(
            __file__), 'uploads'), "b64-" + str(ts) + ".png")
        with open(path, "wb") as fh:
            fh.write(base64.b64decode(data.instance))
            # fh.write(bytes(data.instance).decode('base64'))
    else:
        raise HTTPException(status_code=400, detail="'instance' (b64) not found in request")

    img = Image.open(path).convert('RGB')
    img = np.asarray(img.resize((500,500)))
    img = tf.cast(img, tf.float32)
    img = np.expand_dims(img, axis=0)

    result = model.predict(img)
    print(type(result))

    # if ENV_MODE=='prod':
    #     # Delete uploaded file
    if os.path.isfile(path):
        os.remove(path)

    # Return the results
    return { 'result' : result}
