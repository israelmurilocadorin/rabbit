import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#Fila durável, caso o RabbitMQ pare de funcionar as mensagens não são perdidas
channel.queue_declare(queue='fila_tarefa', durable=True) 
print(' [*] Aguardando mensagens. Para sair, pressione CTRL + C')

#Caso um operario seja morto. A mensagem é entregue para outro operario que estiver on-line
def callback(ch, method, properties, body):
    print(" [x] Recebido %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Concluído")
    ch.basic_ack(delivery_tag=method.delivery_tag)

#Entrega uma mensagem por operario, caso esteja ocupado é enviado para um que esteja livre
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='fila_tarefa', on_message_callback=callback)

channel.start_consuming()

