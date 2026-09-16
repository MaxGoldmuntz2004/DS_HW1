import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def main():
    print("Reading csv located at data/raw/coffee_sales.csv \n")

    BASE_DIR = Path(__file__).resolve().parent.parent
    data_path = BASE_DIR / "data" / "raw" / "coffee_sales.csv"

    df = pd.read_csv(data_path)
    df["revenue"] = df["quantity"] * df["unit_price"]
    daily = df.groupby("date")["revenue"].sum()

    print(f"Daily Average Revenue: \n "
          f"{daily} \n\n"
          f"Average Daily Revenue: \n "
          f"{daily.mean()}\n")

    shuffled = df.sample(frac=1, random_state=5110)
    half = len(shuffled) // 2
    group_a = shuffled.iloc[:half]
    group_b = shuffled.iloc[half:]

    print("Comparing Random 50/50 Split of Days:\n"
          f"Group A mean revenue: {group_a['revenue'].mean():.2f}\n"
          f"Group B mean revenue: {group_b['revenue'].mean():.2f}\n")

    by_product = df.groupby("product")["revenue"].sum()
    by_product.plot(kind="bar")
    plt.ylabel("Total revenue ($)")
    plt.title("Revenue by product")
    plt.savefig(BASE_DIR / "plots" / "revenue_by_product.png")
    print("Added Revenue By Product Plot to plots/revenue_by_product.png")

    highest_product = by_product.idxmax()
    highest_value = by_product.max()

    print(f"The highest product is: {highest_product} (${highest_value})")

    plt.show()


if __name__ == '__main__':
    main()