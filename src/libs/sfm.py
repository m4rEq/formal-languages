

class FSMRule(object):
	# def __init__(self, state, label, next_state):
	# 	self.state = state
	# 	self.label = label 
	# 	self.next_state = next_state

	# def is_apply(self, state, label):
	# 	return self.state == state and self.label == label  

	# def transition(self):
	# 	return self.next_state

	def __init__(self):
		self.states = set()
		self.transitions = set()
		self.initial_states = set()
		self.final_states = set()

	def add_states(self, states):
		if type(states) in (int, str):
			self.states.add(states)
		else:
			self.states.update(states)

	def add_transitions(self, trans):
		if trans[0] in self.states and trans[2] in self.states:
			self.transitions.add(trans)
		else:
			print("Unsupported state(s)")

