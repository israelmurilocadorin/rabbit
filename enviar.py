import pika

#Estabele conexão com o servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#Criação da fila que recebe a mensagem
channel.queue_declare(queue = 'fila')

#Publica a mensagem na fila especificada
channel.basic_publish(exchange='', routing_key='fila', body='Hello World!')
print("Hello World!")
connection.close()

