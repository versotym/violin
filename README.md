# violin
> A simple workaround to produce violin plot with [highcharts.js](http://www.highcharts.js)

## Examples
Plotting random data with example.py    
  
```python
from violin import Violin
from highcharts import Highchart
import random
import numpy as np

'''
Create 3 random datasets
'''
dataset_names = ['dataset1', 'dataset2', 'dataset3']
dataset_1 = np.random.normal(0, 1, size=100).tolist()
dataset_2 = np.random.normal(3, 1, size=100).tolist()
dataset_3 = data1 + data2

'''
Add them to Violin series
'''
chart = Violin(center='mean')
chart.addSeries(dataset_1, name=names[0])
chart.addSeries(dataset_2, name=names[1])
chart.addSeries(dataset_3, name=names[2])

'''
Plot horizontal chart to file <horizontal.html>
'''
hc = Highchart()
hc.set_options('yAxis', {'categories': names, 'min': 0,
                         'max': len(names)-1, 'title': {'text': ''},
                         'gridLineWidth': 0})
hc.set_options('title', {'text': 'example'})
for s in chart.series:
    s['supress_errors'] = True   # otherwise setting attr 'linkTo' raise error
    hc.add_data_set(**s)
hc.save_file(filename='horizontal')
```  
![example1](img/example1.png)

```python
'''
Plot vertical chart to file <vertical.html>
'''
hc = Highchart()
hc.set_options('chart', {'inverted': True})
hc.set_options('xAxis', {'reversed': False})
hc.set_options('yAxis', {'categories': names, 'min': 0,
                         'max': len(names)-1, 'title': {'text': ''},
                         'gridLineWidth': 0})
hc.set_options('title', {'text': 'example'})
for s in chart.series:
    s['supress_errors'] = True   # otherwise setting attr 'linkTo' raise error
    hc.add_data_set(**s)
hc.save_file(filename='vertical')
```  
![example2](img/example2.png)
