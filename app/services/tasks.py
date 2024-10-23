import asyncio

from celery import shared_task

from .telegram_notification import send_telegram_notification


@shared_task
def send_telegram_notification_task(user_id: int, username: str):
    asyncio.run(send_telegram_notification(user_id=user_id, username=username))
     

