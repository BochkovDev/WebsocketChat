import asyncio

from celery import shared_task

from .telegram_notification import send_telegram_notification


@shared_task
def send_telegram_notification_task(user_id: int, username: str):
    """
    Задача Celery для отправки уведомления пользователю в Telegram.

    :param user_id: ID пользователя, которому нужно отправить уведомление.
    :param username: Имя пользователя, которое будет указано в уведомлении.
    
    Эта функция запускает асинхронную функцию send_telegram_notification, 
    чтобы отправить уведомление пользователю в Telegram.
    """
    asyncio.run(send_telegram_notification(user_id=user_id, username=username))
     

