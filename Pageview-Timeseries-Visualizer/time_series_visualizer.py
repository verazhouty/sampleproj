import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates = ["date"], index_col = "date")

# Clean data
#Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
df=df.drop(df[(df['value']<df['value'].quantile(0.025)) | (df['value']>df['value'].quantile(0.975))].index)

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15, 10))
    ax.plot(df.index, df['value'], color='red')
    ax.set(
        xlabel="Date",
        ylabel="Page Views",
        title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019"
    )
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Year'] = df_bar.index.year
    df_bar['Month'] = df_bar.index.month
    df_bar = df_bar.groupby(["Year", "Month"])["value"].mean()
    df_bar = df_bar.unstack()
    # Draw bar plot
    fig = df_bar.plot(kind= 'bar', figsize = (15,10)).figure
    plt.title('')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    lg = plt.legend(title= 'Months', fontsize = 15, labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
             'August', 'September', 'October', 'November', 'December'])
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10)) #set para
    ax1 = sns.boxplot(x=df_box["year"], y=df_box["value"], ax=ax1)
    ax1.set(
        xlabel="Years",
        ylabel="Page Views",
        title="Year-wise Box Plot (Trend)"
    )
    ax2 = sns.boxplot(x=df_box["month"], y=df_box["value"], ax=ax2)
    ax2.set(
        xlabel="Month",
        ylabel="Page Views",
        title="Month-wise Box Plot (Seasonality)"
    )
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
