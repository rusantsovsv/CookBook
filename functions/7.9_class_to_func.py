"""
У вас есть класс, который определяет только один метод, кроме __init__(). Однако
для упрощения вашего кода вы бы хотели заменить его на простую функцию.

Во многих случаях классы с одним методом могут быть превращены в функции
с помощью замыканий. Рассмотрите, например, следующий класс, который по-
зволяет пользователю загружать страницы по URL с использованием некой шаблонной
схемы:
"""

from urllib.request import urlopen


class UrlTemplate:
    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))


# Пример использования. Скачать данные об акциях с Yahoo
yahoo = UrlTemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo.open(names='IBM,AAPL,FB', fields='sl1c1v'):
    print(line.decode('utf-8'))

# Этот класс может быть заменен намного более простой функцией:

def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))
    return opener

# пример использования
yahoo = urltemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo(names='IBM, AAPL, FB', fields='sl1c1v'):
    print(line.decode('utf-8'))

"""
Во многих случаях единственной причиной использовать класс с одним методом
является необходимость сохранять дополнительное состояние для использова-
ния в методе. Например, единственное назначение класса UrlTemplate заключает-
ся в сохранении значения template, чтобы оно могло быть использовано в методе
open().
Использование вложенной функции (замыкания), как показано выше, часто
будет намного более элегантным решением. Замыкание – это просто функция,
но с дополнительным окружением переменных, которые используются внутри
функции. Ключевое преимущество замыкания в том, что оно запоминает окру-
жение, в котором было определено. Поэтому в примере функция opener() запо-
минает значение аргумента template() и использует его в последующих вызовах.

Всякий раз, когда вы пишете код и встречаетесь с задачей прикрепления до-
полнительного состояния к функции, вспоминайте о замыканиях. Они часто яв-
ляются более минималистичным и элегантным решением, нежели альтернатива
(превращение функции в полноценный класс).
"""