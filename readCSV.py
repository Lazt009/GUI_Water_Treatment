import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def getLatestData(attr):
    data = pd.read_csv("sensor_readings.csv")
