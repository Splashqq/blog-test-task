import asyncio

from django.core.management.base import BaseCommand

from apps.tgbot.bot import start_bot


class Command(BaseCommand):
    def handle(self, *args, **options):
        asyncio.run(start_bot())
