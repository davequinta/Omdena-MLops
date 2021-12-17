from fastapi import FastAPI, Request
import uvicorn

from getArea import find_area

app = FastAPI()


@app.get("/")
async def get_input(request: Request):

    packet = await request.json()
    length = packet["length"]
    width = packet["width"]
    area = find_area(length, width)
    return area


if __name__ == "__main__":
    uvicorn.run()
