import random

message = ['It is certain',
           'It is decidely so',
           'Yes definitely',
           'Reply hazy try again',
           'Ask again later',
           'Concentrate and ask again',
           'My reply is no',
           'Outlook not so good',
           'Very doubtful']
print(message[random.randint(2, len(message)-2 )])
