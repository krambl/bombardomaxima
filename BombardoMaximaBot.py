import telebot

class Settings:
    def __init__(self):
        self.token = '680538462:AAEprpQ6oLOEegyaDGU-5Nd7103n-OH86QM'
        self.database = './database.txt'
        self.data = []

settings = Settings()
bot = telebot.TeleBot(settings.token)

@bot.message_handler(content_types=['text'])
def text(message):
    print(settings.data)
    settings.data.append(message.text)
    if len(settings.data) == 1:
        bot.send_message(message.chat.id, 'first ok')
    elif len(settings.data) == 2:
        with open(settings.database, 'a') as file:
            file.write(settings.data[0] + '	' + settings.data[1] + '\n')
            settings.data = []
            bot.send_message(message.chat.id, 'second ok')

if __name__ == '__main__':
    bot.polling(none_stop=True)


