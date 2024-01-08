def register_user(name, email, age, gender):
    if name == '':
        raise InvalidNameException

    if age < 18:
        raise UserAgeShouldbeAbove18

    if gender not in [Gender.MALE.value, Gender.FEMALE.value]:
        raise InvalidGenderException

    if email == '':
        raise EmailAlreadyRegistered

    user = create_user()