from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()
vfile = '/ims/puppet_config.mp4'


@app.get('/')
async def root():
    return {
        "svc": "Video Streaming API"
    }


@app.get('/play')
async def play():
    file_instance = open(vfile, mode='rb')
    return StreamingResponse(file_instance, media_type='video/mp4')
