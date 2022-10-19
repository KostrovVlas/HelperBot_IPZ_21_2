import datetime

import telebot

bot = telebot.TeleBot("5637682238:AAEOsuvuJ5mbS8bW6q_8MrByoTkCNmFiGJ4")


class day_of_the_week:
    def __init__(self):
        self.pair_tuple = []

    def append_pair(self, name_pair: str, time_start: datetime.timedelta, time_end: datetime.timedelta, link: str):
        self.pair_tuple.append([name_pair, time_start, time_end, link])

    def remove_pair(self, name_pair: str):
        count = 0
        for i in self.pair_tuple:
            if i[0] == name_pair:
                self.pair_tuple.remove(count)
                return "Пара видалена"
            count += 1
        return "Пара не знайдена"

    def get_current_pair(self):
        current_time = datetime.timedelta(hours=datetime.datetime.now().time().hour,
                                          minutes=datetime.datetime.now().time().minute)
        for i in self.pair_tuple:
            if i[1] < current_time and current_time < i[2]:
                time1 = f"{i[2]}".replace(":00", "", 1)
                return f"Зараз {i[0]}, закінчиться в {time1}\nПосилання: {i[3]}"
            else:
                continue
        return "Зараз немає пари"

    def get_next_pair(self):
        current_pair = self.get_current_pair()
        current_time = datetime.timedelta(hours=datetime.datetime.now().time().hour,
                                          minutes=datetime.datetime.now().time().minute)
        for i in self.pair_tuple:
            if current_time < i[1] and i[1] - current_time <= datetime.timedelta(hours=1, minutes=50):
                time1 = f"{i[1]}".replace(":00", "", 1)
                return f"Наступна пара: {i[0]}. Початок о {time1}\nПосилання: {i[3]}"
            else:
                continue
        return f"Не бачу наступну пару, можливо до неї ще далеко...\n{current_pair}"

    def get_schedule(self):
        response = ""
        for i in self.pair_tuple:
            time1 = f"{i[1]}".replace(":00", "", 1)
            time2 = f"{i[2]}".replace(":00", "", 1)
            response += f"{time1}-{time2} {i[0]}\n"
        return response


# ----------------------------------------------------------------------------
Monday_denominator = day_of_the_week()
Monday_denominator.append_pair(name_pair="БЖД (Білова Н.А.); ТОВАРОЗНАВСТВО В МИТНІЙ СПРАВІ (Вишнікіна О.В.)",
                               time_start=datetime.timedelta(hours=8),
                               time_end=datetime.timedelta(hours=9, minutes=20),
                               link= "")
# ----------------------------------------------------------------------------
Monday_numerator = day_of_the_week()
Monday_numerator.append_pair(name_pair="БЖД (Білова Н.А.); ТОВАРОЗНАВСТВО В МИТНІЙ СПРАВІ (Вишнікіна О.В.)",
                             time_start=datetime.timedelta(hours=8),
                             time_end=datetime.timedelta(hours=9, minutes=20),
                             link= "")
Monday_numerator.append_pair(name_pair="ФІЛОСОФІЯ",
                             time_start=datetime.timedelta(hours=9, minutes=30),
                             time_end=datetime.timedelta(hours=10, minutes=50),
                             link= "https://us05web.zoom.us/j/8132227966")
# ----------------------------------------------------------------------------
Tuesday_denominator = day_of_the_week()
Tuesday_denominator.append_pair(name_pair="ФІЛОСОФІЯ",
                                time_start=datetime.timedelta(hours=8),
                                time_end=datetime.timedelta(hours=9, minutes=20),
                                link= "https://us05web.zoom.us/j/8132227966")
Tuesday_denominator.append_pair(name_pair="ТЕОРІЯ ЙМОВІРНОСТЕЙ І МАТЕМАТИЧНА СТАТИСТИКА",
                                time_start=datetime.timedelta(hours=9, minutes=30),
                                time_end=datetime.timedelta(hours=10, minutes=50),
                                link= "https://us05web.zoom.us/j/85803218478?pwd=WTRjcnVXQkE0UExFa0hZQTl5dzA5Zz09")
Tuesday_denominator.append_pair(name_pair="ОБ'ЄКТНО-ОРІЄНТОВАНЕ ПРОГРАМУВАННЯ",
                                time_start=datetime.timedelta(hours=11, minutes=20),
                                time_end=datetime.timedelta(hours=12, minutes=40),
                                link= "https://us04web.zoom.us/j/9560807813?pwd=QklQNzhYQmFvUXQrckhYb3p2UkVXUT09")
Tuesday_denominator.append_pair(name_pair="ТЕХНОЛОГІЇ РОЗОРБКИ ПРОГРАМНОГО ЗАБЕЗПЕЧЕННЯ",
                                time_start=datetime.timedelta(hours=12, minutes=50),
                                time_end=datetime.timedelta(hours=14, minutes=10),
                                link= "https://us02web.zoom.us/j/4483896971?pwd=OG8zS0J5WU1kai9PVXMvaVdseVFrQT09")
Tuesday_denominator.append_pair(name_pair="ТЕХНОЛОГІЇ РОЗОРБКИ ПРОГРАМНОГО ЗАБЕЗПЕЧЕННЯ",
                                time_start=datetime.timedelta(hours=14, minutes=20),
                                time_end=datetime.timedelta(hours=15, minutes=40),
                                link= "https://us02web.zoom.us/j/4483896971?pwd=OG8zS0J5WU1kai9PVXMvaVdseVFrQT09")
# ----------------------------------------------------------------------------
Tuesday_numerator = day_of_the_week()
Tuesday_numerator.append_pair(name_pair="ТЕОРІЯ ЙМОВІРНОСТЕЙ І МАТЕМАТИЧНА СТАТИСТИКА",
                              time_start=datetime.timedelta(hours=9, minutes=30),
                              time_end=datetime.timedelta(hours=10, minutes=50),
                              link= "https://us05web.zoom.us/j/85803218478?pwd=WTRjcnVXQkE0UExFa0hZQTl5dzA5Zz09")
Tuesday_numerator.append_pair(name_pair="ОБ'ЄКТНО-ОРІЄНТОВАНЕ ПРОГРАМУВАННЯ",
                              time_start=datetime.timedelta(hours=11, minutes=20),
                              time_end=datetime.timedelta(hours=12, minutes=40),
                              link= "https://us04web.zoom.us/j/9560807813?pwd=QklQNzhYQmFvUXQrckhYb3p2UkVXUT09")
Tuesday_numerator.append_pair(name_pair="ТЕХНОЛОГІЇ РОЗОРБКИ ПРОГРАМНОГО ЗАБЕЗПЕЧЕННЯ",
                              time_start=datetime.timedelta(hours=12, minutes=50),
                              time_end=datetime.timedelta(hours=14, minutes=10),
                              link= "https://us02web.zoom.us/j/4483896971?pwd=OG8zS0J5WU1kai9PVXMvaVdseVFrQT09")
Tuesday_numerator.append_pair(name_pair="ТЕХНОЛОГІЇ РОЗОРБКИ ПРОГРАМНОГО ЗАБЕЗПЕЧЕННЯ",
                              time_start=datetime.timedelta(hours=14, minutes=20),
                              time_end=datetime.timedelta(hours=15, minutes=40),
                              link= "https://us02web.zoom.us/j/4483896971?pwd=OG8zS0J5WU1kai9PVXMvaVdseVFrQT09")
# ----------------------------------------------------------------------------
Wednesday = day_of_the_week()
Wednesday.append_pair(name_pair="ТЕХНОЛОГІЇ Big Date",
                      time_start=datetime.timedelta(hours=11, minutes=20),
                      time_end=datetime.timedelta(hours=12, minutes=40),
                      link= "https://us04web.zoom.us/j/5389482846?pwd=bjhYd2R6anhENHZSU2ZHbzc4Q3BKQT09")
Wednesday.append_pair(name_pair="ОСНОВИ ЮРИСПРУДЕНЦІЇ",
                      time_start=datetime.timedelta(hours=12, minutes=50),
                      time_end=datetime.timedelta(hours=14, minutes=10),
                      link= "посилання постійно змінюється, тому перевір у classroom")
Wednesday.append_pair(name_pair="ТЕХНОЛОГІЇ Big Date",
                      time_start=datetime.timedelta(hours=14, minutes=20),
                      time_end=datetime.timedelta(hours=15, minutes=40),
                      link= "https://us04web.zoom.us/j/5389482846?pwd=bjhYd2R6anhENHZSU2ZHbzc4Q3BKQT09")
# ----------------------------------------------------------------------------
Friday = day_of_the_week()
Friday.append_pair(name_pair="ОБ'ЄКТНО-ОРІЄНТОВАНЕ ПРОГРАМУВАННЯ",
                   time_start=datetime.timedelta(hours=9, minutes=30),
                   time_end=datetime.timedelta(hours=10, minutes=50),
                   link= "https://meet.google.com/qvz-zezi-shi")
Friday.append_pair(name_pair="ТЕОРІЯ ЙМОВІРНОСТЕЙ І МАТЕМАТИЧНА СТАТИСТИКА",
                   time_start=datetime.timedelta(hours=11, minutes=20),
                   time_end=datetime.timedelta(hours=12, minutes=40),
                   link= "https://us05web.zoom.us/j/85803218478?pwd=WTRjcnVXQkE0UExFa0hZQTl5dzA5Zz09")
Friday.append_pair(name_pair="ФІЗИЧНЕ ВИХОВАННЯ (СПЕЦПІДГОТОВКА)",
                   time_start=datetime.timedelta(hours=12, minutes=50),
                   time_end=datetime.timedelta(hours=14, minutes=10),
                   link= "https://meet.google.com/vpv-qnss-nhv?authuser=2&hs=179")
# ----------------------------------------------------------------------------

denominator_list = [Monday_denominator, Tuesday_denominator, Wednesday, 0, Friday, 0, 0]
numerator_list = [Monday_numerator, Tuesday_numerator, Wednesday, 0, Friday, 0, 0]

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print(f"start: {message.from_user.username} {datetime.datetime.now()}")

    file = open('text.txt', 'a')
    file.write(f"start: {message.from_user.username}  {datetime.datetime.now()}" + '\n')
    file.close()

    bot.reply_to(message,
                 "Вітаю! Поки що я можу лише підказати тобі розклад, але в майбутньому зможу робити більше)\n\nТи можеш ввести наступні команди для отримання інформації:\n\n /Пара для отримання поточної пари\n\n/Наступна-пара для того щоб дізнатися наступну пару\n\n/Розклад для отримання сьогоднішнього розкладу")


@bot.message_handler(commands=['Розклад', "розклад"])
def reply_schedule(message):
    print(f"Розклад: {message.from_user.username} {datetime.datetime.now()}")

    file = open('text.txt', 'a')
    file.write(f"Розклад: {message.from_user.username}  {datetime.datetime.now()}" + '\n')
    file.close()

    now = datetime.datetime.now()
    nums = int(datetime.datetime.utcnow().isocalendar()[1])
    now = datetime.datetime.weekday(now)
    if now != 3 and now != 5 and now != 6:
        if (nums % 2) == 0:
            bot.reply_to(message, denominator_list[now].get_schedule())
        else:
            bot.reply_to(message, numerator_list[now].get_schedule())
    else:
        bot.reply_to(message, "Сьогодні пар немає, відпочивай")



@bot.message_handler(commands=['Пара', "пара"])
def current_pair(message):
    print(f"Пара: {message.from_user.username} {datetime.datetime.now()}")

    file = open('text.txt', 'a')
    file.write(f"Пара: {message.from_user.username}  {datetime.datetime.now()}" + '\n')
    file.close()

    now = datetime.datetime.now()
    nums = int(datetime.datetime.utcnow().isocalendar()[1])
    now = datetime.datetime.weekday(now)
    if now != 3 and now != 5 and now != 6:
        if (nums % 2) == 0:
            bot.reply_to(message, denominator_list[now].get_current_pair())
        else:
            bot.reply_to(message, numerator_list[now].get_current_pair())
    else:
        bot.reply_to(message, "Сьогодні пар немає, відпочивай")


@bot.message_handler(commands=['Наступна-пара', "наступна-пара"])
def next_pair(message):
    print(f"Наступна-пара: {message.from_user.username} {datetime.datetime.now()}")

    file = open('text.txt', 'a')
    file.write(f"Наступна-пара: {message.from_user.username}  {datetime.datetime.now()}" + '\n')
    file.close()

    now = datetime.datetime.now()
    nums = int(datetime.datetime.utcnow().isocalendar()[1])
    now = datetime.datetime.weekday(now)
    if now != 3 and now != 5 and now != 6:
        if (nums % 2) == 0:
            bot.reply_to(message, denominator_list[now].get_next_pair())
        else:
            bot.reply_to(message, numerator_list[now].get_next_pair())
    else:
        bot.reply_to(message, "Сьогодні пар немає, відпочивай")

bot.polling(non_stop=True)
