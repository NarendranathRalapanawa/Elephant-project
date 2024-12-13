import serial
import matplotlib.pyplot as plt
import json
import os

# Create directories for storing datasets
os.makedirs("datasets/dushanthan", exist_ok=True)
os.makedirs("datasets/lavan", exist_ok=True)

# Maintain counters for each class
elephant_counter = len(os.listdir("datasets/dushanthan"))
noise_counter = len(os.listdir("datasets/lavan"))

def write_data(file_name, values):
    """
    Writes a list of float values to a JSON file.

    Parameters:
    - file_name: Name of the JSON file (e.g., 'data.json').
    - values: A list of float values to save.
    """
    with open(file_name, 'w') as file:
        json.dump(values, file, indent=4)  # Save data as a JSON array with indentation

def read_and_plot_discrete(port, baud_rate, timeout, num_samples):
    """
    Reads discrete data samples from a serial device (e.g., Arduino), plots them, and saves the data.

    Parameters:
    - port: The COM port to which the device is connected (e.g., 'COM3' or '/dev/ttyUSB0').
    - baud_rate: Baud rate for serial communication (e.g., 9600).
    - timeout: Timeout for serial communication in seconds.
    - num_samples: Number of samples to read.
    """
    global elephant_counter, noise_counter

    # Open the serial port
    ser = serial.Serial(port, baud_rate, timeout=timeout)

    samples = []  # Storage for sensor data
    read_count = 0  # Track the number of samples read

    print(f"Reading {num_samples} samples from {port}...")

    try:
        while read_count < num_samples:
            if ser.in_waiting > 0:  # Check if data is available
                data = ser.readline().decode('utf-8').strip()  # Read and decode a line
                try:
                    samples.append(float(data))  # Convert to float and store
                    read_count += 1
                except ValueError:
                    print(f"Invalid data received: {data}")

        print(f"Collected {len(samples)} samples.")
    finally:
        ser.close()  # Ensure the serial port is closed

    # Plot the samples
    plt.figure()
    plt.plot(samples, 'o-', label='Sensor Data')  # Discrete points with lines
    plt.xlabel('Sample Number')
    plt.ylabel('Sensor Value')
    plt.title('Sensor Data Visualization')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Ask the user for the class label
    while True:
        try:
            label = int(input("Class (If dushanthan=1, lavan=0): "))
            if label not in [0, 1]:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter 1 for elephant or 0 for noise.")

    # Define the file path with a sequential number
    if label == 1:
        file_name = f"datasets/dushanthan/dushanthan_{elephant_counter + 1}.json"
        elephant_counter += 1
    else:
        file_name = f"datasets/lavan/lavan_{noise_counter + 1}.json"
        noise_counter += 1

    # Save the data
    write_data(file_name, samples)
    print(f"Data saved to {file_name}.")

# Continuously collect data until manually stopped

while True:
    read_and_plot_discrete(
        port='COM9',  # Replace with your device's port
        baud_rate=9600,
        timeout=1,
        num_samples=5000
    )
