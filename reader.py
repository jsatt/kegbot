from time import sleep

from kegbot import db
from kegbot.models import Tap, TapReader


def start_loop():
    taps = db.session.query(Tap).all()
    readers = {t: TapReader(t) for t in taps}

    while True:
        for tap in taps:
            if readers[tap].update_volume():
                db.session.add(tap)
        db.session.commit()
        sleep(1)

if __name__ == '__main__':
    start_loop()
