"""
Main cli or app entry point
"""

from mylib.lib import (
    load_dataset,
    bar_visual,
    hist_visual,
)


def g_describe():
    g = load_dataset()
    return g.describe()


def general_viz_combined(general_df, jupyter_render):
    """saves all the figures at once"""
    bar_visual(general_df, "incidents_85_99", jupyter_render)
    hist_visual(general_df, "incidents_85_99", jupyter_render)
    bar_visual(general_df, "fatal_accidents_85_99", jupyter_render)
    hist_visual(general_df, "fatal_accidents_85_99", jupyter_render)
    bar_visual(general_df, "fatalities_85_99", jupyter_render)
    hist_visual(general_df, "fatalities_85_99", jupyter_render)
    bar_visual(general_df, "incidents_00_14", jupyter_render)
    hist_visual(general_df, "incidents_00_14", jupyter_render)
    bar_visual(general_df, "fatal_accidents_00_14", jupyter_render)
    hist_visual(general_df, "fatal_accidents_00_14", jupyter_render)
    bar_visual(general_df, "fatalities_00_14", jupyter_render)
    hist_visual(general_df, "fatalities_00_14", jupyter_render)


def save_to_md():
    """save to markdown"""
    df = load_dataset()
    general_viz_combined(df, False)
    markdown_table = g_describe().to_markdown()
    with open("report.md", "w", encoding="utf-8") as file:
        file.write("# Report\n\n")
        file.write("## Statistics\n\n")
        file.write(f"{markdown_table}\n\n")
        file.write("## Visualizations\n\n")
        file.write("### Incidents 85-99\n\n")
        file.write(
            "![Incidents 85-99](incidents_85_99_over_Airlines.png)\n\n"
        )
        file.write("![Incidents 85-99](Frequency_of_incidents_85_99_histogram.png)\n\n")
        file.write("### Fatal Accidents 85-99\n\n")
        file.write(
            "![Fatal Accidents 85-99](fatal_accidents_85_99_over_Airlines.png)\n\n"
        )
        file.write(
            "![Fatal Accidents 85-99](Frequency_of_fatal_accidents_85_99_histogram.png)\n\n"
        )
        file.write("### Fatalities 85-99\n\n")
        file.write("![Fatalities 85-99](fatalities_85_99_over_Airlines.png)\n\n")
        file.write(
            "![Fatalities 85-99](Frequency_of_fatalities_85_99_histogram.png)\n\n"
        )
        file.write("### Incidents 00-14\n\n")
        file.write(
            "![Incidents 00-14](incidents_00_14_over_Airlines.png)\n\n"
        )
        file.write("![Incidents 00-14](Frequency_of_incidents_00_14_histogram.png)\n\n")
        file.write("### Fatal Accidents 00-14\n\n")
        file.write(
            "![Fatal Accidents 00-14](fatal_accidents_00_14_over_Airlines.png)\n\n"
        )
        file.write(
            "![Fatal Accidents 00-14](Frequency_of_fatal_accidents_00_14_histogram.png)\n\n"
        )
        file.write("### Fatalities 00-14\n\n")
        file.write("![Fatalities 00-14](fatalities_00_14_over_Airlines.png)\n\n")
        file.write(
            "![Fatalities 00-14](Frequency_of_fatalities_00_14_histogram.png)\n\n"
        )


# if __name__ == "__main__":
#     save_to_md()
#     print(g_describe())
