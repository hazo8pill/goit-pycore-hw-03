"""Task 3: normalize phone numbers for SMS delivery."""

import re

COUNTRY_CODE = '38'


def normalize_phone(phone_number: str) -> str:
    """Return `phone_number` as '+' followed by digits only.

    All characters except digits are removed; a '+' is kept only if it
    was the first non-space character. Numbers without an international
    code get Ukraine's: '380...' gets just '+', '0...' gets '+38'.

    Args:
        phone_number: Phone number in any format, e.g. '(050)888-99-00'.

    Returns:
        Normalized number, e.g. '+380508889900'.

    Examples:
        >>> normalize_phone('    +38(050)123-32-34')
        '+380501233234'
        >>> normalize_phone('38050 111 22 11   ')
        '+380501112211'
        >>> normalize_phone('(050)8889900')
        '+380508889900'
    """

    digits = re.sub(r'\D', '', phone_number)

    if phone_number.strip().startswith('+'):
        return '+' + digits  
    if digits.startswith(COUNTRY_CODE):
        return '+' + digits
    return '+' + COUNTRY_CODE + digits