import time

from cert_general import CertPrepGeneral
from cert_tutoring import CertPrepTutoring
from cert_main import CertPrepMain
from excel import ExcelManipulation
from logger import get_logger

logger = get_logger(__name__)
excel_manipulation = ExcelManipulation()


def generate_single_certificate(data, certificate_class):
	try:
		certificate = certificate_class(**data)
		certificate.generate_pdf()
	except Exception as e:
		logger.error(f"{e!r}", exc_info=True)


def generate_pdfs(data: list, certificate_class, test: bool = False, id_: int | tuple = None):
	if (
			test
			and (
				not id_
				or (id_ > len(data) if isinstance(id_, int) else id_[1] > len(data))
				or (id_ < 0 if isinstance(id_, int) else id_[1] < 0)
			)
	):
		raise ValueError(f'Invalid row id: {id_}')
	if test:
		if isinstance(id_, int):
			idx_test = data.index(next(filter(lambda x: x.get('id') == float(id_), data), 1))
			data = data[idx_test: idx_test+1]
		elif isinstance(id_, tuple):
			idx_start = data.index(next(filter(lambda x: x.get('id') == float(id_[0]), data)))
			idx_stop = data.index(next(filter(lambda x: x.get('id') == float(id_[1]), data)))
			data = data[idx_start: idx_stop+1]
	prog_start = time.perf_counter()
	for idx, d in enumerate(data, start=1):
		start = time.perf_counter()
		generate_single_certificate(d, certificate_class=certificate_class)
		end = time.perf_counter()
		print(
			f'\033[KProgress: {round(idx*100/len(data), 1)} %. Time: {round(end-start, 2)}. '
			f'Time total: {round(end-prog_start, 2)}', end='\r'
		)
	logger.info('Task finished')


if __name__ == '__main__':
	# generate_pdfs(excel_manipulation.prepare_data(), CertPrepMain)
	generate_pdfs(excel_manipulation.prepare_data(), CertPrepMain, test=True, id_=423)
