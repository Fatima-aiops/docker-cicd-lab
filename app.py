from flask import Flask
import os
import redis

app = Flask(__name__)

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
redis_client = redis.Redis(
    host=REDIS_HOST,
    port=6379,
    decode_responses=True
)

@app.route("/")
def hello():
    return "Hello from Docker CI/CD!"

@app.route("/health")
def health():
    try:
        redis_client.ping()
        return "OK", 200
    except redis.RedisError:
        return "Redis unavailable", 503

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
