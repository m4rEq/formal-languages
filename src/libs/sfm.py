

class FSMRule(object):
	def __init__(self):
		self.states = set()
		self.transitions = set()
		# self.initial_states = set()
		self.initial_state = None
		self.final_states = set()
		self.current_state = None
		self.alphabet = set()

	def add_alphabet(self, letters):
		if type(letters) is str:
			self.alphabet.add(letters)
		else:
			self.alphabet.update(letters)

	def add_states(self, states):
		"""obj.add_states(1) or obj.add_states((1, 2))"""
		if type(states) in (int, str):
			self.states.add(states)
		else:
			self.states.update(states)

	def add_transitions(self, trans):
		"""obj.add_transitions((1, 'a', 2))"""
		if trans[0] in self.states and trans[2] in self.states:
			self.transitions.add(trans)
		else:
			print("Unsupported state(s)")

	# def add_initial_states(self, states):
	# 	"""obj.add_initial_states(1) or obj.add_initial_states((1, 2))"""
	# 	if type(states) is int:
	# 		self.initial_states = states
	# 		if self.current_state == None:
	# 			self.current_state = states
	# 	else:
	# 		self.states.update(states)
	# 		self.initial_states = states

	def set_initial_state(self, state):
		if type(state) in (int, str):
			self.initial_state = state
			if self.current_state is None:
				self.current_state = state

	def add_final_states(self, states):
		"""obj.add_final_states(1) or obj.add_final_states((1, 2))"""
		if type(states) in (int, str):
			self.final_states.add(states)
		else:
		 	self.final_states.update(states)

	def transit(self, state, label):
		"""obj.transition(2, 'a')"""
		if (self.current_state, label, state) in self.transitions:
			self.current_state = state
		else:
			print("Invalid transition!")

	def trans(self, label):
		for transit in self.transitions:
			if self.current_state == transit[0] and label == transit[1]:
				print(f"{self.current_state, label} - {transit}")
				self.current_state = transit[2]
				return
		self.current_state = None


	def is_finish(self):
		if self.current_state in self.final_states:
			return True
		return False



