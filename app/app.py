from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "K8s CI/CD Pipeline - Running!",
        "status": "healthy",
        "host": socket.gethostname()
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "version": os.getenv("APP_VERSION", "1.0.0")
    })

@app.route("/info")
def info():
    return jsonify({
        "app": "k8s-cicd-pipeline",
        "author": "Douglas Deveza",
        "stack": ["Python", "Flask", "Docker", "Kubernetes", "GitHub Actions"],
        "pod": socket.gethostname()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
