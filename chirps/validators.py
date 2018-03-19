from django.core.exceptions import ValidationError
# a third way to do validations (not used very frequently)
def validate_content(value):
    content = value
    if content == '':
        raise ValidationError("content cannot be blank")

    return value
