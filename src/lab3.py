from libs.sfm import FSMRule


def main():
	fsm = FSMRule()
	fsm.add_states(1)
	fsm.add_states(2)
	fsm.add_states((3, 4))

	print(fsm.states)

	fsm.add_transitions((1, 'a', 2))
	fsm.add_transitions((1, 'b', 1))

	print(fsm.transitions)


if __name__ == '__main__':
	main()