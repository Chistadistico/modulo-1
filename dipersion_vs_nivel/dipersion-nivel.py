import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO

# Datos
data_string = """ 
n,mes,y
1,2011-01,112
2,2011-02,118
3,2011-03,132
4,2011-04,129
5,2011-05,121
6,2011-06,135
7,2011-07,148
8,2011-08,148
9,2011-09,136
10,2011-10,119
11,2011-11,104
12,2011-12,118
13,2012-01,115
14,2012-02,126
15,2012-03,141
16,2012-04,135
17,2012-05,125
18,2012-06,149
19,2012-07,170
20,2012-08,170
21,2012-09,158
22,2012-10,133
23,2012-11,114
24,2012-12,140
25,2013-01,145
26,2013-02,150
27,2013-03,178
28,2013-04,163
29,2013-05,172
30,2013-06,178
31,2013-07,199
32,2013-08,199
33,2013-09,184
34,2013-10,162
35,2013-11,146
36,2013-12,166
37,2014-01,171
38,2014-02,180
39,2014-03,193
40,2014-04,181
41,2014-05,183
42,2014-06,218
43,2014-07,230
44,2014-08,242
45,2014-09,209
46,2014-10,191
47,2014-11,172
48,2014-12,194
49,2015-01,196
50,2015-02,196
51,2015-03,236
52,2015-04,235
53,2015-05,229
54,2015-06,243
55,2015-07,264
56,2015-08,272
57,2015-09,237
58,2015-10,211
59,2015-11,180
60,2015-12,201
61,2016-01,204
62,2016-02,188
63,2016-03,235
64,2016-04,227
65,2016-05,234
66,2016-06,264
67,2016-07,302
68,2016-08,293
69,2016-09,259
70,2016-10,229
71,2016-11,203
72,2016-12,229
73,2017-01,242
74,2017-02,233
75,2017-03,267
76,2017-04,269
77,2017-05,270
78,2017-06,315
79,2017-07,364
80,2017-08,347
81,2017-09,312
82,2017-10,274
83,2017-11,237
84,2017-12,278
85,2018-01,284
86,2018-02,277
87,2018-03,317
88,2018-04,313
89,2018-05,318
90,2018-06,374
91,2018-07,413
92,2018-08,405
93,2018-09,355
94,2018-10,306
95,2018-11,271
96,2018-12,306
97,2019-01,315
98,2019-02,301
99,2019-03,356
100,2019-04,348
101,2019-05,355
102,2019-06,422
103,2019-07,465
104,2019-08,467
105,2019-09,404
106,2019-10,347
107,2019-11,305
108,2019-12,336
109,2020-01,340
110,2020-02,318
111,2020-03,362
112,2020-04,348
113,2020-05,363
114,2020-06,435
115,2020-07,491
116,2020-08,505
117,2020-09,404
118,2020-10,359
119,2020-11,310
120,2020-12,337
121,2021-01,360
122,2021-02,342
123,2021-03,406
124,2021-04,396
125,2021-05,420
126,2021-06,472
127,2021-07,548
128,2021-08,559
129,2021-09,463
130,2021-10,407
131,2021-11,362
132,2021-12,405
133,2022-01,417
134,2022-02,391
135,2022-03,419
136,2022-04,461
137,2022-05,472
138,2022-06,535
139,2022-07,622
140,2022-08,606
141,2022-09,508
142,2022-10,461
143,2022-11,390
144,2022-12,432
"""

# Leer la cadena de datos en un DataFrame
data_df = pd.read_csv(StringIO(data_string), delimiter=',')

# Extraer el año de la columna 'mes'
data_df['Año'] = data_df['mes'].str.split('-').str[0].astype(int)

# Calcular la mediana y la dispersión intercuartílica por año
grouped_data = data_df.groupby(data_df['Año'])
medians = grouped_data['y'].median()
IQRs = grouped_data['y'].quantile(0.75) - grouped_data['y'].quantile(0.25)

# Tomar el logaritmo de los valores
log_medians = np.log(medians)
log_IQRs = np.log(IQRs)

# Realizar el gráfico de dispersión y ajustar una línea de regresión lineal
plt.figure(figsize=(12, 6))
plt.scatter(log_medians, log_IQRs, color='blue', label='Datos')
plt.xlabel('Log de la Mediana')
plt.ylabel('Log de la Dispersión Intercuartílica')
plt.title('Gráfico de Dispersión vs Nivel')

# Ajustar una línea de regresión lineal y trazarla
m, b = np.polyfit(log_medians, log_IQRs, 1)
plt.plot(log_medians, m*log_medians + b, color='red', label=f'Regresión lineal (pendiente={m:.2f})')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


