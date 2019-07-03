import matplotlib.pyplot as plt
from matplotlib import cm
import pandas as pd
import os
import numpy as np
from random import shuffle

date = "3jul19"
cao = "July 3, 2019"
if not os.path.isdir(date):
    os.mkdir(date)

file = "top10000_info_rem.csv"
total_edits = 899904244

df = pd.read_csv(file)
data_rank_max = max(df['rank'])
df['rev_rank'] = abs(df['rank'] - (data_rank_max + 1))
non_10000_edits = total_edits - sum(df['edits'])
min_rank = 1
max_rank = 1000
iterator = 1000
rank_sum_list = []
rank_labels = []
while min_rank < data_rank_max:
    min_df = df[df['rank'] >= min_rank]
    filter_df = min_df[min_df['rank'] <= max_rank]
    rank_block_sum = sum(filter_df['edits'])
    rank_sum_list.append(rank_block_sum)
    rank_labels.append("Editors " + str(min_rank) + " - " + str(max_rank))
    min_rank += iterator
    max_rank += iterator
all_edit_sum_list = rank_sum_list[:]
all_edit_sum_list.append(non_10000_edits)
all_edit_labels = rank_labels[:]
all_edit_labels.append('The rest of Wikipedia')
#rank_sum_df = pd.DataFrame(rank_sum_list, columns=['rank', 'edits'])
#print(rank_sum_df)
#df['edits'].plot(kind='hist', cumulative=True, normed=True, bins=100)

def line_plot_edit_distro(df, date):
    df.plot(x='rev_rank', y='edits', grid=True)
    file_save = date + "/line_chart_" + date + ".png"
    plt.savefig(file_save)

def pie_chart_edit_distro(df, date):
    df.plot(y='edits', grid=True, kind='pie', legend='True', labels=rank_labels)
    file_save = date + "/pie_chart_" + date + ".png"
    plt.savefig(file_save)

def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    abs_string = str(absolute)
    #return "{:.1f}%\n({:n})".format(pct, absolute)
    return "{:.1f}%".format(pct)

def pct_pie_chart(data, labels, title, cao, chart_type):
    #data = rank_sum_df['edits']
    plt.figure(figsize=(10, 10))
    #theme = plt.get_cmap('jet')
    slices = range(1, len(data) + 1)
    cmap = cm.Paired
    colors = cmap(np.linspace(0., 1, len(slices)))
    wedges, texts, autotexts = plt.pie(data, counterclock=False, autopct=lambda pct: func(pct, data), colors=colors)

    plt.legend(labels,loc=1, title="Editors")

    plt.setp(autotexts, size=7, weight="bold")

    plt.title(title, size=20)
    plt.text(.8, -1, "Current as of " + cao, style='italic',)

    file_save = date + "/" + chart_type + "_" + date + ".png"
    plt.savefig(file_save)
    #plt.show()


#line_plot_edit_distro(df, date)
#pie_chart_edit_distro(rank_sum_df, date)
pct_pie_chart(rank_sum_list, rank_labels, title="The Top 10,000 Editors", cao=cao, chart_type = "top1000_pie")
pct_pie_chart(all_edit_sum_list, all_edit_labels, title="The Top 10,000 Editors and the rest of English Wikipedia", cao=cao, chart_type = "all_pie")