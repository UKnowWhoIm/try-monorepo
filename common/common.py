import uvicorn

def x():
    print("FA")

def run(app, host, port):
    uvicorn.run(app, host=host, port=port)
