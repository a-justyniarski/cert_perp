import os

from numpy import NaN
from pylatex import Document, StandAloneGraphic, NoEscape, Package, TextBlock, Command, TextColor, Itemize, \
	FlushLeft, LineBreak
from pylatex.utils import bold

from customs.func import *
from customs.func import transform_polish_char_to_latex, insert_text_font_f, recognize_sex, format_date
from customs.const import *
from customs.const import ExcelStructure


class CertPrepGeneral:
	_header: str = 'Zaświadczenie'
	_subheader: str = 'Zaświadcza się, że {}'
	_birth_text: str = 'ur. {}, {}'
	_header_training: str = 'ukończył{} szkolenie:'
	_policy_statement_text: str = """Zaświadczenie nr 10/2020 o wpisie Niepublicznej Placówki Doskonalenia Nauczycieli 
	Instytut Educare, do ewidencji niepublicznych placówek doskonalenia nauczycieli mających siedzibę na terenie 
	województwa śląskiego z dnia 23.09.2020 r. pod numerem 9"""
	_training_scope_header: str = 'Zakres szkolenia'
	_title_person_authorised: str = transform_polish_char_to_latex('Dyrektor ds. kształcenia')
	_person_authorised: str = transform_polish_char_to_latex('Elżbieta Wagner')

	def __init__(
			self,
			name='',
			surname='',
			birthday='',
			birthplace='',
			training_title='',
			training_date_list: list = '',
			training_duration: int = '',
			scope_of_training_list='',
			person_authorized='',
			title_person_authorized='',
			certificate_no='TEST/2022',
			policy_statement_text=_policy_statement_text,
			**kwargs
	):
		kwarg_keys = list(kwargs.keys())
		for key in kwarg_keys:
			translated_key = ExcelStructure.TRANSLATE_COLUMNS.get(key)
			if translated_key:
				kwargs[translated_key] = kwargs.pop(key)

		self.name = kwargs.get('name') or name
		self.name = "-".join([i.capitalize() for i in self.name.split('-')]).strip()
		self.surname = kwargs.get('surname') or surname
		self.surname = "-".join([i.capitalize() for i in self.surname.split('-')]).strip()
		self.birthday = kwargs.get('birthday') or birthday
		self.birthday = format_date(self.birthday)
		self.birthplace = kwargs.get('birthplace') or birthplace
		self.training_title = kwargs.get('training_title') or training_title
		self.training_date_list = kwargs.get('training_date_list') or training_date_list
		self.training_duration = kwargs.get('training_duration') or training_duration
		self.scope_of_training_list = kwargs.get('scope_of_training_list') or scope_of_training_list
		self.policy_statement_text = kwargs.get('policy_statement_text') or policy_statement_text
		self.person_authorized = kwargs.get('person_authorized') or person_authorized
		self.title_person_authorized = kwargs.get('title_person_authorized') or title_person_authorized
		self.certificate_no = kwargs.get('certificate_no') if not NaN else certificate_no
		self.sex = recognize_sex(self.name)

		self.document = self.generate_doc()

	# noinspection Py
	@property
	def header(self):
		return self._header

	@header.setter
	def header(self, new_value):
		self._header = transform_polish_char_to_latex(new_value)

	@property
	def subheader(self):
		return self._subheader

	@subheader.setter
	def subheader(self, new_value):
		self._subheader = transform_polish_char_to_latex(new_value)

	@property
	def birth_text(self):
		return self._birth_text

	@birth_text.setter
	def birth_text(self, new_value):
		self._birth_text = transform_polish_char_to_latex(new_value)

	@property
	def header_training(self):
		return self._header_training

	@header_training.setter
	def header_training(self, new_value):
		self._header_training = transform_polish_char_to_latex(new_value)

	@property
	def training_scope_header(self):
		return self._training_scope_header

	@training_scope_header.setter
	def training_scope_header(self, new_value):
		self._training_scope_header = transform_polish_char_to_latex(new_value)

	@property
	def policy_statement_text(self):
		return self._policy_statement_text

	@policy_statement_text.setter
	def policy_statement_text(self, new_value):
		self._policy_statement_text = transform_polish_char_to_latex(new_value)

	@property
	def title_person_authorised(self):
		return self._title_person_authorised

	@title_person_authorised.setter
	def title_person_authorised(self, new_value):
		self._title_person_authorised = transform_polish_char_to_latex(new_value)

	@property
	def person_authorised(self):
		return self._person_authorised

	@person_authorised.setter
	def person_authorised(self, new_value):
		self._person_authorised = transform_polish_char_to_latex(new_value)

	@staticmethod
	def generate_doc() -> Document:
		document_class = 'article'
		document_options = ['a4paper', 'notitlepage', 'polish', 'ngerman']
		geometry_options = {
			"margin": "0in",
			"includeheadfoot": False,
		}

		doc = Document(
			documentclass=document_class,
			document_options=document_options,
			geometry_options=geometry_options,
			page_numbers=False,
		)

		return doc

	def prepare_preamble(self) -> None:
		self.document.change_length('\\TPHorizModule', '1cm')
		self.document.change_length('\\TPVertModule', '1cm')

		packages = [
			Package('tikz'),
			Package('graphicx'),
			Package('xcolor'),
			Package('textpos', options=["absolute", "overlay"]),
			Package('csquotes', options="autostyle"),
			Package('babel'),
		]

		for package in packages:
			self.document.packages.append(package)

	def set_background(self, bg_path=None):
		if not bg_path:
			bg_path = 'background.jpg'
			# bg_path = 'background.png'
		bg_img = StandAloneGraphic(filename=bg_path, image_options=NoEscape(r"width=\paperwidth,height=\paperheight"))
		self.document.append(
			NoEscape(
				f"\\tikz[remember picture,overlay] \\node at (current page.center) {{{bg_img.dumps()}}};"
			)
		)

	def append_header(
			self, text: str = _header, font_size: float = 50, upper: bool = True,
			width: float = 20, vertical_pos: float = 4.5, horizontal_pos: float = 0
	) -> None:
		text = text.upper() if upper else text
		header = NoEscape(transform_polish_char_to_latex(text))
		h_font_size = str(font_size)
		h1_block = TextBlock(width=width, vertical_pos=vertical_pos, horizontal_pos=horizontal_pos)
		h1_block.append(Command('centering'))
		h1_block.append(insert_text_font_f(bold(header), h_font_size))
		self.document.append(h1_block)

	def append_underline(
			self, line_width: float = 0.5, line_thickness: float = 1.5, width: float = 20, vertical_pos: float = 6.9,
			horizontal_pos: float = 0, line_color: str = 'orange',
	) -> None:
		line_block = TextBlock(width=width, vertical_pos=vertical_pos, horizontal_pos=horizontal_pos)
		line_block.append(Command('centering'))
		line_block.append(TextColor(
			line_color,
			Command(
				'rule',
				arguments=NoEscape(f'{line_width}\\paperwidth'),
				extra_arguments=NoEscape(f'{line_thickness}pt')
			)
		))
		self.document.append(line_block)

	def append_subheader(
			self, text: str = _subheader, font_size: float = 15,
			width: float = 20, vertical_pos: float = 8, horizontal_pos: float = 0,
	) -> None:
		title_of_respect = 'Pan' if self.sex == 'm' else 'Pani'
		header2 = text.format(title_of_respect)
		h2_font_size = str(font_size)
		h2_block = TextBlock(width=width, vertical_pos=vertical_pos, horizontal_pos=horizontal_pos)
		h2_block.append(Command('centering'))
		h2_block.append(insert_text_font_f(bold(header2), h2_font_size))
		self.document.append(h2_block)

	def append_name(
			self, text_color: str = 'orange', font_size: float = 15, width: float = 20, vertical_pos: float = 9.5,
			horizontal_pos: float = 0,
	) -> None:
		name_formatted = TextColor(
			text_color,
			bold(NoEscape(transform_polish_char_to_latex(
				f"{self.name} {self.surname}"))
			)
		).dumps()
		name_font_size = str(font_size)
		name_block = TextBlock(width=width, vertical_pos=vertical_pos, horizontal_pos=horizontal_pos)
		name_block.append(Command('centering'))
		name_block.append(insert_text_font_f(name_formatted, name_font_size))
		self.document.append(name_block)

	def append_birthday(
			self, text: str = None, font_size: float = 10, width: float = 20, vertical_pos: float = 10.8,
			horizontal_pos: float = 0,
	):
		if not text:
			text = self._birth_text.format(self.birthday, self.birthplace)
		name_font_size = str(font_size)
		birth_block = TextBlock(width=width, vertical_pos=vertical_pos, horizontal_pos=horizontal_pos)
		birth_block.append(Command('centering'))
		birth_block.append(insert_text_font_f(text, name_font_size))
		self.document.append(birth_block)

	def append_training_header(
			self, text: str = _header_training, font_size: float = 15, width: float = 20,
			vertical_pos: float = 12, horizontal_pos: float = 0,
	) -> None:
		training_h_font_size = str(font_size)
		try:
			text = text.format('a' if self.sex == 'f' else '')
		except IndexError:
			text = text
		text = bold(text)
		training_h_block = TextBlock(width=width, vertical_pos=vertical_pos, horizontal_pos=horizontal_pos)
		training_h_block.append(Command('centering'))
		training_h_block.append(insert_text_font_f(text, training_h_font_size))
		self.document.append(training_h_block)

	def append_training_name(
			self, training_title: str = None, quotes: bool = True, font_size: float = 25, width: float = 20,
			vertical_pos: float = 13.2, horizontal_pos: float = 0,
	) -> None:
		training_name_font_size = str(font_size)
		if not training_title:
			training_title = self.training_title
		if quotes:
			training_title = f'\\enquote{{{bold(training_title)}}}'
		else:
			training_title = bold(training_title)
		training_name_block = TextBlock(width=width, vertical_pos=vertical_pos, horizontal_pos=horizontal_pos)
		training_name_block.append(Command('centering'))
		training_name_block.append(insert_text_font_f(training_title, training_name_font_size))
		self.document.append(training_name_block)

	def append_training_date(
			self, training_date_list: list = None, training_date_text: str = None, training_duration: float = None,
			font_size: float = 12, width: float = 20, vertical_pos: float = 15, horizontal_pos: float = 0,
	) -> None:
		if not training_date_list:
			training_date_list = self.training_date_list
		if not training_duration:
			training_duration = self.training_duration
		training_date_font_size = str(font_size)
		training_date_block = TextBlock(width=width, vertical_pos=vertical_pos, horizontal_pos=horizontal_pos)
		training_date_block.append(Command('centering'))
		training_date_list_text = ", ".join(training_date_list)
		if not training_date_text:
			training_date_text = f'w {"dniach" if len(training_date_list) > 1 else "dniu"} {training_date_list_text}, '\
				f'w wymiarze {int(training_duration) if training_duration.is_integer() else training_duration} ' \
				f'{"godziny" if training_duration == 1 else "godzin"}'

		training_date_block.append(insert_text_font_f(training_date_text, training_date_font_size))
		self.document.append(training_date_block)

	def append_training_scope_header(
			self, text: str = _training_scope_header, upper_header: bool = True, font_size: float = 15,
			width: float = 20, vertical_pos: float = 17, horizontal_pos: float = 1.2,
	) -> None:
		training_scope_h_font_size = str(font_size)
		training_scope_h_block = TextBlock(width=width, vertical_pos=vertical_pos, horizontal_pos=horizontal_pos)
		training_scope_h_text = bold(text.upper() if upper_header else text)
		training_scope_h_block.append(insert_text_font_f(training_scope_h_text, training_scope_h_font_size))
		self.document.append(training_scope_h_block)

	def append_training_scope(
			self, scope_of_training: list = None, font_size: float = 10, width: float = 18, vertical_pos: float = 17.8,
			horizontal_pos: float = 0.7,
	) -> None:
		if not scope_of_training:
			scope_of_training = self.scope_of_training_list
		training_scope_font_size = str(font_size)
		training_scope_block = TextBlock(width=width, vertical_pos=vertical_pos, horizontal_pos=horizontal_pos)
		training_scope_list_container = Itemize()
		for bullet_point in scope_of_training:
			training_scope_list_container.add_item(insert_text_font_f(bullet_point, training_scope_font_size))
		training_scope_block.append(training_scope_list_container)
		self.document.append(training_scope_block)

	def append_policy_statement(
			self, text: str = _policy_statement_text, font_size: float = 10, width: float = 19,
			vertical_pos: float = 25, horizontal_pos: float = 1.2,
	) -> None:
		policy_statement_font_size = str(font_size)
		policy_statement_block = TextBlock(width=width, vertical_pos=vertical_pos, horizontal_pos=horizontal_pos)
		policy_statement_block_l_align = FlushLeft()
		policy_statement_block_l_align.append(insert_text_font_f(text, policy_statement_font_size))
		policy_statement_block.append(policy_statement_block_l_align)
		self.document.append(policy_statement_block)

	def append_sign_space(
			self, title_person_authorised: str = _title_person_authorised, person_authorised: str = _person_authorised,
			font_size: float = 10, width: float = 20, vertical_pos: float = 28, horizontal_pos: float = 0,
	) -> None:
		sign_space_font_size = str(font_size)
		sign_space_block = TextBlock(width=width, vertical_pos=vertical_pos, horizontal_pos=horizontal_pos)
		sign_space_block.append(Command('centering'))
		sign_space_block.append(insert_text_font_f('.'*40, sign_space_font_size))
		sign_space_block.append(LineBreak())
		sign_space_block.append(insert_text_font_f(title_person_authorised, sign_space_font_size))
		sign_space_block.append(LineBreak())
		sign_space_block.append(insert_text_font_f(person_authorised, sign_space_font_size))
		self.document.append(sign_space_block)

	def append_certificate_no(
			self, certificate_no: str = None, font_size: float = 11, width: float = 18, vertical_pos: float = 27.7,
			horizontal_pos: float = 1.2,
	) -> None:
		if not certificate_no:
			certificate_no = self.certificate_no
		certificate_no_font_size = str(font_size)
		certificate_no_block = TextBlock(width=width, vertical_pos=vertical_pos, horizontal_pos=horizontal_pos)
		certificate_no_l_align = FlushLeft()
		certificate_no_l_align.append(insert_text_font_f(f'Nr {certificate_no}', certificate_no_font_size))
		certificate_no_block.append(certificate_no_l_align)
		self.document.append(certificate_no_block)

	def prepare_certificate_pdf(self):
		self.prepare_preamble()
		self.set_background()
		self.append_header()
		self.append_underline()
		self.append_subheader()
		self.append_name()
		self.append_birthday()
		self.append_training_header()
		self.append_training_name()
		self.append_training_date()
		self.append_training_scope_header()
		self.append_training_scope()
		self.append_policy_statement()
		self.append_sign_space()
		self.append_certificate_no()

	def generate_pdf(self):
		self.prepare_certificate_pdf()
		try:
			os.mkdir('defaults')
		except FileExistsError:
			pass
		self.document.generate_pdf(
			f'defaults/{self.name.lower()}_{self.surname.lower()}_{self.certificate_no.replace("/", "_")}'
		)
