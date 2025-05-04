import asyncio as aio

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from pydantic import BaseModel


class ResponseModel(BaseModel):
    ok: bool
    msg: str
    rsp: str


app = FastAPI()

@app.wsc("/ws/chat")
async def websocket_chat(wsc: WebSocket):
    await wsc.accept()
    close = False
    for _ in range(3):
        try:
            while True:
                user_input = await wsc.receive_json()
                if user_input and user_input.get("action", "") == "close":
                    print("Closing connection")
                    close = True
                    break
                reply = await gen_response(user_input)
                await wsc.send_json(reply.model_dump_json(exclude_none=True))
        except (KeyError, AttributeError, IndexError) as e:
            er_ = await gen_exc_response(e)
            await wsc.send_json(er_.model_dump_json(exclude_none=True))
        except WebSocketDisconnect:
            print("Socket connection error, retrying...")
            await aio.sleep(3)
        except Exception:
            print("Error in chatbot response generation, retrying...")
            await aio.sleep(3)
        finally:
            if not close:
                continue
            await wsc.close()


# Dummy chatbot response
async def gen_response(user_input):
    return ResponseModel(ok=True, msg="User input received", rsp=user_input)


async def gen_exc_response(exc):
    return ResponseModel(ok=False, msg="Error in chatbot response generation", rsp=str(exc))
