```python
pip install tensorflow
```

    Collecting tensorflowNote: you may need to restart the kernel to use updated packages.
    
      Using cached tensorflow-2.7.0-cp38-cp38-win_amd64.whl (430.8 MB)
    Collecting absl-py>=0.4.0
      Using cached absl_py-1.0.0-py3-none-any.whl (126 kB)
    Requirement already satisfied: wheel<1.0,>=0.32.0 in c:\users\phmm2\anaconda4\lib\site-packages (from tensorflow) (0.36.2)
    Collecting tensorboard~=2.6
      Using cached tensorboard-2.7.0-py3-none-any.whl (5.8 MB)
    Collecting keras<2.8,>=2.7.0rc0
      Using cached keras-2.7.0-py2.py3-none-any.whl (1.3 MB)
    Collecting protobuf>=3.9.2
      Using cached protobuf-3.19.3-cp38-cp38-win_amd64.whl (895 kB)
    Collecting google-pasta>=0.1.1
      Using cached google_pasta-0.2.0-py3-none-any.whl (57 kB)
    Collecting gast<0.5.0,>=0.2.1
      Using cached gast-0.4.0-py3-none-any.whl (9.8 kB)
    Collecting flatbuffers<3.0,>=1.12
      Using cached flatbuffers-2.0-py2.py3-none-any.whl (26 kB)
    Requirement already satisfied: wrapt>=1.11.0 in c:\users\phmm2\anaconda4\lib\site-packages (from tensorflow) (1.12.1)
    Requirement already satisfied: six>=1.12.0 in c:\users\phmm2\anaconda4\lib\site-packages (from tensorflow) (1.15.0)
    Collecting grpcio<2.0,>=1.24.3
      Using cached grpcio-1.43.0-cp38-cp38-win_amd64.whl (3.4 MB)
    Requirement already satisfied: h5py>=2.9.0 in c:\users\phmm2\anaconda4\lib\site-packages (from tensorflow) (2.10.0)
    Collecting libclang>=9.0.1
      Using cached libclang-12.0.0-2-py2.py3-none-win_amd64.whl (13.0 MB)
    Collecting keras-preprocessing>=1.1.1
      Using cached Keras_Preprocessing-1.1.2-py2.py3-none-any.whl (42 kB)
    Collecting tensorflow-estimator<2.8,~=2.7.0rc0
      Using cached tensorflow_estimator-2.7.0-py2.py3-none-any.whl (463 kB)
    Collecting tensorflow-io-gcs-filesystem>=0.21.0
      Using cached tensorflow_io_gcs_filesystem-0.23.1-cp38-cp38-win_amd64.whl (1.5 MB)
    Collecting astunparse>=1.6.0
      Using cached astunparse-1.6.3-py2.py3-none-any.whl (12 kB)
    Requirement already satisfied: numpy>=1.14.5 in c:\users\phmm2\anaconda4\lib\site-packages (from tensorflow) (1.20.1)
    Requirement already satisfied: typing-extensions>=3.6.6 in c:\users\phmm2\anaconda4\lib\site-packages (from tensorflow) (3.7.4.3)
    Collecting termcolor>=1.1.0
      Using cached termcolor-1.1.0-py3-none-any.whl
    Collecting opt-einsum>=2.3.2
      Using cached opt_einsum-3.3.0-py3-none-any.whl (65 kB)
    Collecting tensorboard-plugin-wit>=1.6.0
      Using cached tensorboard_plugin_wit-1.8.1-py3-none-any.whl (781 kB)
    Requirement already satisfied: requests<3,>=2.21.0 in c:\users\phmm2\anaconda4\lib\site-packages (from tensorboard~=2.6->tensorflow) (2.25.1)
    Collecting tensorboard-data-server<0.7.0,>=0.6.0
      Using cached tensorboard_data_server-0.6.1-py3-none-any.whl (2.4 kB)
    Collecting markdown>=2.6.8
      Using cached Markdown-3.3.6-py3-none-any.whl (97 kB)
    Requirement already satisfied: werkzeug>=0.11.15 in c:\users\phmm2\anaconda4\lib\site-packages (from tensorboard~=2.6->tensorflow) (1.0.1)
    Collecting google-auth-oauthlib<0.5,>=0.4.1
      Using cached google_auth_oauthlib-0.4.6-py2.py3-none-any.whl (18 kB)
    Collecting google-auth<3,>=1.6.3
      Using cached google_auth-2.3.3-py2.py3-none-any.whl (155 kB)
    Requirement already satisfied: setuptools>=41.0.0 in c:\users\phmm2\anaconda4\lib\site-packages (from tensorboard~=2.6->tensorflow) (52.0.0.post20210125)
    Collecting pyasn1-modules>=0.2.1
      Using cached pyasn1_modules-0.2.8-py2.py3-none-any.whl (155 kB)
    Collecting cachetools<5.0,>=2.0.0
      Using cached cachetools-4.2.4-py3-none-any.whl (10 kB)
    Collecting rsa<5,>=3.1.4
      Using cached rsa-4.8-py3-none-any.whl (39 kB)
    Collecting requests-oauthlib>=0.7.0
      Using cached requests_oauthlib-1.3.0-py2.py3-none-any.whl (23 kB)
    Collecting importlib-metadata>=4.4
      Downloading importlib_metadata-4.10.1-py3-none-any.whl (17 kB)
    Requirement already satisfied: zipp>=0.5 in c:\users\phmm2\anaconda4\lib\site-packages (from importlib-metadata>=4.4->markdown>=2.6.8->tensorboard~=2.6->tensorflow) (3.4.1)
    Collecting pyasn1<0.5.0,>=0.4.6
      Using cached pyasn1-0.4.8-py2.py3-none-any.whl (77 kB)
    Requirement already satisfied: chardet<5,>=3.0.2 in c:\users\phmm2\anaconda4\lib\site-packages (from requests<3,>=2.21.0->tensorboard~=2.6->tensorflow) (4.0.0)
    Requirement already satisfied: certifi>=2017.4.17 in c:\users\phmm2\anaconda4\lib\site-packages (from requests<3,>=2.21.0->tensorboard~=2.6->tensorflow) (2020.12.5)
    Requirement already satisfied: idna<3,>=2.5 in c:\users\phmm2\anaconda4\lib\site-packages (from requests<3,>=2.21.0->tensorboard~=2.6->tensorflow) (2.10)
    Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\users\phmm2\anaconda4\lib\site-packages (from requests<3,>=2.21.0->tensorboard~=2.6->tensorflow) (1.26.4)
    Collecting oauthlib>=3.0.0
      Using cached oauthlib-3.1.1-py2.py3-none-any.whl (146 kB)
    Installing collected packages: pyasn1, rsa, pyasn1-modules, oauthlib, cachetools, requests-oauthlib, importlib-metadata, google-auth, tensorboard-plugin-wit, tensorboard-data-server, protobuf, markdown, grpcio, google-auth-oauthlib, absl-py, termcolor, tensorflow-io-gcs-filesystem, tensorflow-estimator, tensorboard, opt-einsum, libclang, keras-preprocessing, keras, google-pasta, gast, flatbuffers, astunparse, tensorflow
      Attempting uninstall: importlib-metadata
        Found existing installation: importlib-metadata 3.10.0
        Uninstalling importlib-metadata-3.10.0:
          Successfully uninstalled importlib-metadata-3.10.0
    Successfully installed absl-py-1.0.0 astunparse-1.6.3 cachetools-4.2.4 flatbuffers-2.0 gast-0.4.0 google-auth-2.3.3 google-auth-oauthlib-0.4.6 google-pasta-0.2.0 grpcio-1.43.0 importlib-metadata-4.10.1 keras-2.7.0 keras-preprocessing-1.1.2 libclang-12.0.0 markdown-3.3.6 oauthlib-3.1.1 opt-einsum-3.3.0 protobuf-3.19.3 pyasn1-0.4.8 pyasn1-modules-0.2.8 requests-oauthlib-1.3.0 rsa-4.8 tensorboard-2.7.0 tensorboard-data-server-0.6.1 tensorboard-plugin-wit-1.8.1 tensorflow-2.7.0 tensorflow-estimator-2.7.0 tensorflow-io-gcs-filesystem-0.23.1 termcolor-1.1.0
    


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
