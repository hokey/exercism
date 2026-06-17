"""
Ledger Utility
"""
# -*- coding: utf-8 -*-
from datetime import datetime

LOCALES = {
    "en_US": ("Date", "Description", "Change"),
    "nl_NL": ("Datum", "Omschrijving", "Verandering")
}
CURRENCY = {
    "USD": "$",
    "EUR": "€"
}
PADDING = (11, 26, 13)
DELIMITER = "| "

class LedgerEntry:
    """
    Ledger Entry
    """
    def __init__(self):
        self.date: datetime | None = None
        self.description: str | None = None
        self.change: float | None = None


def create_entry(date: str, description: str, change: float) -> LedgerEntry:
    """
    Create Ledger Entry
    :param datetime date: Date
    :param str description: Description of the entry
    :param float change: Amount change
    :return LedgerEntry: A ledger entry
    """
    entry = LedgerEntry()
    entry.date = datetime.strptime(date, "%Y-%m-%d")
    entry.description = description
    entry.change = change
    return entry


def format_entries(currency: str, locale_str: str, entries: list[LedgerEntry]) -> list[str]:
    """
    Format Ledger Entries
    :param str currency: Currency
    :param str locale_str: Locale
    :param list[LedgerEntry] entries: List of ledger entries
    :return list[str]: Formatted entries
    """
    import locale

    try:
        locale.setlocale(locale.LC_ALL, f"{locale_str}.UTF-8")
    except locale.Error:
        locale.setlocale(locale.LC_ALL, locale_str)

    result: list[str] = []
    result.append(DELIMITER.join([
        f"{LOCALES[locale_str][0]:<{PADDING[0]}}",
        f"{LOCALES[locale_str][1]:<{PADDING[1]}}",
        f"{LOCALES[locale_str][2]:<{PADDING[2]}}"
    ]))
    entries.sort(key=lambda entry: (entry.date, entry.change))
    for entry in entries:
        if locale_str.startswith("nl_NL"):
            date_str = entry.date.strftime("%d-%m-%Y")
        elif locale_str.startswith("en_US"):
            date_str = entry.date.strftime("%m/%d/%Y")
        else:
            raise NotImplementedError
        result.append(DELIMITER.join([
            f"{date_str:<{PADDING[0]}}",
            f"{entry.description[:22] + "..." if len(entry.description) > 26 else entry.description:<{PADDING[1]}}",
            f"{dynamic_formatter(entry.change / 100, locale_str, currency):>{PADDING[2]}}"
        ]))
    return "\n".join(result)


def dynamic_formatter(amount: float, target_locale: str, target_currency: str) -> str:
    """
    Dynamic formatter function
    :param float amount: Amount
    :param str target_locale: Locale
    :param str target_currency: Currency
    :return str:
    """
    symbol: str = CURRENCY.get(target_currency, target_currency)

    abs_amount: float = abs(amount)
    base_format: str = f"{abs_amount:,.2f}"

    if target_locale in ["nl_NL", "nl_NL.UTF-8"]:
        translation: dict[str, str] = str.maketrans({',': '.', '.': ','})
        formatted_number: float = base_format.translate(translation)
        if amount < 0:
            return f"{symbol} -{formatted_number} "
        return f"{symbol} {formatted_number} "
    elif target_locale in ["en_US", "en_US.UTF-8"]:
        formatted: str = f"{symbol}{base_format}"
        if amount < 0:
            return f"({formatted})"
        return f"{formatted} "
    else:
        raise NotImplementedError