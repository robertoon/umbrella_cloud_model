import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from math import sqrt
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Verdana']
rcParams['font.size'] = 10

p1 = [0, 40]
p2 = [0, 40]

X, Y = [], []
x, y = np.genfromtxt(r'./output_test1.txt', unpack = True)

for idx, lon in enumerate(x):
        X.append(lon)
        Y.append(y[idx])

m, b = np.polyfit(x, y, 1)  # calculate regression line equation (y)
r = np.corrcoef(x, y)[1, 0]  # calculate correlation coefficient (r)
RMSE = sqrt(np.square(np.subtract(X, Y)).mean())  # calculate root mean square error (RMSE)


plt.scatter(X, Y, marker='o', color='#FAA300', edgecolor='black', linewidth='0.5')
plt.plot(p1, p2, color='k', linewidth = 0.8, linestyle='--')
plt.plot(x, m * x + b, linestyle='-', linewidth = 0.8, color='k')

#plt.legend(frameon=False)
plt.text(1, 36, 'y = {:.2f}x+{:.2f}'.format(m, b))
plt.text(1, 34, 'r = {:.2f}'.format(r))
plt.text(1, 32, 'RMSE = {:.2f}'.format(RMSE))
plt.text(1, 30, '$\chi^2$ = 1806')
plt.axis([0,40, 0, 40], aspect="auto")
plt.xlabel('Observed thickness (cm)', fontsize=12)
plt.ylabel('Modeled thickness (cm)', fontsize=12)
plt.title('Disk source')
#plt.show()
plt.savefig('Equiline_plot.png', figsize=(3.5, 1.75), dpi=300, facecolor='w', edgecolor='k')
