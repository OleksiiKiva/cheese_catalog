from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
def sey_hello(name: str):
    return {"message": f"Hello {name}"}
