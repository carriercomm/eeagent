

class EEAgentParameterException(Exception):

    def __init__(self, message):
        Exception.__init__(self, message)


class EEAgentUnauthorizedException(Exception):
    pass


class EEAgentSupDException(Exception):

    def __init__(self, message):
        Exception.__init__(self, message)
