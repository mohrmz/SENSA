"""
SENSA: Software Entity Name Suggestion Apparatus

This module contains method to visualize the results of SENSA-1


"""
__author__ = 'Mohammad Ramezani'
__version__ = '1.0'

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

dir = r'D:/Users/Ramezani/OneDrive/'


def change_width(g, new_value):
    for ax in g.axes.ravel():
        print(ax)
        current_width = ax.patch.get_width()
        diff = current_width - new_value

        # we change the bar width
        ax.patch.set_width(new_value)

        # we recenter the bar
        ax.patch.set_x(ax.patch.get_x() + diff * .5)


def change_width2(g, new_value):
    locs = g.ax.get_xticks()
    for i, patch in enumerate(g.ax.patches):
        current_width = patch.get_width()
        diff = current_width - new_value

        # we change the bar width
        patch.set_width(new_value)

        # we recenter the bar
        patch.set_x(locs[i // 4] - (new_value * .5))


def plot_accessor_mutators_frequency():
    df = pd.read_excel(dir + 'accessor_mutator_methods.xlsx', index_col=False)
    df1 = pd.melt(df, id_vars=['Method type', 'TrainPercent', 'TestPercent'], var_name='Dataset',
                  value_name='Number of methods', )

    print(df1)
    # quit()
    g = sns.catplot(data=df1,
                    x='Method type', y='Number of methods',
                    # hue='',
                    col='Dataset',
                    kind='bar',
                    height=3, aspect=1.20, dodge=False,
                    sharex=True, sharey=False,

                    # facet_kws={'width':.3},
                    # kwargs = {'width': .3}
                    )
    change_width(g, 0.2)
    plt.tight_layout()
    plt.show()


def plot_sensa_pefromance_changes():
    df = pd.read_excel(dir + 'evaluation_sensa1.xlsx', index_col=False)
    df1 = df.melt(id_vars=['Model', 'Method filter'], var_name='Metric', value_name='Value', )

    print(df1)
    # quit()
    g = sns.catplot(data=df1,
                    x='Model', y='Value',
                    hue='Method filter',
                    col='Metric', col_wrap=4,
                    kind='bar',
                    height=3, aspect=0.70,
                    # dodge=False,

                    )
    # change_width(g, .30)
    plt.tight_layout()
    plt.show()


def plot_samples_histogram():
    df_path = r'D:/Users/Ramezani/OneDrive/'
    df_name = 'SENSA_charts.xlsx'
    df = pd.read_excel(df_path + df_name, sheet_name='manual-evaluation-samples')
    df['All methods'] = df['All methods'] / df['All methods'].sum()
    df['Methods selected for manual evaluation'] = df['Methods selected for manual evaluation'] / df[
        'Methods selected for manual evaluation'].sum()

    df2 = pd.melt(df,
                  # id_vars=['Project ID'],
                  var_name=['Test set'],
                  value_vars=['All methods', 'Methods selected for manual evaluation'],
                  value_name='Number of methods',
                  )

    print(df2)

    g = sns.displot(df2, x='Number of methods',
                    hue='Test set',
                    # hue_order=['All methods', 'Methods selected for manual evaluation'],
                    bins=31,
                    kind='hist',
                    # kind='ecdf',
                    kde=True,
                    # bins=[1, 2, 3, 4, 5,6,7],
                    # ax=ax
                    # legend=False,
                    # rug=True,
                    # log_scale=True
                    )
    # g.ax.legend(loc=5)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    # plot_sensa_pefromance_changes()
    # plot_accessor_mutators_frequency()
    plot_samples_histogram()
