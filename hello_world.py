'''
My first code. 
Edited by Arun Kumar on 16/05/2025.
@author JGraham
created 25/06/19
'''
import datetime
current_time = datetime.datetime.now()


if current_time.hour < 12:
    print("Good morning")
elif current_time.hour < 18:
    print("Good afternoon")
else:
    print("Good evening")
