class NDTUID:

    # method name in constructor
    def __init__(self, n):
        self.method = n

    # Nested Dictionary to define method paremeters
    NDTmethods = {
        # Methods are defined as per ISO 9712
        'AT': {'UID': 000000, },
        'ET': {'UID': 000000, },
        'IT': {'UID': 000000, },
        'LT': {'UID': 000000, },
        'MT': {'UID': 000000, },
        'PT': {'UID': 000000, },
        'RT': {'UID': 000000, },
        'ST': {'UID': 000000, },
        'UT': {'UID': 000000, },
        'VT': {'UID': 000000, }
    }
