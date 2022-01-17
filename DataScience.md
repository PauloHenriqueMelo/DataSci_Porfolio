```python
pip install tensorflow
```

```python
import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
```


```python
df= pd.read_csv('boko.csv',delimiter=";",decimal='.')
```


```python
df['hemoglobina'] = [x.replace(',', '.') for x in df['hemoglobina']]
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>hemoglobina</th>
      <th>Vitamina D</th>
      <th>Desfecho</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8</td>
      <td>31</td>
      <td>Óbito após 48hs de internação</td>
    </tr>
    <tr>
      <th>1</th>
      <td>7</td>
      <td>31</td>
      <td>Óbito após 48hs de internação</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8.2</td>
      <td>31</td>
      <td>Óbito após 48hs de internação</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6.5</td>
      <td>31</td>
      <td>Óbito após 48hs de internação</td>
    </tr>
    <tr>
      <th>4</th>
      <td>7.1</td>
      <td>31</td>
      <td>Óbito após 48hs de internação</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>380</th>
      <td>7.5</td>
      <td>26</td>
      <td>Alta médica curado</td>
    </tr>
    <tr>
      <th>381</th>
      <td>7.5</td>
      <td>26</td>
      <td>Alta médica curado</td>
    </tr>
    <tr>
      <th>382</th>
      <td>7.5</td>
      <td>27</td>
      <td>Alta médica curado</td>
    </tr>
    <tr>
      <th>383</th>
      <td>7.5</td>
      <td>31</td>
      <td>Alta médica curado</td>
    </tr>
    <tr>
      <th>384</th>
      <td>5.3</td>
      <td>80</td>
      <td>Óbito  nas primeiras 48hs</td>
    </tr>
  </tbody>
</table>
<p>385 rows × 3 columns</p>
</div>




```python
df['hemoglobina'] = df['hemoglobina'].astype(float)
```


```python
df['VitaminaD'] = df['Vitamina D'].astype(float)
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>hemoglobina</th>
      <th>Vitamina D</th>
      <th>Desfecho</th>
      <th>VitaminaD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8.0</td>
      <td>31.0</td>
      <td>Óbito após 48hs de internação</td>
      <td>31.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>7.0</td>
      <td>31.0</td>
      <td>Óbito após 48hs de internação</td>
      <td>31.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8.2</td>
      <td>31.0</td>
      <td>Óbito após 48hs de internação</td>
      <td>31.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6.5</td>
      <td>31.0</td>
      <td>Óbito após 48hs de internação</td>
      <td>31.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>7.1</td>
      <td>31.0</td>
      <td>Óbito após 48hs de internação</td>
      <td>31.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>380</th>
      <td>7.5</td>
      <td>26.0</td>
      <td>Alta médica curado</td>
      <td>26.0</td>
    </tr>
    <tr>
      <th>381</th>
      <td>7.5</td>
      <td>26.0</td>
      <td>Alta médica curado</td>
      <td>26.0</td>
    </tr>
    <tr>
      <th>382</th>
      <td>7.5</td>
      <td>27.0</td>
      <td>Alta médica curado</td>
      <td>27.0</td>
    </tr>
    <tr>
      <th>383</th>
      <td>7.5</td>
      <td>31.0</td>
      <td>Alta médica curado</td>
      <td>31.0</td>
    </tr>
    <tr>
      <th>384</th>
      <td>5.3</td>
      <td>80.0</td>
      <td>Óbito  nas primeiras 48hs</td>
      <td>80.0</td>
    </tr>
  </tbody>
</table>
<p>385 rows × 4 columns</p>
</div>




```python
sns.scatterplot(x="hemoglobina", y="Vitamina D", hue="Desfecho", data=df)
```




    <AxesSubplot:xlabel='hemoglobina', ylabel='Vitamina D'>




    
![png](output_8_1.png)
    



```python
df_grouped = df.groupby(["hemoglobina", "VitaminaD", "Desfecho"])

df_grouped.count()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th></th>
      <th>Vitamina D</th>
    </tr>
    <tr>
      <th>hemoglobina</th>
      <th>VitaminaD</th>
      <th>Desfecho</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">3.9</th>
      <th>21.0</th>
      <th>Alta médica curado</th>
      <td>1</td>
    </tr>
    <tr>
      <th>32.0</th>
      <th>Alta médica curado</th>
      <td>1</td>
    </tr>
    <tr>
      <th>34.0</th>
      <th>Alta médica curado</th>
      <td>1</td>
    </tr>
    <tr>
      <th>73.0</th>
      <th>Alta médica curado</th>
      <td>1</td>
    </tr>
    <tr>
      <th>79.0</th>
      <th>Alta médica curado</th>
      <td>1</td>
    </tr>
    <tr>
      <th>...</th>
      <th>...</th>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>8.9</th>
      <th>31.0</th>
      <th>Óbito após 48hs de internação</th>
      <td>1</td>
    </tr>
    <tr>
      <th>9.6</th>
      <th>15.0</th>
      <th>Alta médica curado</th>
      <td>1</td>
    </tr>
    <tr>
      <th>10.0</th>
      <th>13.0</th>
      <th>Alta médica curado</th>
      <td>1</td>
    </tr>
    <tr>
      <th>10.2</th>
      <th>13.0</th>
      <th>Alta médica curado</th>
      <td>1</td>
    </tr>
    <tr>
      <th>10.3</th>
      <th>29.0</th>
      <th>Óbito após 48hs de internação</th>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>269 rows × 1 columns</p>
</div>




```python

```

    <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001B37838F850>
    


```python

```
