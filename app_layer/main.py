from fastapi import FastAPI
from common.common import run

print("APP LAYER")

app = FastAPI()

@app.get("/")
def root():
    return "HEllo"


@app.get("/run")
def run():
    return "FS"

if __name__ == "__main__":
    run(app, "0.0.0.0", 8000)
