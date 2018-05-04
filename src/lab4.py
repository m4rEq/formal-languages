
from libs.sfm import FSMRule


def main():
	fsm = FSMRule()

	fsm.add_alphabet(('a', 'b', 'c', 'd'))
	fsm.add_states(('q0', 'q1', 'q2', 'q3', 'F'))

	fsm.set_initial_state('q0')

	fsm.add_final_states(('q0', 'q2', 'F'))

	print(f"All states: {fsm.states}")
	print(f"Current state: {fsm.current_state}")
	print(f"Is it finish state? {fsm.is_finish()}")
	print("======================================")

	fsm.add_transitions(('q0', 'a', 'q1'))
	fsm.add_transitions(('q1', 'b', 'F'))
	fsm.add_transitions(('q0', 'c', 'F'))
	fsm.add_transitions(('q0', 'd', 'q2'))
	fsm.add_transitions(('q2', 'd', 'q2'))

	word = "cd"

	for i in word:
		fsm.trans(i)
		print(f"Current state: {fsm.current_state}")
		print(f"Is it finish state? {fsm.is_finish()}")
		print("======================================")
	

if __name__ == '__main__':
	main()