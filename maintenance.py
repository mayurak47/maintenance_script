import requests
import sys

r = requests.get(sys.argv[1])

from bs4 import BeautifulSoup

soup = BeautifulSoup(r.text, 'html.parser')

single = str(soup.find_all('td', attrs={'class':'score', 'rowspan':3}))[31:35]
multi = str(soup.find_all('td', attrs={'class':'score', 'rowspan':3}))[72:76]

file = open("history.csv", "a")
file.write(single+','+multi+'\n')
file.close()

import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("/Users/mayurarvind/maintenance/history.csv", delimiter=',')
length = range(1, len(data[:,0])+1)

plt.plot(length, data[:,0])
plt.plot(length, data[:,1])
plt.savefig('graph.png')
