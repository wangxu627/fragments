from fastapi import FastAPI
import pika

HTTP_PORT = 8995
HOST = '0.0.0.0'

app = FastAPI()


def send_message(message):
    connection_params = pika.ConnectionParameters(
        host='router.wxioi.fun',
        credentials=pika.PlainCredentials('admin', 'admin')
    )
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()
    channel.queue_declare(queue='youtube')
    channel.basic_publish(exchange='', routing_key='youtube', body=message)
    print(f" [x] Sent '{message}'")
    connection.close()



@app.get("/download/")
def post_msg(url: str):
    msg = "queued"
    try:
        send_message(url)
    except pika.exceptions.AMQPConnectionError:
        msg = "connection error"
    return {"message": msg}


def main():
    import uvicorn
    uvicorn.run(app, host=HOST, port=HTTP_PORT)


if __name__ == "__main__":
    main()
