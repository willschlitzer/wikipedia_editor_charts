import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np

date = "3jul19"
if not os.path.isdir(date):
    os.mkdir(date)

file = "top1000_info_rem.csv"

df = pd.read_csv(file)
#print(max(df['rank']))
data_rank_max = max(df['rank'])
df['rev_rank'] = abs(df['rank'] - (data_rank_max + 1))
min_rank = 1
max_rank = 100
iterator = 100
rank_sum_list = []
rank_labels = []
while min_rank < data_rank_max:
    min_df = df[df['rank'] >= min_rank]
    filter_df = min_df[min_df['rank'] <= max_rank]
    rank_block_sum = sum(filter_df['edits'])
    rank_sum_list.append([max_rank, rank_block_sum])
    rank_labels.append(str(min_rank) + " - " + str(max_rank))
    min_rank += iterator
    max_rank += iterator

rank_sum_df = pd.DataFrame(rank_sum_list, columns=['rank', 'edits'])
print(rank_sum_df)
#df['edits'].plot(kind='hist', cumulative=True, normed=True, bins=100)

def line_plot_edit_distro(df, date):
    df.plot(x='rev_rank', y='edits', grid=True)
    plt.show()

def pie_chart_edit_distro(df, date):
    df.plot(y='edits', grid=True, kind='pie', legend='True', labels=rank_labels)
    file_save = date + "/pie_chart_" + date + ".png"
    plt.savefig(file_save)

def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d})".format(pct, absolute)

def pct_pie_chart(rank_sum_df):
    data = rank_sum_df['edits']
    wedges, texts, autotexts = plt.pie(data, autopct=lambda pct: func(pct, data),
                                      textprops=dict(color="w"))
    #plt.legend(wedges, title="Ingredients", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    #plt.setup(autotexts, size=8, weight="bold")

    #plt.set_title("Matplotlib bakery: A pie")

    plt.show()



#line_plot_edit_distro((df))
#pie_chart_edit_distro(rank_sum_df, date)
pct_pie_chart(rank_sum_df)