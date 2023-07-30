from pylatex import Command
from pylatex.base_classes import Environment, Arguments


class TextBlock(Environment):
	def __init__(self, *args, arguments=None, coordinates: tuple | None, star: bool = False, **kwargs):
		self.coordinates = coordinates
		self._latex_name = 'textblock'
		if star:
			self._latex_name += '*'
		super().__init__(*args, **kwargs)

	def dumps(self):
		"""Represent the environment as a string in LaTeX syntax.

		Returns
		-------
		str
			A LaTeX string representing the environment.
		"""

		content = self.dumps_content()
		if not content.strip() and self.omit_if_empty:
			return ''

		string = ''

		# Something other than None needs to be used as extra arguments, that
		# way the options end up behind the latex_name argument.
		if self.arguments is None:
			extra_arguments = Arguments()
		else:
			extra_arguments = self.arguments

		begin = Command('begin', self.start_arguments, self.options, extra_arguments=extra_arguments)
		begin.arguments._positional_args.insert(0, self.latex_name)
		begin.arguments._positional_args.insert(-1, self.coordinates)
		string += begin.dumps() + self.content_separator

		string += content + self.content_separator

		string += Command('end', self.latex_name).dumps()

		return string
