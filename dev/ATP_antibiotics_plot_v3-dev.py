import plotly.graph_objects as go #lgtm [py/unused-import]
from plotly.subplots import make_subplots
import json
from itertools import chain#lgtm [py/unused-import]


def plot_data():

    #import data
    try:
        data = json.loads(open(r'C:\Users\carterc\OneDrive - Norwich BioScience Institutes\Python scripts\ATP_antibiotics_figure\ATP_literature_data.json').read())
    except IOError as ex:
        print(f"Could not find {ex.strerror}, please run ATP_antibiotics_figures_v3.py")

    #assign to groups
    with_cfu = [key for key, values in data.items() if 'ATP_per_CFU' in values.keys()] #lgtm [py/unused-local-variable]
    without_cfu = [key for key, values in data.items() if 'ATP_per_CFU' not in values.keys()] #lgtm [py/unused-local-variable]

    # (row, column)
    fig_subplots_specs = { #lgtm [py/unused-local-variable]
        0 : ((1,1), (2, 1)),
        1 : ((1,2), (2,2)),
        2 : ((4,1), (5,1)),
        3 : ((4,2), (5,2)),
        4 : ((7,1), (8,1)),
        5 : ((7,2), (8,2)),
        6 : ((10,1), (11,1)),
        7 : ((10, 2), (11, 2)),
        8 : (13, 1),
        9 : (13, 2),
        10 : (15, 1),
        11 : (15, 2),
        12 : (17, 1),
        13 : (17, 2)
    } 


    fig = make_subplots(
        rows=18, cols=2,
        specs=[
            [{}, {}],
            [{"rowspan" : 2}, {"rowspan" : 2}],
            [None, None],
            [{}, {}],
            [{"rowspan" : 2}, {"rowspan" : 2}],
            [None, None],
            [{}, {}],
            [{"rowspan" : 2}, {"rowspan" : 2}],
            [None, None],
            [{}, {}],
            [{"rowspan" : 2}, {"rowspan" : 2}],
            [None, None],
            [{"rowspan" : 2}, {"rowspan" : 2}],
            [None, None],
            [{"rowspan" : 2}, {"rowspan" : 2}],
            [None, None],
            [{"rowspan" : 2}, {"rowspan" : 2}],
            [None, None]
        ])

    fig.show()
    # for num, antibiotic in enumerate(chain(with_cfu, without_cfu)):

    #     print(num, antibiotic)
    #     for conc in data[antibiotic].keys():
        # fig.add_trace(go.Scatter)


if __name__ == "__main__":
    plot_data()