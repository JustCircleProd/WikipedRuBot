from telegram.ext import Updater, Filters
from telegram.ext import CommandHandler, MessageHandler
from telegram import ReplyKeyboardMarkup

import wikipedia
import re


start_text = 'Привет! Вы можете написать мне любой запрос, ' \
             'и я найду страницу в Wikipedia, соответствующую этому запросу.'

help_text = 'Чтобы начать использование бота, необходимо нажать кнопку "Запустить" или написать команду /start.\n' \
            'После этого вы можете написать любой запрос боту, в ответ на который он пришлёт краткую выдержку из ' \
            'Wikipedia вместе с ссылкой на страницу, либо оповестит вас об ошибке и порекомендует уточнить запрос.\n' \
            'Если ответ бота на ваш запрос не соответствует тому, что вы искали, то вы можете посмотреть список, ' \
            'других страниц с похожим названием, нажав на кнопку "Посмотреть другие страницы".' \
            'После чего можно нажать на кнопку с ответом подходящей вам страницей.' \
            'Бот отправит вам новую статью с уточнённым запросом. '

wait_for_search_text = 'Ищу страницу по вашему запросу.'
search_error_text = 'Страницы по такому запросу либо не существует, либо запрос неоднозначен.\n' \
                    'Попробуйте уточнить запрос.'

show_other_results_text = 'Посмотреть другие страницы.'
search_results_text = 'Вот что ещё удалось найти.'
no_more_pages_found_text = 'Страниц больше не найдено.'

last_search_key = 'last_search'


def handle_start(update, _):
    update.message.reply_text(start_text)


def handle_help(update, _):
    update.message.reply_text(help_text)


def handle_text(update, context):
    if update.message.text == show_other_results_text:
        show_other_results_keyboard(update, context)
        return

    update.message.reply_text(wait_for_search_text)

    context.user_data[last_search_key] = update.message.text
    success, reply_text = get_wiki(update.message.text)

    if success:
        keyboard = [
            [show_other_results_text]
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    else:
        reply_markup = None

    update.message.reply_text(reply_text, reply_markup=reply_markup)


def show_other_results_keyboard(update, context):
    if last_search_key in context.user_data:
        last_search = context.user_data['last_search']
        search_result = wikipedia.search(last_search)

        if len(search_result) > 1:
            reply_text = search_results_text
            keyboard = []
            number_of_buttons = 5 if (len(search_result) > 5) else len(search_result) - 1

            for i in range(1, number_of_buttons):
                keyboard.append(
                    [search_result[i]]
                )

            reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)

        else:
            reply_text = no_more_pages_found_text
            reply_markup = None

        update.message.reply_text(reply_text, reply_markup=reply_markup)


def get_wiki(message_text):
    try:
        search_result = wikipedia.search(message_text)

        if len(search_result) == 0:
            return False, search_error_text

        sentences = wikipedia.page(search_result[0]).content[:1000].split('.')[:-1]
        result_text = ''
        for sentence in sentences:
            if not ('==' in sentence):
                if len((sentence.strip())) > 3:
                    result_text = f"{result_text}{sentence}."
            else:
                break

        result_text = re.sub(r'\([^()]*\)', '', result_text)
        result_text = re.sub(r'\([^()]*\)', '', result_text)
        result_text = re.sub(r'\{[^\{\}]*\}', '', result_text)

        page_url = wikipedia.page(search_result[0]).url
        result_text = f'{result_text}\n\n{page_url}'

        return True, result_text

    except wikipedia.exceptions.DisambiguationError:
        return False, search_error_text


def main():
    wikipedia.set_lang('ru')

    TOKEN = ''
    updater = Updater(TOKEN, use_context=True)

    db = updater.dispatcher

    db.add_handler(CommandHandler('start', handle_start, run_async=True))
    db.add_handler(CommandHandler('help', handle_help, run_async=True))
    db.add_handler(MessageHandler(Filters.text, handle_text, run_async=True))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
