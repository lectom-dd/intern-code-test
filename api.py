from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from redis import Redis
from rq import Queue

app = FastAPI()

redis_conn = Redis(host='redis_queue', port=6379)
q = Queue('my_queue', connection=redis_conn)

@app.get('/hello')
def hello():
    """Test endpoint"""
    return {'hello': 'world'}
