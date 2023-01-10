import matplotlib.pyplot as plt

xLIMIT = lambda x: x + (100 - x % 100)


def plot(reqs: list, time: int, head: int, algo: str, dsize: int = None) -> None:
    temp = [head] + reqs
    temp.reverse()

    # Upper limit for x-axis
    xlim = (xLIMIT(max(reqs)) - 1) if dsize is None else (dsize - 1)

    # Plot stylesheet
    plt.style.use('./diskUtil/styles/diskplot.mplstyle')

    # Axes limits and ticks
    plt.ylim(0, len(reqs))
    plt.yticks([])

    plt.xlim(0, xlim)
    plt.xticks([0, xlim] + temp)

    y = [i for i in range(len(temp))]

    plt.vlines(
        temp, y, len(temp),
        linestyle='dashed',
        colors='red'
    )

    plt.plot(
        temp, y,
        color='#088F8F',
        marker='o',
        clip_on=False,
        linewidth=2
    )

    # Algo name and seek time in plot
    plt.title(f'{algo} Disk Scheduling Algorithm', pad=15)
    plt.annotate(
        f'Seek Time = {time}',
        xy=(1.0, -0.2),
        xycoords='axes fraction',
        ha='right',
        va='center'
    )

    plt.show()
