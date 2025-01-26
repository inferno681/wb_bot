class BotText:
    cmd_start_text_first = 'Привет!'
    cmd_start_text_second = (
        'Этот бот позволяет получить актуальную информацию о товаре '
        'из базы данных.'
    )
    get_data = 'Получить данные по товару'
    collect_data = 'Запросить сбор данных'
    subscription_activation = 'Подписаться на товар'
    subscription_deactivation = 'Отписаться от товара'
    buttons = [
        get_data,
        collect_data,
        subscription_activation,
        subscription_deactivation,
    ]
    choice_case = {
        get_data: 'get',
        collect_data: 'collect',
        subscription_activation: 'sub_a',
        subscription_deactivation: 'sub_d',
    }
    ask_article = 'Пришлите артикул'
    cancel = '❌ Отмена'
    cancel_text = 'Действие отменено.'
    article_isdigit_message = 'Артикул должен быть числом. Попробуйте еще раз.'
    unknown_action = 'Неизвестное действие.'
