import pandas as pd

from customs.const import Directories
from logger import get_logger

logger = get_logger(__name__)


class ExcelManipulation:
	def __init__(
			self,
			participants_xlsx_path: str = Directories.participants_excel_file_dir,
			trainings_xlsx_path: str = Directories.trainings_excel_file_dir
	):
		self.participants_xlsx_path = participants_xlsx_path
		self.participants_xlsx = pd.read_excel(self.participants_xlsx_path, 0)
		self.renamed_participants_xlsx = self.participants_xlsx
		self.renamed_participants_xlsx.columns = self.renamed_participants_xlsx.columns.str.strip() \
			.str.lower().str.replace(' ', '_')
		self.trainings_xlsx_path = trainings_xlsx_path
		self.trainings_xlsx = pd.read_excel(self.trainings_xlsx_path, 0)
		self.renamed_trainings_xlsx = self.trainings_xlsx
		self.renamed_trainings_xlsx.columns = self.renamed_trainings_xlsx.columns.str.strip()\
			.str.lower().str.replace(' ', '_')

	def parse_trainings(self) -> dict:
		try:
			trainings_dict = dict()
			for training in self.renamed_trainings_xlsx.iterrows():
				if not isinstance(training[1].get('nazwa_szkolenia'), str):
					continue
				training[1]['zakres_szkolenia'] = [i for i in training[1]['zakres_szkolenia'].split(';') if i != '']
				training[1]['data'] = [i for i in training[1]['data'].split(';') if i != '']
				trainings_dict.update({training[1].get('nazwa_szkolenia').lower(): training[1].to_dict()})
			return trainings_dict
		except FileNotFoundError as e:
			logger.error(e)
			return dict()

	def parse_participants(self) -> list:
		participants: list = list()
		for participant in self.renamed_participants_xlsx.iterrows():
			participants.append(participant[1].to_dict())
		return participants

	def prepare_data(self):
		trainings = self.parse_trainings()
		data = list()
		for idx, participant in enumerate(self.parse_participants()):
			training_col_name = "".join(filter(lambda x: 'wybierz_szkolenie' in x, participant.keys()))
			if not isinstance(participant.get(training_col_name), str):
				continue
			try:
				participant.update(trainings.get(participant.get(training_col_name).lower()))
			except TypeError:
				pass
			data.append(participant)
			logger.info(participant)
		data.sort(key=lambda x: x.get('id'))
		return data

	def update_participants_ident_fields(self, training_stamp_ident: str, last_ident: int):
		pass

	def update_training_last_ident_fields(self, training_ident: str):
		training_row = self.trainings_xlsx_path[self.trainings_xlsx_path['IDENT'] == training_ident]
