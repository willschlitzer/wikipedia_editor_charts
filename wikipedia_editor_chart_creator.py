import matplotlib.pyplot as plt
import pandas as pd

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
    rank_labels.append(str(max_rank))
    min_rank += iterator
    max_rank += iterator

rank_sum_df = pd.DataFrame(rank_sum_list, columns=['rank', 'edits'])
print(rank_sum_df)
#df['edits'].plot(kind='hist', cumulative=True, normed=True, bins=100)

def line_plot_edit_distro(df):
    df.plot(x='rev_rank', y='edits', grid=True)
    plt.show()

def pie_chart_edit_distro(df):
    df.plot(y='edits', grid=True, kind='pie', legend='True', labels=rank_labels)
    plt.show()

#line_plot_edit_distro((df))
#pie_chart_edit_distro(rank_sum_df)
