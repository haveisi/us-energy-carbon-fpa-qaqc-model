from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Project root
project_root = Path(__file__).resolve().parent.parent

# Input and output paths
portfolio_path = project_root / "data_processed" / "portfolio_electricity_costs.csv"
output_chart = project_root / "outputs" / "top_sites_total_climate_cost_mid.png"

# Load data
df = pd.read_csv(portfolio_path)

print("\nAVAILABLE COLUMNS:")
print(df.columns.tolist())

# Choose plotting metric
if "total_climate_cost_mid_$" in df.columns:
    metric_col = "total_climate_cost_mid_$"
    chart_title = "Total Climate-Adjusted Cost by Site (Mid Carbon Scenario)"
    x_label = "Total Climate-Adjusted Cost ($)"
elif "annual_electricity_cost_$" in df.columns and "carbon_cost_mid_$" in df.columns:
    df["total_climate_cost_mid_$"] = df["annual_electricity_cost_$"] + df["carbon_cost_mid_$"]
    metric_col = "total_climate_cost_mid_$"
    chart_title = "Total Climate-Adjusted Cost by Site (Mid Carbon Scenario)"
    x_label = "Total Climate-Adjusted Cost ($)"
elif "annual_electricity_cost_$" in df.columns:
    metric_col = "annual_electricity_cost_$"
    chart_title = "Annual Electricity Cost by Site"
    x_label = "Annual Electricity Cost ($)"
else:
    raise ValueError(
        "No usable cost column found. Expected one of: "
        "'total_climate_cost_mid_$', 'annual_electricity_cost_$', 'carbon_cost_mid_$'."
    )

# Validate required columns
required_cols = ["site_id", metric_col]
missing_cols = [c for c in required_cols if c not in df.columns]
if missing_cols:
    raise ValueError(f"Missing required columns for plotting: {missing_cols}")

# Prepare chart data
chart_df = df[["site_id", metric_col]].dropna().copy()

if chart_df.empty:
    raise ValueError("Chart dataset is empty after dropping missing values.")

chart_df = chart_df.sort_values(metric_col, ascending=True)

print("\nCHART DATA:")
print(chart_df)

# Create chart
plt.figure(figsize=(10, 6))
bars = plt.barh(chart_df["site_id"], chart_df[metric_col])

plt.title(chart_title)
plt.xlabel(x_label)
plt.ylabel("Site")

# Add labels
for bar in bars:
    width = bar.get_width()
    plt.text(
        width,
        bar.get_y() + bar.get_height() / 2,
        f" ${width:,.0f}",
        va="center"
    )

plt.tight_layout()
output_chart.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_chart, dpi=300, bbox_inches="tight")
plt.show()

print(f"\nChart saved to: {output_chart}")