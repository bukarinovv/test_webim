from random import randrange
from homepage.models import RandomInteger
from datetime import datetime, timedelta


def find_random_integer():
    random_integer = RandomInteger.objects.all().first()
    if random_integer:
        now_datetime = datetime.now(random_integer.updated_at.tzinfo)
        five_seconds_ago = now_datetime - timedelta(seconds=5)
        if random_integer.updated_at < five_seconds_ago:
            random_integer.value = randrange(1, 100)
            random_integer.save()
    else:
        random_integer = RandomInteger.objects.create(
            value=randrange(1, 100),
        )

    return random_integer.value
