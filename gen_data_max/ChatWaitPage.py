from otree.api import *


doc = """
to do: i need to make sure i get the data from the schedule part which is not clear here yet
"""

# i need to pass the round (which is an integer) and the statement (which is a string)
def Make_Chat_Wait_Page(round_index: int, label : str ):
    class CustomChatWaitPage(WaitPage):
        # make sure all players arrive
        wait_for_all_groups = True


    # aparently, we can return classes :)
    return CustomChatWaitPage