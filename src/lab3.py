from libs.sfm import FSMRule


def main():
	fsm = FSMRule()

	fsm.add_alphabet(('a', 'b'))


	fsm.add_states(1)
	fsm.add_states(2)
	fsm.add_states((3, 4))

	fsm.add_initial_states(1)
	fsm.add_final_states(4)

	print(fsm.states)

	fsm.add_transitions((1, 'a', 2))
	fsm.add_transitions((2, 'a', 1))
	fsm.add_transitions((2, 'b', 3))
	fsm.add_transitions((3, 'a', 2))
	fsm.add_transitions((3, 'b', 4))
	fsm.add_transitions((2, 'a', 4))
	

	print(f"current state = {fsm.current_state}\n")

	fsm.transit(2, 'a')
	print(f"current state = {fsm.current_state}")
	print(f"is finish? {fsm.is_finish()}\n")

	fsm.transit(4, 'a')
	print(f"current state = {fsm.current_state}")
	print(f"is finish? {fsm.is_finish()}\n")


	fsm.transit(3, 'b')
	print(f"current state = {fsm.current_state}")
	print(f"is finish? {fsm.is_finish()}\n")

	fsm.transit(4, 'b')
	print(f"current state = {fsm.current_state}")
	print(f"is finish? {fsm.is_finish()}\n")



if __name__ == '__main__':
	main()