'''(Create large dataset) Create a data file with 1000 lines.
Each line in the file consists of a faculty first name, last name, rank,
and salary. Faculty’s first name and last name for the ith line are
FirstNamei and LastNamei. The rank is randomly generated as assistant,
associate, and full. The salary is randomly generated as a number with
two digits after the decimal point. The salary for assistant professor
should be in the range from 50,000 to 80,000, for associate professor
from 60,000 to 110,000, and for full professor from 75,000 to 130,000.
Save the file in Salary.txt. Here are some sample data:
FirstName1 LastName1 assistant 60055.95 
FirstName2 LastName2 associate 81112.45 
... 
FirstName1000 LastName1000 full 92255.21
'''

import random

fh = open("Salary.txt",'w+')
rank = ["assistant","associate","full"]


for i in range(1,10001):
    rank_index = random.randint(0,2)
    if rank[rank_index] == "assistant":
        salary = round(random.uniform(50000.0,80000.0),2)
    elif rank[rank_index] == "associate":
        salary = round(random.uniform(60000.0, 110000.0),2)
    elif rank[rank_index] == "full":
        salary = round(random.uniform(75000.0, 130000.0),2)
    
    inputString = "FirstName"+str(i)+ " "+ "LastName"+str(i)+ " " +rank[rank_index]+ " " + str(salary) + "\n"
    fh.write(inputString)

fh.close()


