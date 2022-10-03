'''
Hy: Henry Bach, Yuki Feng
SoftDev
K06 -- <Title/Topic/Summary... (Aim for concision, brevity, CLARITY. Write to your future self...)>
2022-9-30
time spent: 2.5
DISCO:
maxsplit does nice things
QCC:
What is the name of this assignment?
'''

import random as rng

def readFile() :
    file_text = open("occupations.csv").read()
    jobs = file_text.split("\n")
    new_dict = {}
    for job in jobs[1:-2] : # Look at every job excluding the first line and last lines
        job = job[::-1] # Reverse the string
        (percentage, occupation) = job.split(",", maxsplit=1) # Split the string once, and set percentage and occupation
        percentage = (float)(percentage[::-1]) # Re-reverse percentage and convert it to a float
        occupation = occupation[::-1] # Re-reverse occupation
        if occupation not in list(new_dict) :
            new_dict[occupation] = percentage # Add the job
    return new_dict

def randOccupation() :
    job_dict = readFile() #reads file
    occupations = [] #create empty list
    for occupation in list(job_dict) : #iterate
        percentage = job_dict[occupation] #grabs occupation percentage
        for i in range((int)(percentage*10)):
            occupations.append(occupation) #adds occupation based on Percentage
    job = rng.choice(occupations) #random job
    return job + ": " + (str)(job_dict[job]) #returns said job and corresponding percentage

print(randOccupation())
