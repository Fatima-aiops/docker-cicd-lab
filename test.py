import os
import redis

redis_host = os.getenv("REDIS_HOST", "redis")

client = redis.Redis(
    host=redis_host,
    port=6379,
    decode_responses=True
)

print("Testing Redis connection...")

client.ping()

client.set("ci_cd_test", "PASS")

result = client.get("ci_cd_test")

if result != "PASS":
    raise SystemExit("TEST FAILED")

print("Redis integration test: PASS")
