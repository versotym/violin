import numpy as np
import json
from sklearn.neighbors.kde import KernelDensity


class Violin:

    def __init__(self, center='median',
                 box=(25, 75), whiskers=(5, 95)):
        self.center = center
        self.box = box
        self.whiskers = whiskers
        self.series = []
        self.seriesId = 0

    def addSeries(self, data, name=None):
        if name:
            self.seriesName = name
        else:
            self.seriesName = str(self.seriesId)
        self.np = np.array(data)
        self.series.extend((self._density(), self._whiskers(),
                            self._box(), self._center()))
        self.seriesId += 1

    def _center(self):
        if self.center == 'median':
            c = np.median(self.np)
        elif self.center == 'mean':
            c = np.mean(self.np)
        return {
            'linkedTo': str(self.seriesId),
            'type': 'scatter',
            'name': self.center,
            'marker': {
                'symbol': 'circle'

            },
            'color': 'white',
            'data': [{'x': c, 'y': self.seriesId, 'name': self.center}]
        }

    def _box(self):
        b = (np.percentile(self.np, self.box[0]),
             np.percentile(self.np, self.box[1]))
        return {
            'linkedTo': str(self.seriesId),
            'type': 'line',
            'name': 'box',
            'marker': {
                'symbol': 'circle',
                'enabled': False
            },
            'lineWidth': 8,
            'color': 'black',
            'data': [{'x': b[0], 'y': self.seriesId,
                      'name': 'percentile ' + str(self.box[0])},
                     {'x': b[1], 'y': self.seriesId,
                      'name': 'percentile ' + str(self.box[1])}]
        }

    def _whiskers(self):
        w = (np.percentile(self.np, self.whiskers[0]),
             np.percentile(self.np, self.whiskers[1]))
        return {
            'linkedTo': str(self.seriesId),
            'type': 'line',
            'name': 'whiskers',
            'marker': {
                'symbol': 'circle',
                'enabled': False
            },
            'lineWidth': 2,
            'color': 'black',
            'data': [{'x': w[0], 'y': self.seriesId,
                      'name': 'percentile ' + str(self.whiskers[0])},
                     {'x': w[1], 'y': self.seriesId,
                      'name': 'percentile ' + str(self.whiskers[1])}]
        }

    def _density(self):
        d = list()
        h = dict()
        bw = self.np.size ** (-1./5)
        kd = KernelDensity(kernel='gaussian',
                           bandwidth=bw).fit(self.np.reshape(-1, 1))
        kd_vals = np.exp(kd.score_samples(self.np.reshape(-1, 1)))

        for i, x in enumerate(kd_vals):
            h[self.np[i]] = x
        for x in sorted(h):
            dp = h[x] * (0.4 / max(kd_vals))
            d.append([x, self.seriesId - dp, self.seriesId + dp])
        return {
            'id': str(self.seriesId),
            'name': self.seriesName,
            'type': 'areasplinerange',
            'enableMouseTracking': False,
            'marker': {
                'symbol': 'circle',
                'enabled': False
            },
            'color': 'Highcharts.getOptions().colors[' +
                     str(self.seriesId) + ']',
            'data': d
        }

    def series_list(self):
        return self.series
        
    def series_json(self):
        return json.dumps(self.series)