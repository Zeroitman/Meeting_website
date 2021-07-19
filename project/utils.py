import math


def determination(from_user, to_user):
    a = float(abs(from_user.latitude - to_user.latitude)) * 111.16
    min_latitude = min(float(from_user.latitude), float(to_user.latitude))
    long_diff = float(abs(from_user.longitude - to_user.longitude))
    b = long_diff * math.cos(math.radians(min_latitude)) * 111.3
    r = 6371
    re = ((a / r) ** 2) + ((b / r) ** 2)
    return math.sqrt(re) * r
