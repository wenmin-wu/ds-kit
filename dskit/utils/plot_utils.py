import numpy as np
import pandas as pd
from typing import Tuple, List
from matplotlib import pyplot as plt


def get_min_max(df, col):
    assert col in df.columns, f"{col} not found in dataframe columns"
    return df[col].values.min(), df[col].values.max()


def plot_feat_hists(
    dfs: List[Tuple[str, pd.DataFrame]], col: str, ax, y_scale=None
):
    min_val, max_val = np.inf, -np.inf
    for (name, df) in dfs:
        cur_min_val, cur_max_val = get_min_max(df, col)
        min_val = min(min_val, cur_min_val)
        max_val = max(max_val, cur_max_val)
    for (name, df) in dfs:
        df[col].hist(ax=ax, bins=np.linspace(min_val, max_val, 20), label=name)
    ax.legend()
    ax.set_title(f"{col}")
    if y_scale is not None:
        ax.set_yscale(y_scale)


def plot_df_feats_hists(
    dfs: List[Tuple[str, pd.DataFrame]],
    cols: List[str],
    num_col=4,
    y_scale=None,
):
    '''
    list of name and df pairs
    '''
    num_row = int(len(cols) / num_col)
    if (num_row * num_col) < len(cols):
        num_row += 1
    ax_height = 60 / 18
    fig, axes = plt.subplots(num_row, num_col)
    plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)
    axes = axes.flatten()
    fig.set_size_inches(20, round(ax_height * num_row))
    for i, col in enumerate(cols):
        plot_feat_hists(dfs, col, axes[i], y_scale)
    plt.show()
