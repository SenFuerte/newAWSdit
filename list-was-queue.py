# This script created a queue
#
# Author - Paul Doyle Aug 2013
#
#
import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError

				#				right A to fale B							right t to false m	
conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id='BKIAIR7EH3TNSTDUCWKA', aws_secret_access_key='m2FZT5mrLYy8gX7kS1q0p4ObQYXTwGnaiUm+rxHZ')
newConn = conn.create_queue("D14122972")
new.set_message_class(Message)
m = Message()
m.set_body('It works yuuuur')
newConn.write(m)

textMessage = newConn.get_messages()
print(len(textMessage))
m = textMessage[0]
print m.get_body()



rs = conn.get_all_queues()
for q in rs:
	print q.id
