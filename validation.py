def validate_field(data, field, expected_type):
    if field not in data:
        return False
    if not isinstance(data[field], expected_type):
        return False
    return True


def validate_fields(data, fields):
    for field, expected_type in fields:
        if not validate_field(data, field, expected_type):
            return False
    return True
