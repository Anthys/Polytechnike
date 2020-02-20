__author__ = 'julesmichaud'
__filename__ = 'Jules.py'
__date__ = '20/02/20'


def tri_days_sign_up(list):
    list.sort(key=lambda x: x["days_signup"], reverse=False)
    return list


def tri_1(list):
    list.sort(key=lambda x: (x["sum_score"]/(x["days_signup"]+x["books_per_day"])), reverse=True)
    return list


def tri_2(list):
    list.sort(key=lambda x: (x["sum_score"]/(x["days_signup"]) - x["books_per_day"]), reverse=True)
    return list