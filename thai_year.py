"""thai_year.py

โมดูลแปลงปี พ.ศ. (พุทธศักราช) <-> ค.ศ. (คริสต์ศักราช)

กฎการจำแนกปีที่รับเข้ามา:
- ปี >= 2400 ถือว่าเป็นปี พ.ศ.
- ปี < 2400 ถือว่าเป็นปี ค.ศ.

ผลต่างระหว่าง พ.ศ. และ ค.ศ. คือ 543 ปี (พ.ศ. = ค.ศ. + 543)
"""

BUDDHIST_GREGORIAN_OFFSET = 543
BUDDHIST_YEAR_THRESHOLD = 2400


def _validate_year(year):
    """ตรวจสอบว่า year เป็น int (ไม่รับ bool) มิฉะนั้น raise ValueError"""
    if isinstance(year, bool) or not isinstance(year, int):
        raise ValueError(f"year must be an int, got {type(year).__name__}: {year!r}")


def to_gregorian(year):
    """แปลงปีที่รับเข้ามาให้เป็นปี ค.ศ.

    - ถ้า year >= 2400 (ถือว่าเป็น พ.ศ.) จะลบ 543 แล้วคืนค่าเป็น ค.ศ.
    - ถ้า year < 2400 (ถือว่าเป็น ค.ศ. อยู่แล้ว) จะคืนค่าเดิม
    """
    _validate_year(year)
    if year >= BUDDHIST_YEAR_THRESHOLD:
        return year - BUDDHIST_GREGORIAN_OFFSET
    return year


def to_buddhist(year):
    """แปลงปีที่รับเข้ามาให้เป็นปี พ.ศ.

    - ถ้า year < 2400 (ถือว่าเป็น ค.ศ.) จะบวก 543 แล้วคืนค่าเป็น พ.ศ.
    - ถ้า year >= 2400 (ถือว่าเป็น พ.ศ. อยู่แล้ว) จะคืนค่าเดิม
    """
    _validate_year(year)
    if year < BUDDHIST_YEAR_THRESHOLD:
        return year + BUDDHIST_GREGORIAN_OFFSET
    return year
