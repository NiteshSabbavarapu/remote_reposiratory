def register_user(name, email, age, gender):
    if  name != '':
        if age > 18:
            if gender in [Gender.MALE.value, Gender.FEMALE.value]:
                if email != '':
                    user = create_user()
                    ...
                else:
                    raise EmailAlreadyRegistered
            else:
                raise InvalidGenderException
        else:
            raise UserAgeShouldbeAbove18
    else:
        raise InvalidNameException
