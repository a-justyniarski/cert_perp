import datetime
import locale
import time
from contextlib import contextmanager

from pylatex import NoEscape

from .const import Translators, Exceptions

from logger import get_logger

logger = get_logger(__name__)


def transform_polish_char_to_latex(text: str) -> str:
	text = list(text)
	for idx, letter in enumerate(text):
		if Translators.POLISH_CHARS_TO_LATEX.get(letter):
			text[idx] = Translators.POLISH_CHARS_TO_LATEX.get(letter)
	return "".join(text)


def insert_text_font_f(s: str, fontsize: str, relative_font_size: str = "12", dimension: str = 'pt'):
	return NoEscape(
		f"{{\\fontsize{{{fontsize+dimension}}}{{{relative_font_size+dimension}}}\\selectfont {s}}}"
	)


def recognize_sex(name: str):
	if name.endswith('a') and name not in Exceptions.MALE_NAMES_EXCEPTIONS:
		return 'f'
	elif name in Exceptions.FEMALE_NAMES_EXCEPTIONS:
		return 'f'
	else:
		return 'm'


def format_date(s):
	locale.setlocale(locale.LC_TIME, "pl_PL.UTF-8")
	s = s.strip().strip('r')
	s = s.strip('r.').strip()
	if '.' in s:
		date_list = s.split('.')
	elif '-' in s:
		date_list = s.split('-')
	else:
		date_list = s.split()

	if len(date_list) != 3:
		raise ValueError(f'Unknown date format: {s}')

	if date_list[1].isalpha():
		s = s.replace(date_list[1], Translators.MONTHS_TO_UNIFORM.get(date_list[1], date_list[1]))
		try:
			date_formatted = datetime.datetime.strptime(s, '%d %B %Y').strftime('%d.%m.%Y r.')
		except ValueError as e:
			logger.error(f'{e.__class__.__name__}: Unknown date format: {s}')
			raise
	else:
		date_formatted = ".".join(date_list) + ' r.'

	return date_formatted
