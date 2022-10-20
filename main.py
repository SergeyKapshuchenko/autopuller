from fastapi import FastAPI, Request, Body
import subprocess

from utils import load_json, Path

app = FastAPI()


@app.get("/pull/git")
async def pull_git():
    return {"message": "Hello World"}


@app.post("/pull/docker")
async def pull_docker(payload: dict = Body()):
    tag: str = payload["push_data"]["tag"]

    config: dict = load_json(Path(__file__).parent.absolute() / "config.json")["docker"]

    if tag not in config:
        return {"state": "failure", "description": "Tag not found!"}

    for script in config[tag]:
        subprocess.Popen(["sh", script], stdin=subprocess.PIPE)

    return {"status": 200, "state": "success", "description": "commands executed!"}
