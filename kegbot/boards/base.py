class BaseBoard:
    def setup_event_handling(self, channel, callback):
        raise NotImplementedError

    def teardown_event_handling(self, channel):
        pass
