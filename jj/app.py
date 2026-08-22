from fastapi import FastAPI

app = FastAPI()


def add(a, b):
    return a + b


@app.get("/")
def root():
    return {"result": add(2, 3)}


@app.get("/health")
def health():
    return {"status": "ok"}
