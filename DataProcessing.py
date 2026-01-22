import serial
import matplotlib.pyplot as plt

PORT = "COM7" #Change it to yours
BAUD = 115200

ser = serial.Serial(PORT, BAUD, timeout=1)

times = {}
speeds = {}

while True:
    line = ser.readline().decode().strip()
    if not line:
        continue

    print("Read: ", line)

    #Processing data
    parts = line.split(":")
    if len(parts) != 3:
        continue

    type, runnerID, value = parts
    runnerID = int(runnerID)
    value = float(value)

    if type == "Time":
        times[runnerID] = value
    elif type == "Speed":
        speeds[runnerID] = value

    if len(times) >= 2 and len(speeds) >= 2:
        break

ser.close()

"""
times = {1: 8.21, 2: 6.54}
speeds = {1: 6.09, 2: 7.64}
"""

#Draw
runners = sorted(times.keys())
timeValues = [times[r] for r in runners]
speedValues = [speeds[r] for r in runners]
labels = [f"Runner{r}" for r in runners]

#Bar chart
plt.figure()
plt.barh(labels, timeValues)

plt.xlabel("Time second")
plt.title("Running Time Comparison")

for i in range(len(runners)):
    t = timeValues[i]
    v = speedValues[i]
    plt.text(t + 0.1, i, f"{v:.2f} m/s", va='center')

plt.tight_layout()

#Scatter plot
plt.figure()
plt.scatter(timeValues, speedValues)

for r, t, v in zip(runners, timeValues, speedValues):
    plt.text(t, v, f"Runner{r}")

plt.xlabel("Time second")
plt.ylabel("Average Speed (m/s)")
plt.title("Time vs Speed")
plt.grid(True)
plt.show()

