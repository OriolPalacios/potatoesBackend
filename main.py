from typing import Union
from PIL import Image
import io


from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.get("/")
def read_root():
    return "Conexion exitosa"


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# i want a post method that receives an image and returns the prediction of the image
@app.post("/predict/")
def predict(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(file.file.read()))
    # TODO: do something with the image
    prediction = "whatever"
    return {"prediction": prediction}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)