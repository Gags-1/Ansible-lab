from fastapi import FastAPI
import socket

app = FastAPI(title="Ansible Deployment Demo")


@app.get("/")
def root():
    return {
        "message": "Application deployed successfully with Ansible",
        "hostname": socket.gethostname()
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
