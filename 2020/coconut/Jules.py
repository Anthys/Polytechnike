__author__ = 'julesmichaud'
__filename__ = 'Jules.py'
__date__ = '20/02/20'


def tri_days_sign_up(liste):
    liste.sort(key=lambda x: x["days_signup"], reverse=False)
    return liste


def tri_1(liste):
    liste.sort(key=lambda x: (x["sum_score"] / (x["days_signup"] + x["books_per_day"])), reverse=True)
    return liste


def tri_2(liste):
    liste.sort(key=lambda x: (x["sum_score"] / (x["days_signup"]) - x["books_per_day"]), reverse=True)
    return liste