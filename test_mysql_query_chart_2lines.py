#created by Jess Valdez
#sometime in march 2016

import datetime
import mysql.connector
from mysql.connector import errorcode

import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(1,1,1)

config = {
    'user': 'jess',
    'password': 'vhanmiaka',
    'host': 'dig1',
    'database': 'battery',
    'raise_on_warnings': True,
}

try:
    cnx = mysql.connector.connect(**config)


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
    
print("Connected to dig1 battery Database.")
cursor = cnx.cursor()

query = ("SELECT runtime, Vbat_sw, Vbat_ocv FROM discharge_lfs "
         "WHERE runtime BETWEEN %s AND %s")

start = 27
end = 5890

cursor.execute(query, (start, end))

z = 0

for (runtime, Vbat_sw, Vbat_ocv) in cursor:
    print('> {}=>{}' .format( runtime, Vbat_sw, Vbat_ocv))
    if z==0:
        x = [runtime]
        y = [Vbat_sw]
        y2 = [Vbat_ocv]
    x.append(runtime)
    y.append(Vbat_sw)
    y2.append(Vbat_ocv)
    z=z+1
    
cursor.close()
cnx.close()

ax.plot(x, y, linewidth=3, color='b', label='Vbat_sw')
ax.plot(x, y2, linewidth=3, color='r', label='Vbat_ocv')
ax.grid()
ax.legend()
ax.set_ylim([2.0,4.5])
ax.set_title('Battery rundown',fontsize=12,color='b')
#pyplot.set_title('Battery rundown',fontsize=12,color='b')

plt.ylabel('Vbatt (V)')
plt.xlabel('Time (s)')
plt.show()


