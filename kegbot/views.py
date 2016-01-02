from kegbot import app
from kegbot.models import Tap

@app.route('/')
def test_view():
    t1, t2 = Tap.query.all()
    return 't1: {}\nt2: {}'.format(t1.current_volume, t2.current_volume)
