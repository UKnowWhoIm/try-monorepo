from fastapi import FastAPI
from common.common import run

print("APP LAYER")

app = FastAPI()

@app.get("/")
def root():
    return "HEllo"


if __name__ == "__main__":
    run(app, "0.0.0.0", 8000)
