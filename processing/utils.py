from datetime import date
from random import randint
from processing.models import CrateInfo, Crating, Shipping
from users.models import User
from django.utils.crypto import get_random_string


def get_crate_code(user_id):
    last_crate = CrateInfo.objects.count()
    this_crate = last_crate + 1

    for i in range(4 - len(str(this_crate))):  # in '0001' format
        this_crate = '0' + str(this_crate)

    branch_code = User.objects.filter(id=user_id).first().production_house.branch_code
    crate_no = branch_code + this_crate  # 'branch_code' + '0001'

    today = date.today()
    d1 = today.strftime("%d%m%y")  # today in ddmmyy format
    random_num = str(randint(100000, 999999))
    bar_code = random_num + d1

    if CrateInfo.objects.filter(bar_code=bar_code).exists():
        get_crate_code()
    else:
        return crate_no, bar_code


def generate_crating_code():
    today = date.today()
    d1 = today.strftime("%d%m%y")  # today in ddmmyy format
    random_str = get_random_string(6)  # 6 random string using django.utils.crypto
    crating_code = d1 + random_str
    # check for uniqueness
    if Crating.objects.filter(crating_code=crating_code).exists():
        generate_crating_code()
    else:
        return crating_code


def generate_shipping_code():
    today = date.today()
    d1 = today.strftime("%d%m%y")  # today in ddmmyy format
    random_str = get_random_string(6).upper()  # 6 random string using django.utils.crypto
    shipping_code = d1 + random_str
    # check for uniqueness
    if Shipping.objects.filter(shipping_code=shipping_code).exists():
        generate_shipping_code()
    else:
        return shipping_code
