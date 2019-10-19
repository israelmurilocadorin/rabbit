import pika

#Estabele conexão com o servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#Criação da fila que recebe a mensagem
channel.queue_declare(queue = 'ola')

#Publica a mensagem na fila especificada
channel.basic_publish(exchange='', routing_key='ola', body='Hello World!')
print("[x] Enviado 'Hello World!'")
connection.close()



