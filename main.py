from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/pull/git")
async def pull_git():
    return {"message": "Hello World"}


@app.post("/pull/docker")
async def pull_docker(request: Request):
    payload = await request.json()
    print(payload)
    return {'status': 200}
