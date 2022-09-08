# First we will take input of what nominee what we want to keep
nominee1 = input("Enter the Name of 1st Nominee:")
nominee2 = input("Enter the Name of 2nd Nominee:")

# Initially vote count for both must be Zero:

nm1_votes = 0
nm2_votes = 0

voter_id = [1, 2, 3, 4, 5,6,7]

no_of_voter = len(voter_id)

while True:
    if voter_id == []:  # To check when voter list is completed
        print("Voting sesssion is over !!!!")
        if nm1_votes > nm2_votes:
            percent = (nm1_votes / no_of_voter) * 100  # To calculate the Percentge
            print(nominee1, "has won the Election with", percent, "% of votes")
            break  # To get rid of infinite Loop

        elif nm2_votes > nm1_votes:
            percent = (nm2_votes / no_of_voter) * 100
            print(nominee2, "has won the Election with", percent, "% of votes")
            break

        else:
            print("Both have equal number of votes !!! Government will decided who will rule")
            break

    voter = int(input("Enter your voter id :"))
    if voter in voter_id:
        print("You are a voter")
        voter_id.remove(voter)  # We will remove so that again same voter can not vote
        print("======================================")
        print("To give vote to", nominee1, "press 1")
        print("To give vote to", nominee2, "press 2")
        print("=======================================")

        vote = int(input("Enter Your precious vote :"))

        if vote == 1:
            nm1_votes += 1
            print(nominee1, "Thank you to give your important vote to them!!")
        elif vote == 2:
            nm2_votes += 2
            print(nominee2, "Thank you to give your important vote to them!!")
        elif vote > 2:
            print("check your pressed key!!")
        else:
            print("You are not a voter OR You have already voted ")