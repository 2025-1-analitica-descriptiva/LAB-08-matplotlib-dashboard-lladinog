# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""
import matplotlib.pyplot as plt
import pandas as pd

from homework.utils import (load_data,create_directory,create_visual_for_weight_distribution,
                            create_visual_for_average_customer_rating,create_visual_for_mode_of_shipment,
                            create_visual_for_shipping_per_warehouse,crear_html)

def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    df = load_data("files/input/shipping-data.csv")

    create_directory("docs/")
    create_visual_for_shipping_per_warehouse(df,"docs/shipping_per_warehouse.png")
    create_visual_for_mode_of_shipment(df, "docs/mode_of_shipment.png" )
    create_visual_for_average_customer_rating(df, "docs/average_customer_rating.png")
    create_visual_for_weight_distribution(df, "docs/weight_distribution.png")
    crear_html("docs")

if __name__ == "__main__":
    pregunta_01()
