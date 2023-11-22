import pika
import video_tool

def callback(ch, method, properties, body):
    video_info = video_tool.download_video(body.decode())
    video_tool.upload_video(video_info["requested_downloads"][0]["filename"])
    print(f" [x] Received {body}")


def receive_message():
    connection_params = pika.ConnectionParameters(
        host='router.wxioi.fun',
        credentials=pika.PlainCredentials('admin', 'admin')
    )
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    channel.queue_declare(queue='youtube')

    channel.basic_consume(
        queue='youtube', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


receive_message()
