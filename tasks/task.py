class Task:
    def run(self):
        raise NotImplementedError('{}: function \'run\' not implemented!'.format(__class__))

    def before_pushed(self, engine):
        pass
