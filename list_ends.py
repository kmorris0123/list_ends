import os




def list_input():
	usr_input = input("Please input a list of numbers: ")
	usr_input = usr_input.replace(", ","")
	usr_input = usr_input.split(",")

	return usr_input


def get_ends(usr_input):
	ends =[]
	ends.append(usr_input[0])
	ends.append(usr_input[-1])

	return ends



def main():
	play = True
	while play == True:
		num_list = list_input()
		print(get_ends(num_list))

		play_again = input('Do you want to play again? "Yes" or "No": ')

		if play_again == "yes":
			play = True
			os.system('clear')
		else:

			play = False






if __name__ == '__main__':

	main()


