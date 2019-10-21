import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='fila_tarefa', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(
    exchange='',
    routing_key='fila_tarefa',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2, # torna a mensagem persistente(Salva a mensagem no disco. Não é uma garantia total)
    )
)

print(" [x] Enviado %r" % message)
connection.close()