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
dataset_3 = dataset_1 + dataset_2

'''
Add them to Violin series
'''
chart = Violin(center='mean')
chart.addSeries(dataset_1, name=dataset_names[0])
chart.addSeries(dataset_2, name=dataset_names[1])
chart.addSeries(dataset_3, name=dataset_names[2])

'''
Plot horizontal chart to file <horizontal.html>
'''
hc = Highchart()
hc.set_options('yAxis', {'categories': dataset_names, 'min': 0,
                         'max': len(dataset_names)-1, 'title': {'text': ''},
                         'gridLineWidth': 0})
hc.set_options('title', {'text': 'example'})
for s in chart.series_list():
    s['supress_errors'] = True   # otherwise setting attr 'linkTo' raise error
    hc.add_data_set(**s)
hc.save_file(filename='example_horizontal')

'''
Plot vertical chart to file <vertical.html>
'''
hc = Highchart()
hc.set_options('chart', {'inverted': True})
hc.set_options('xAxis', {'reversed': False})
hc.set_options('yAxis', {'categories': dataset_names, 'min': 0,
                         'max': len(dataset_names)-1, 'title': {'text': ''},
                         'gridLineWidth': 0})
hc.set_options('title', {'text': 'example'})
hc.set_options('tooltip', {'pointFormat': '<b>{point.name}</b>: {point.x}',
                           'headerFormat': ''})
for s in chart.series_list():
    s['supress_errors'] = True   # otherwise setting attr 'linkTo' raise error
    hc.add_data_set(**s)
hc.save_file(filename='example_vertical')
