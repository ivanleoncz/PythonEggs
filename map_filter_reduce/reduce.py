""" Calculate how much a gasoline a pump has provided in a day,
from a proposed data set (hour of the day:gasoline in liters).
"""

from functools import reduce

gasoline = {
        "00":12.902,
        "01":11.015,
        "02":08.230,
        "03":06.320,
        "04":12.987,
        "05":21.310,
        "06":35.890,
        "07":78.901,
        "08":129.900,
        "09":136.529,
        "10":145.090,
        "11":142.780,
        "12":138.090,
        "13":135.208,
        "14":146.430,
        "15":161.070,
        "16":189.210,
        "17":246.678,
        "18":278.890,
        "19":263.410,
        "20":189.630,
        "21":130.450,
        "22":112.231,
        "23":103.109
        }


gasoline_total = reduce(lambda x, y: x + y, gasoline.values() )

print("Approx. Consumption:", round(gasoline_total))
