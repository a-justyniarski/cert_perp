import time

from cert_general import CertPrepGeneral
from cert_tutoring import CertPrepTutoring
from cert_main import CertPrepMain
from excel import ExcelManipulation
from logger import get_logger

logger = get_logger(__name__)
excel_manipulation = ExcelManipulation()


def generate_single_certificate(data, certificate_class):
	certificate = certificate_class(**data)
	certificate.generate_pdf()


def generate_pdfs(data: list, certificate_class, test: bool = False, id_: int = None):
	if test and (not id_ or id_ > len(data) or id_ < 0):
		logger.debug(data)
		raise ValueError(f'Invalid row id: {id_}')
	if test:
		idx_test = data.index(next(filter(lambda x: x.get('id') == float(id_), data), 0))
		data = data[idx_test: idx_test+1]

	for idx, d in enumerate(data, start=1):
		start = time.perf_counter()
		generate_single_certificate(d, certificate_class=certificate_class)
		end = time.perf_counter()
		logger.info(f'Progress: {round(idx*100/len(data), 1)} %. Time: {round(end-start, 2)}')


if __name__ == '__main__':
	# generate_pdfs(excel_manipulation.prepare_data(), CertPrepMain)
	generate_pdfs(excel_manipulation.prepare_data(), CertPrepMain, test=True, id_=422)

