

class FSMRule(object):
	def __init__(self):
		self.states = set()
		self.transitions = set()
		self.initial_states = set()
		self.final_states = set()
		self.current_state = None

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

	def add_initial_states(self, states):
		"""obj.add_initial_states(1) or obj.add_initial_states((1, 2))"""
		if type(states) in (int, str):
			self.states.add(states)
			self.initial_states(states)
		else:
			self.states.update(states)
			self.initial_states(states)

	def add_final_states(self, states):
		"""obj.add_final_states(1) or obj.add_final_states((1, 2))"""
		if type(states) in (int, str):
			self.states.add(states)
			self.initial_states(states)
		else:
			self.states.update(states)
			self.initial_states(states)

	def transition(self, state, label):
		"""obj.transition(2, 'a')"""
		if (self.current_state, label, state) in self.transitions:
			self.current_state = state
		else:
			print("Invalid transition!")

	def is_finish(self):
		if self.current_state in self.final_states:
			return True
		return False



