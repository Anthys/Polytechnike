__author__ = 'julesmichaud'
__filename__ = 'Jules.py'
__date__ = '20/02/20'


def tri_days_sign_up(list):
    list.sort(key=lambda x: x["days_signup"], reverse=False)
    return list

