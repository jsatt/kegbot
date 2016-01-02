from kegbot import app, db


class Beverage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    style = db.Column(db.String(100))
    abv = db.Column(db.Float, default=0)
    ibu = db.Column(db.Integer, default=0)
    srm = db.Column(db.Integer, default=0)


class Tap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    channel = db.Column(db.String(10))
    factor = db.Column(db.Integer, default=0)
    total_volume = db.Column(db.Float, default=0)
    beverage_id = db.Column(db.Integer, db.ForeignKey('beverage.id'))
    beverage = db.relationship('Beverage', backref='taps', lazy='joined')
    current_volume = db.Column(db.Float, default=0)

    def reset_volume(self):
        self.current_volume == self.total_volume

    def dispense(self, pulses):
        self.current_volume = (self.current_volume or 0) - (pulses / self.factor)


class TapReader:
    def __init__(self, tap):
        self.tap = tap
        self.pulses = 0
        app.config['BOARD'].setup_event_handling(self.tap.channel, self.process_pulse)

    def reset_pulses(self):
        self.pulses = 0

    def process_pulse(self, *args):
        self.pulses += 1

    def update_volume(self):
        if self.pulses:
            self.tap.dispense(self.pulses)
            self.reset_pulses()
            return True
        return False
