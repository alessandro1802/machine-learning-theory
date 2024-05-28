from glob import glob
from os.path import join
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def read_metrics(path: str) -> pd.DataFrame:
    df = pd.DataFrame()
    for set_type_path in glob(join(path, '*')):
        set_type = set_type_path.split('/')[-1]
        for file_path in glob(join(set_type_path, '*.csv')):
            parameter = file_path.split('/')[-1].split('.')[0]
            metric = pd.read_csv(file_path, header=None)
            metric.rename(columns={0: "epoch", 2: "metric"}, inplace=True)
            metric["epoch"] = metric["epoch"].astype(int) + 1
            metric["parameter"], metric["set_type"] = parameter, set_type
            df = pd.concat([df, metric[["parameter", "set_type", "epoch", "metric"]]])
    return df

def plot_metric(df: pd.DataFrame, title: str, save_path: str) -> None:
    fig = plt.figure(figsize=(16, 9))
    sns.set_style("darkgrid")
    sns.lineplot(df, x="epoch", y="metric", hue="parameter")
    fig.suptitle(title, fontsize=20)
    plt.savefig(save_path)

def plot_metrics(df: pd.DataFrame, title: str, save_path: str) -> None:
    subplots = pd.unique(df["set_type"])
    fig, axes = plt.subplots(1, len(subplots), figsize=(16, 9), sharey=True)
    sns.set_style("darkgrid")
    for i, ax in enumerate(axes.flat):
        sns.lineplot(df[df["set_type"] == subplots[i]], x="epoch", y="metric", hue="parameter", ax=ax)
        ax.set_title(subplots[i], fontsize=14)
    fig.suptitle(title, fontsize=20)
    plt.savefig(save_path)


if __name__ == '__main__':
    metrics_path = "./metrics"
    accuracy = read_metrics(join(metrics_path, "acc"))
    loss = read_metrics(join(metrics_path, "loss"))

    plots_path = "./plots"
    plot_metric(accuracy, "Test accuracy", join(plots_path, "test_acc.jpeg"))
    plot_metrics(loss, "Losses", join(plots_path, "losses.jpeg"))
