import plotly
import plotly.graph_objs as go

fig = {
            'data': [{'labels': ['Residential', 'Non-Residential', 'Utility'],
                              'values': [19, 26, 55],
                                            'type': 'pie'}],
                'layout': {'title': 'Forcasted 2014 U.S. PV Installations by Market Segment'}
                     }
plotly.offline.plot(fig)
