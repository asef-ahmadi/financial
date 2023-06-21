def eng_to_persian(user_number):
    persian_numbers = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹']
    eng_number = str(user_number)
    persian_number = ''
    for i in range(len(eng_number)):
        num = eng_number[i]
        persian_number.append(num)

    return int(persian_number)
