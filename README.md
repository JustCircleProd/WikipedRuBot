# WikipedRuBot🧠

**Telegram-бот WikipedRuBot (@wikipedrubot) позволяет быстро найти самую главную информацию с портала Wikipedia по вашему запросу.**

Чтобы начать использование бота, необходимо нажать кнопку "Запустить" или написать команду */start*.
После этого вы можете написать любой запрос боту, в ответ на который он пришлёт краткую выдержку из Wikipedia вместе с ссылкой на страницу, либо оповестит вас об ошибке и порекомендует уточнить запрос.

*Если ответ бота на ваш запрос не соответствует тому, что вы искали, то вы можете посмотреть список других страниц с похожим названием, нажав на кнопку "Посмотреть другие страницы".
После чего можно нажать на кнопку с ответом подходящей вам страницы. Бот отправит вам новую статью с уточнённым запросом.*

В случае появления каких-либо затруднений вам может помочь команда */help*.

## Технологии🐍

**Бот написан на языке программирования Python с использованием API python-telegram-bot, встроенных модулей (re, os) и стороннего модуля wikipedia (для доступа к контенту с портала Wikipedia).**

## Работоспособность📈

**Бот был загружен на сервис Heroku и полностью функционирует.** \
**Чтобы его протестировать**, необходимо ввести в поиске Telegram @wikipedrubot и начать использование. \
*При долгом бездействии первый ответ может поступить со значительной задержкой.*

## Как запустить💻

Код бота можно открыть в любом редакторе программного кода с поддержкой Python. \
**Чтобы протестировать сам код необходимо**: \
- установить соответствующие модули из файла *"requirements.txt"* через консоль с использованием системы управления пакетами pip, \
- создать своего бота и получить токен, \
- вставить токен в строку с номером 116: *TOKEN = 'ваш токен'*. \
После этого можно запустить программный файл на исполнение. \
Бот будет исполнять функционал, описанный в файле bot.py. Любые изменения будут сказывать на работе созданного вами бота, но не бота WikipedRuBot.

## License📝
      Copyright 2022 JustCircle Prod. (Vadim Karchagin)

      Licensed under the Apache License, Version 2.0 (the "License");
      you may not use this file except in compliance with the License.
      You may obtain a copy of the License at

         http://www.apache.org/licenses/LICENSE-2.0

      Unless required by applicable law or agreed to in writing, software
      distributed under the License is distributed on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
      See the License for the specific language governing permissions and
      limitations under the License.
