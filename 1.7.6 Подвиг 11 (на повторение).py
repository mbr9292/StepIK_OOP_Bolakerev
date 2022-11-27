class Message:
    def __init__(self, text):
        self.text = text
        self.fl_like = False


class Viber:
    msgs = {}
    i = 1

    @classmethod
    def add_message(cls, msg):
        i = cls.i
        cls.msgs[id(msg)] = [i, msg]
        cls.i += 1

    @classmethod
    def remove_message(cls, msg):
        cls.msgs.pop(id(msg))


    @classmethod
    def set_like(cls, msg):
        mess = cls.msgs.setdefault(id(msg))[1]
        if mess.fl_like == True:
            mess.fl_like = False
        elif mess.fl_like == False:
            mess.fl_like = True

    @classmethod
    def show_last_message(cls, num):
        dict_of_value = cls.get_dict_of_value(cls.msgs)
        len_of_dict = len(dict_of_value)
        for i in range(len_of_dict-num+1, len_of_dict+1):
            print(dict_of_value.get(i))


    @staticmethod
    def get_dict_of_value(d):
        dict_of_value = {}
        for key, value in d.items():
            dict_of_value[value[0]] = value[1].text
        return dict_of_value

    @classmethod
    def total_messages(cls):
        return len(cls.msgs)


assert hasattr(Viber, 'show_last_message'), "отсутствует метод show_last_message"

msg = Message("Всем привет!")
Viber.add_message(msg)
assert Viber.total_messages() == 1, "сообщение не было добавлено: некорректно работает метод add_message"

Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))

assert Viber.total_messages() == 3, "неверное число сообщений: некорректно работает метод add_message"

assert msg.fl_like == False, "лайка по умолчанию не должно быть - значение False"
Viber.set_like(msg)
assert msg.fl_like == True, "лайк не проставился: некорректно работает метод set_like"
Viber.set_like(msg)
assert msg.fl_like == False, "лайк не убрался при повторном вызове метода set_like"
Viber.remove_message(msg)

assert Viber.total_messages() == 2, "неверное число сообщений: некорректно работает метод remove_message"


