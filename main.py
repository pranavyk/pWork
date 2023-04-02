import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/abcd")
def root():
    return {"message": "Hello World"}


def main():
    uvicorn.run(app)


if __name__ == "__main__":
    main()
