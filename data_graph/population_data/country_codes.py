from pygal.maps.world import COUNTRIES


def get_country_code(country_name):
    """return pygal country codes"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        """if not found return none"""
    return None

