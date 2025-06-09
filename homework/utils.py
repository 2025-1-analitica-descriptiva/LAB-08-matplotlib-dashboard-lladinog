import matplotlib.pyplot as plt
import pandas as pd
import os

def pregunta_01():
    df = load_data("files/input/shipping-data.csv")

    create_visual_for_shipping_per_warehouse(df)
    create_visual_for_mode_of_shipment(df)
    create_visual_for_average_customer_rating(df)
    create_visual_for_weight_distribution(df)

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        # If the directory exists, clear its contents
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
            if os.path.isdir(file_path):
                os.rmdir(file_path)


def load_data(path):
    df = pd.read_csv(path)
    return df

def create_visual_for_shipping_per_warehouse(df, path):
    df= df.copy()
    plt.figure()

    counts = df.Warehouse_block.value_counts()

    counts.plot.bar(
        title = "Shipping per Warehouse",
        xlabel = "Warehouse block",
        ylabel = " Record Count",
        color = "tab:blue",
        fontsize = 8,
    )
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.savefig(path)

def create_visual_for_mode_of_shipment(df, path):
    df = df.copy()
    plt.figure()

    counts = df.Mode_of_Shipment.value_counts()

    counts.plot.pie(
        title= "Mode of shipment",
        wedgeprops = dict(width = 0.35),
        ylabel = "",
        colors = ["tab:blue", "tab:orange", "tab:green"],
        )
    
    plt.savefig(path)

def create_visual_for_average_customer_rating(df, path):
    df = df.copy()
    plt.figure()

    df = (
        df[["Mode_of_Shipment", "Customer_rating"]]
        .groupby("Mode_of_Shipment")
        .describe()
    )

    df.columns = df.columns.droplevel()
    df = df[["mean", "min","max"]]

    plt.barh(
        y = df.index.values,
        width = df["max"].values-1,
        left = df["min"].values,
        height = 0.9,
        color = "lightgray",
        alpha = 0.8,
    )

    colors = [
        "tab:green" if value >= 3.0 else "tab:orange" for value in df["mean"].values
    ]

    plt.barh(
        y = df.index.values,
        width = df["mean"].values-1,
        left = df["min"].values,
        color = colors,
        height = 0.5,
        alpha = 1.0, 
    )

    plt.title("Average Customer Rating")
    plt.gca().spines["left"].set_color("gray")
    plt.gca().spines["bottom"].set_color("gray")
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)

    plt.savefig(path)

def create_visual_for_weight_distribution(df, path):
    df = df.copy()
    plt.figure()

    df.Weight_in_gms.plot.hist(
        title = "Shipped Weight Distribution",
        color = "tab:orange",
        edgecolor = "white",
    )

    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.savefig(path)

import os

def crear_html(path):
    contenido_html = '''<!DOCTYPE html>
<html>
    <body>
        <h1>
            Shipping Dashboard Example
        </h1>
        <div style="width:45%;float:left">
            <img src="shipping_per_warehouse.png" alt="Fig 1">
            <img src="mode_of_shipment.png" alt="Fig 2">
        </div>
        <div style="width:45%;float:left">
            <img src="average_customer_rating.png" alt="Fig 3">
            <img src="weight_distribution.png" alt="Fig 4">
        </div>
    </body>
</html>'''

    # Asegurarse de que la carpeta existe
    os.makedirs(path, exist_ok=True)

    # Crear el archivo index.html en la ruta especificada
    ruta_completa = os.path.join(path, "index.html")
    with open(ruta_completa, "w", encoding="utf-8") as f:
        f.write(contenido_html)

