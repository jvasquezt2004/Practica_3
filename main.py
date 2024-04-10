import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import sys
np.set_printoptions(threshold=sys.maxsize)

image_clear = Image.open("./test.jpg")
# image_dark = Image.open("./image_dark.jpg")

clear_array = np.array(image_clear)
clear_array_red = clear_array[0]
clear_array_green = clear_array[1]
clear_array_blue = clear_array[2]
frequency_red = {}
frequency_green = {}
frequency_blue = {}

for i in range(0, 256):
    reference = str(i)
    frequency_red[reference] = 0
    frequency_green[reference] = 0
    frequency_blue[reference] = 0

for row in clear_array_red:
    for value in row:
        frequency_red[str(value)] += 1
        
for row in clear_array_green:
    for value in row:
        frequency_green[str(value)] += 1
        

for row in clear_array_blue:
    for value in row:
        frequency_blue[str(value)] += 1
        
data_red = list(frequency_red.keys())
bars_red = list(frequency_red.values())

data_green = list(frequency_green.keys())
bars_green = list(frequency_green.values())

data_blue = list(frequency_blue.keys())
bars_blue = list(frequency_blue.values())

fig, axs = plt.subplots(1, 3, figsize=(15, 5), sharey=True)

axs[0].bar(data_red, bars_red, label="Histograma rojo", color="red")
axs[1].bar(data_green, bars_green, label="Histograma verde", color="green")
axs[2].bar(data_blue, bars_blue, label="Histograma azul", color="blue")

plt.show()