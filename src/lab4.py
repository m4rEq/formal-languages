
from libs.sfm import FSMRule


def main():
	fsm = FSMRule()

	fsm.add_alphabet(('a', 'b', 'c', 'd'))
	fsm.add_states(('q0', 'q1', 'q2', 'q3'))

	fsm.set_initial_state('q0')

	fsm.add_final_states(('q0', 'q1', 'q3'))

	print(f"All states: {fsm.states}")
	print(f"Current state: {fsm.current_state}")
	print(f"Is it finish state? {fsm.is_finish()}")
	print("======================================")

	fsm.add_transitions(('q0', 'a', 'q2'))
	fsm.add_transitions(('q2', 'b', 'q1'))
	fsm.add_transitions(('q0', 'c', 'q1'))
	fsm.add_transitions(('q0', 'd', 'q3'))
	fsm.add_transitions(('q3', 'd', 'q3'))

	word = input("Enter word: ")

	for i in word:
		fsm.trans(i)
		print(f"Current state: {fsm.current_state}")
		print(f"Is it finish state? {fsm.is_finish()}")
		print("======================================")
	

if __name__ == '__main__':
	main()