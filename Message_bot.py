import telebot
from telebot.types import Message
from simplecrypt import encrypt, decrypt

TOKEN = '968491075:AAFaHwBVf-FmPXUKd-3Msqc7_jIRcegCx-o'
bot = telebot.TeleBot(TOKEN)

q = 0
mes = str()
password = str()
enpassword = str()
mas = {}
profi = {}
chek = 0


@bot.message_handler(commands=['myID'])
def command_handler(message: Message):
    if message.text == '/myID':
        s = message.from_user.id
        bot.reply_to(message, str(s))


@bot.message_handler(commands=['crypt'])
def command_handler(message: Message):
    global profi, chek, mas, mes, password
    if len(mes) != 0 and len(password) != 0:
        bot.reply_to(message, 'Wait...')
        s = encrypt(password, mes)
        mas[chek] = s
        profi[chek] = message.from_user.id
        chek += 1
        bot.reply_to(message, f'It is your ID {chek - 1}')

        # print(decrypt(password, s))
    elif len(mes) == 0:
        bot.reply_to(message, 'Please enter message')
    elif len(password) == 0:
        bot.reply_to(message, 'Please enter password fo crypt')


@bot.message_handler(commands=['getmymes'])
def command_handler(message: Message):
    global q
    bot.reply_to(message, 'Take you message ID')
    q = 5


@bot.message_handler(commands=['decrypt'])
def command_handler(message: Message):
    bot.reply_to(message, 'Send ID message')
    global q
    q = 3


@bot.message_handler(commands=['delkey'])
def command_handler(message: Message):
    bot.reply_to(message, 'I am delete your key')
    global password
    password = str()


@bot.message_handler(commands=['lastkey', 'lastmes'])
def command_handler(message: Message):
    global password, mes
    if message.text == '/lastkey':
        if len(password) == 0:
            bot.reply_to(message, 'You dont have key')
        else:
            bot.reply_to(message, password)
    elif message.text == '/lastmes':
        if len(mes) == 0:
            bot.reply_to(message, 'You dont have mes')
        else:
            bot.reply_to(message, mes)


@bot.message_handler(commands=['delmes'])
def command_handler(message: Message):
    bot.reply_to(message, 'I am delete your mes')
    global mes
    mes = str()


@bot.message_handler(commands=['getmes'])
def command_handler(message: Message):
    bot.reply_to(message, 'Enter your Mes')
    global q
    q = 2


@bot.message_handler(commands=['getkey'])
def command_handler(message: Message):
    bot.reply_to(message, 'Enter your key')
    global q
    q = 1


@bot.message_handler(commands=['getenkey'])
def command_handler(message: Message):
    bot.reply_to(message, 'Enter your encrypt key')
    global q
    q = 4


@bot.message_handler(content_types=['text'])
def ques(message: Message):
    global profi, chek, mas, mes, q, password, enpassword
    if q == 5:
        id = int(message.text)
        if profi[id] == message.from_user.id:
            bot.reply_to(message, str(mas[id]))
        else:
            bot.reply_to(message, 'Thit is not your message')
    elif q == 4:
        enpassword = message.text
        # print(enpassword)
    elif q == 3:
        s = int(message.text)
        # print(s)
        if s in mas:
            bot.reply_to(message, 'wait...')
            pol = 0
            try:
                t = decrypt(enpassword, mas[s])
            except:
                bot.reply_to(message, 'Uncorrect enkey')
                pol = 1
            if pol == 0:
                t = t.decode('utf-8')
                bot.reply_to(message, t)
        else:
            bot.reply_to(message, 'Your ID uncorected')
    elif q == 2:
        mes = message.text
        # print(mes)
        q = 0
    elif q == 1:
        password = message.text
        # print(password)
        q = 0
    elif q == 0:
        bot.reply_to(message, 'Pleas end a some command')


bot.polling(timeout=60)
