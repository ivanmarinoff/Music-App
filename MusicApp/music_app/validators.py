from django.core.exceptions import ValidationError

import re


def username_validator(value):
    if not re.match("^\w+$", value):
        raise ValidationError(
            "Ensure this value contains only letters, numbers, and underscore."
        )
