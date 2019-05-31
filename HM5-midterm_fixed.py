import pandas as pd
import seaborn as sns
import requests as req
import matplotlib.pyplot as plt

# Task1
# I did not know what is algae! so I searched about it:
# Cyanobacteria and algae having complex photosynthetic
# systems can channelize absorbed solar energy into other
# forms of energy for production of food and metabolites.
# In addition, they are promising biocatalysts and can be
# used in the field of “white biotechnology” for enhancing
# the sustainable production of food, metabolites, and green
# energy sources such as biodiesel.
# creating dataframe
algae = pd.read_csv('/home/sedreh/ITMO/semester2/Biopython/session5/algae.csv')
# at first I look at the data to understand it
print(algae)

# The question is: Using ​ pandas ​library find the average concentration
# of each of the metabolite in each algae genus.
# here we need genus and group column to calculate mean value! so, we can take
# average or mean of the dataframe by pandas like: df.mean()
# but at first we need groupby() function to group the data based on the “genus”.
# Then plot it using saborn package

algae = pd.DataFrame(algae)
print(algae)


gk = algae.groupby(['genus'])
df = gk.mean()
algae.data = pd.DataFrame(df)
print(algae.data)

plt.plot(algae.data)
plt.show()


# Task2
# Task at first wants to make iterator with map and lambda function! lambda is
# Anonymous function because it doesn’t get a name!
# and map function applies the function to each item in the list, returning another list
# we can write z = list(map(lambda x: x%3==0, numbers)) but the question is about map(lambda(..))
# The method next() is used when a file is used as an iterator, typically in a loop, the next() method
# is called repeatedly.
# example: mylist = iter(["apple", "banana", "cherry"])
# x = next(mylist)
# print(x)
# x = next(mylist)
# print(x)
# apple
# banana

# Exceptions are convenient in many ways for handling errors and special conditions
# in a program. When we think that we have a code which can produce an error then
# we can use exception handling which avoids program to crash.

numbers = [1, 2, 3, 4, 5, 6]
my_iter = map(lambda x: x % 3 == 0, numbers)
while True:
    try:
        print(next(my_iter))
    except StopIteration:
        break

# Task3
# This task wants us to get information of 4 number about math and history of them from site.
# we should use request package for it
numbers = [17, 45, 999, 1883]
for number in numbers:
    req_math = req.get(f'http://numbersapi.com/{number}/math')
    print(f'mathematical information for number {number}: {req_math.text}')

    req_date = req.get(f'http://numbersapi.com/{number}/date')
    print(f'historical information for number {number}: {req_date.text}')
