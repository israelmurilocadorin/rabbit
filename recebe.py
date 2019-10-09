import pika

#Estabele conexão com o servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#Criação da fila que recebe a mensagem
channel.queue_declare(queue='ola')

#Função que imprime na tela a mensagem
def ​callback(ch, method, properties, body):
   ​print(" [x] Received %r" % body)

#Informa o RabbitMQ que essa função deve receber mensagens só da fila ola
channel.basic_consume(queue='ola', on_message_callback=callback, auto_ack=True)

#Loop que executa os retornos sempre que necessário
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()