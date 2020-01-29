from matplotlib import pyplot as plt
import numpy as np

def get_min_max(df, col):
    assert col in df.columns, f'{col} not found in dataframe columns'
    return df[col].values.min(), df[col].values.max()

def plot_fea_hists(dfs, names, col, ax):
    if names is not None:
        assert len(dfs) == len(names), 'len of DataFrames not euqal to len of names'
    min_val, max_val = np.inf, -np.inf
    for df in dfs:
        curr_min_val, curr_max_val = get_min_max(df, col)
        min_val = min(min_val, curr_min_val)
        max_val = max(max_val, curr_max_val)
    for i, df in enumerate(dfs):
        name = names[i] if names is not None else None
        df[col].hist(ax=ax, bins=np.linspace(min_val, max_val, 20), label=name)
    if names is not None:
        ax.legend()
    ax.set_title(f'{col}')
    ax.set_yscale('log')
    if max_val > 100:
        ax.set_xscale('log')


def plot_df_feas_hists(*dfs, names=None, cols=None, num_col=4):
    """
    list of name and df pairs
    """
    num_row = int(len(cols) / num_col)
    if (num_row * num_col) < len(cols):
        num_row += 1
    ax_height = 60 / 18
    fig, axes = plt.subplots(num_row, num_col)
    plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)
    axes = axes.flatten()
    fig.set_size_inches(20, round(ax_height * num_row))
    for i, col in enumerate(cols):
        plot_fea_hists(dfs, names, cols[i], axes[i])
    plt.show()
