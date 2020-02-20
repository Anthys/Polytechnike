__author__ = 'julesmichaud'
__filename__ = 'Jules.py'
__date__ = '20/02/20'



def tri_days_sign_up(list):
    list.sort(key=lambda x: x["days_signup"], reverse=False)
    return list


def tri_1(list):
    list.sort(key=lambda x: (x["sum_score"]/(x["books_per_day"]+x["days_signup"])), reverse=True)
    return list


def tri_2(list):
    list.sort(key=lambda x: (x["sum_score"]/x["books_per_day"] - x["days_signup"]), reverse=True)
    return list


list = [{"sum_score": 10, "books_per_day": 2, "days_signup": 3}, {"sum_score": 9, "books_per_day": 3, "days_signup": 4}]

print(tri_2(list))