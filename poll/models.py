from django.db import models

""" 
    each poll has a question and three options. 
    each option has a option counter to count the votes of each option for a consideration poll.
"""


class Poll( models.Model ):
    question = models.TextField()
    option_1 = models.CharField( max_length=100, help_text='option 1' )
    option_2 = models.CharField( max_length=100, help_text='option 2' )
    option_3 = models.CharField( max_length=100, help_text='option 3' )
    option_1_counter = models.IntegerField( default=0, help_text='counter for option 1' )
    option_2_counter = models.IntegerField( default=0, help_text='counter for option 2' )
    option_3_counter = models.IntegerField( default=0, help_text='counter for option 3' )

    def __str__(self):
        return self.question
