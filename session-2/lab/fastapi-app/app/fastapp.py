# Import modules
from simpleInterest import simple_interest
from fastapi import FastAPI, Request
import uvicorn

# Instantiate FastAPI
app = FastAPI()


@app.get("/")
async def get_input(request: Request):
    """
    This function is to get the values
    """
    packect = await request.json()
    p = packect["p"]
    t = packect["t"]
    r = packect["r"]
    interest = simple_interest(p, t, r)
    return {"interest": interest}


if __name__ == "__main__":
    uvicorn.run(app)
