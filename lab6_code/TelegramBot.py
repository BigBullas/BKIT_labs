import telebot
import os
from telebot import types

token = '5568359005:AAHgtpdFifN9cwECSYqg5SmADU9G3dxnWIE'
bot = telebot.TeleBot(token)

path0 = 'C:/Users/alikn/Desktop/python/photos/'


class Category:
    def __init__(self, name):
        self.name = name
        self.length = 0
        self.array = []
        self.path = path0 + name + '/'

    def __str__(self):
        return self.name


class TempPhoto:
    def __init__(self):
        self.id = ''
        self.messages = []
        self.num = 0
        self.category = ''
        self.name = 'noname'
        self.flag = False

    def rename_name(self, message):
        print('rename_name')
        if message.text is None:
            self.before_sending()
        else:
            self.name = message.text
            self.sending()

    def before_sending(self):
        print('before_sending')
        if self.num == 0:
            self.clearing()
        elif self.name == 'noname':
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton(text='Добавить название', callback_data='add_name' + '1'))
            keyboard.add(types.InlineKeyboardButton(text='Выйти', callback_data='exit_photo' + '1'))
            bot.send_message(self.id, 'Пожалуйста, добавьте название фотографиям', reply_markup=keyboard)
        else:
            self.sending()

    def sending(self):
        print('sending')
        for message, num in zip(self.messages, range(0, self.num)):
            file_photo = bot.get_file(message.photo[-1].file_id)
            filename, file_extention = os.path.splitext(file_photo.file_path)
            downloaded_file_photo = bot.download_file(file_photo.file_path)
            # src = 'C:/Users/alikn/Desktop/python/photos/' + message.photo[-1].file_id + file_extention
            # print('type of message:')
            # print(type(message))
            src = path0 + categories[-1].__str__() + '/' + self.name + str(num) + file_extention
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file_photo)
        self.clearing()
        bot.send_message(self.id, 'Фотографии успешно добавлены')

    def clearing(self):
        print('clearing')
        self.category = ''
        self.name = 'noname'
        self.num = 0
        self.messages = []
        self.flag = False


# скорей всего ненужные переменные
# message_with_photo = {}
# num_photo = 0
# global_category = ''
global_photo = TempPhoto()
categories_name = ['ААСОиУ', 'БКиТ', 'Англ', 'МД', 'Право',
                   'ТВиМС', 'Физика', 'Экология', 'Физра', 'Элтех', 'Прочее']
categories = []
for i in categories_name:
    categories.append(Category(i))


def create_keyboard(flag):
    keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
    for category in categories:
        keyboard.add(types.InlineKeyboardButton(text=category.name, callback_data=category.name + flag))
    return keyboard


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Добавить новые фото', 'Посмотреть существующие')
    bot.send_message(message.chat.id, 'Привет! Чем могу помочь?', reply_markup=keyboard)


# def get_photo(message=None):
#     file_photo = bot.get_file(message_with_photo.photo[-1].file_id)
#     filename, file_extention = os.path.splitext(file_photo.file_path)
#     downloaded_file_photo = bot.download_file(file_photo.file_path)
#     # src = 'C:/Users/alikn/Desktop/python/photos/' + message.photo[-1].file_id + file_extention
#     print('type of message:')
#     print(type(message))
#     if isinstance(message, telebot.types.Message):
#         src = path0 + categories[-1].__str__() + '/' + message.text + file_extention
#     if type(message) == str:
#         src = path0 + categories[-1].__str__() + '/' + message + file_extention
#     with open(src, 'wb') as new_file:
#         new_file.write(downloaded_file_photo)


@bot.message_handler(content_types=['photo'])
def check_get_photo(message):
    # Использовать класс Категория
    if message.photo is not None:
        # global message_with_photo
        # global num_photo
        global global_photo

        if message.caption is not None:
            if global_photo.name != 'noname':
                bot.send_message(message.chat.id, 'Для начала закончите отправку фотографий выше')
                return
            global_photo.name = message.caption
        global_photo.messages.append(message)
        global_photo.num += 1
        global_photo.flag = True

        # if num_photo != 0:
        #     if message.id == message_with_photo.id + 1:
        #         message.caption = message_with_photo.caption + str(num_photo)
        #         message_with_photo = message
        #         message_with_photo.caption = message_with_photo.caption[0:len(message_with_photo.caption)-1]
        #     else:
        #         num_photo = 0
        #         message_with_photo = message
        # else:
        #     message_with_photo = message
        # num_photo += 1
        # print()
        # print(type(message))
        #
        # print(message)
        # одинаковые у группы фотографий message.date, message.media_group_id
        # print('content_type: ', message.content_type, '\n', 'id: ', message.id, '\n', 'date: ', message.date, '\n',
        #       'media_group_id: ', message.media_group_id, '\n', )
        # if message.caption is None:
        #
        #     keyboard = types.InlineKeyboardMarkup()
        #     keyboard.add(types.InlineKeyboardButton(text='Добавить название', callback_data='add_name' + '1'))
        #     keyboard.add(types.InlineKeyboardButton(text='Выйти', callback_data='exit_photo' + '1'))
        #     bot.send_message(message.chat.id, 'Пожалуйста, добавьте название фотографиям', reply_markup=keyboard)
        # else:
        #     get_photo(message.caption)


@bot.callback_query_handler(func=lambda call: call.data[-1] == '1')
def get_photo_rename(call):
    print('get_photo_rename')
    global global_photo
    if call.data == 'add_name1':
        bot.register_next_step_handler(bot.send_message(call.message.chat.id, 'Введите название фотографий'),
                                       global_photo.rename_name)
    elif call.data == 'exit_photo1':
        global_photo.clearing()
        bot.send_message(call.message.chat.id, 'Выберите дальнейшее действие')


# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     keyboard = types.InlineKeyboardMarkup();  # наша клавиатура
#     key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')  # кнопка «Да»
#     keyboard.add(key_yes)  # добавляем кнопку в клавиатуру
#     key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
#     keyboard.add(key_no)
#     question = 'Тебе ' + ' лет, тебя зовут ' + '?'
#     bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
#
#     if message.text == "Привет":
#         bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
#     elif message.text == "/help":
#         bot.send_message(message.from_user.id, "Напиши привет")
#     else:
#         bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

@bot.message_handler(content_types=['text'])
def query_handler_start(message):
    global global_photo
    global_photo.id = message.chat.id
    if message.text == 'Добавить новые фото':
        keyboard1 = create_keyboard('10')
        keyboard1.add(types.InlineKeyboardButton(text='Добавить новую', callback_data='Add0'))
        bot.send_message(message.chat.id, 'Выберите категорию из списка, либо создайте новую:',
                         reply_markup=keyboard1)
    elif message.text == 'Посмотреть существующие':
        keyboard2 = create_keyboard('20')
        bot.send_message(message.chat.id, 'Окей, выберите необходимую категорию:', reply_markup=keyboard2)
    elif message.text == 'конец':
        global_photo.before_sending()


@bot.callback_query_handler(func=lambda call: call.data[-1] == '0')
def callback_worker(call):
    if call.data == 'Add0':
        keyboard = create_keyboard('10')
        bot.send_message(call.message.chat.id,
                         'Упс, произошла ошибка, невозможно создать новую категорию. Выберите из существующих',
                         reply_markup=keyboard)
    elif call.data[-2] == '1':
        global global_photo
        # global global_category
        if global_photo.flag:
            global_photo.before_sending()
        else:
            global_photo.category = call.data[0:len(call.data) - 2]
        # global_category = call.data[0:len(call.data) - 2]
        bot.send_message(call.message.chat.id, global_photo.category +
                         '. Присылайте фотографии с названием. По окончании отправки фотографий напишите "конец"')
        # Теперь у нас ожидает необходимых данных функция  get_photo
    elif call.data[-2] == '2':
        # Вызов функции вывода фотографий, которая будет проверять наличие фотографий в категории и юзать класс Категория
        bot.send_message(call.message.chat.id, call.data + ' false')


bot.polling(none_stop=True, interval=0)
