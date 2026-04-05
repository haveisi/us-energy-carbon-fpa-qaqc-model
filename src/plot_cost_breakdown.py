from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# =========================================
# Paths
# =========================================
project_root = Path(__file__).resolve().parent.parent
portfolio_path = project_root / "data_processed" / "portfolio_electricity_costs.csv"
output_chart = project_root / "outputs" / "cost_breakdown_stacked.png"

# =========================================
# Load data
# =========================================
df = pd.read_csv(portfolio_path)

print("\nAVAILABLE COLUMNS:")
print(df.columns.tolist())

required_cols = ["site_id", "annual_electricity_cost_$", "carbon_cost_mid_$"]
missing = [c for c in required_cols if c not in df.columns]

if missing:
    raise ValueError(f"Missing required columns: {missing}")

chart_df = df[required_cols].dropna().copy()

if chart_df.empty:
    raise ValueError("No valid data after cleaning.")

chart_df = chart_df.sort_values("annual_electricity_cost_$", ascending=True)

print("\nCHART DATA:")
print(chart_df)

# =========================================
# Plot stacked bar chart
# =========================================
plt.figure(figsize=(10, 6))

plt.barh(
    chart_df["site_id"],
    chart_df["annual_electricity_cost_$"],
    label="Electricity Cost"
)

plt.barh(
    chart_df["site_id"],
    chart_df["carbon_cost_mid_$"],
    left=chart_df["annual_electricity_cost_$"],
    label="Carbon Cost (Mid Scenario)"
)

# Total labels at end of bars
for i, row in enumerate(chart_df.itertuples(index=False)):
    total = row[1] + row[2]
    plt.text(total, i, f" ${total:,.0f}", va="center")

plt.title("Electricity vs Carbon Cost by Site")
plt.xlabel("Total Cost ($)")
plt.ylabel("Site")
plt.legend()

output_chart.parent.mkdir(parents=True, exist_ok=True)
plt.tight_layout()
plt.savefig(output_chart, dpi=300, bbox_inches="tight")
plt.show()

print(f"\nChart saved to: {output_chart}")