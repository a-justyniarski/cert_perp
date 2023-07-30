import os


class ExcelStructure:
	TRANSLATE_COLUMNS = {
		'imię': "name",
		'nazwisko': "surname",
		'nazwa_szkolenia': "training_title",
		'data': "training_date_list",
		'czas_trwania': "training_duration",
		'zakres_szkolenia': "scope_of_training_list",
		'data_urodzenia_-_potrzebna_do_zaświadczenia': "birthday",
		'miejsce_urodzenia_-_miejscownik': 'birthplace',
		'cert_ident': 'certificate_no',
	}


class Directories:
	participants_excel_file_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'files', 'participants.xlsx')
	trainings_excel_file_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'files', 'trainings.xlsx')


class Translators:
	POLISH_CHARS_TO_LATEX = {
		"ą": "\\k{a}",
		"Ą": "\\k{A}",
		"ę": "\\k{e}",
		"Ę": "\\k{E}",
		"ó": "\\'o",
		"Ó": "\\'O",
		"ś": "\\'s",
		"Ś": "\\'S",
		"ł": "\\l{}",
		"Ł": "\\L{}",
		"ż": "\\.z",
		"Ż": "\\.Z",
		"ź": "\\'z",
		"Ź": "\\'Z",
		"ć": "\\'c",
		"Ć": "\\'C",
		"ń": "\\'n",
		"Ń": "\\'N",
	}

	MONTHS_TO_UNIFORM = {
		"stycznia": "styczeń",
		"lutego": "luty",
		"marca": "marzec",
		"kwietnia": "kwiecień",
		"maja": 'maj',
		"czerwca": "czerwiec",
		"lipca": "lipiec",
		"sierpnia": "sierpień",
		"września": "wrzesień",
		"października": "październik",
		"listopada": "listopad",
		"grudnia": "grudzień",
	}


class Exceptions:
	FEMALE_NAMES_EXCEPTIONS = []
	with open(os.path.join(os.path.dirname(__file__), 'exceptions', 'female_names_exceptions.txt'), 'r') as f_exc:
		for name in f_exc.read().splitlines(keepends=False):
			FEMALE_NAMES_EXCEPTIONS.append(name.capitalize())

	MALE_NAMES_EXCEPTIONS = []
	with open(os.path.join(os.path.dirname(__file__), 'exceptions', 'male_names_exceptions.txt'), 'r') as m_exc:
		for name in m_exc.read().splitlines(keepends=False):
			MALE_NAMES_EXCEPTIONS.append(name.capitalize())


