import serial
import matplotlib.pyplot as plt
import json  # Import json module for saving data in JSON format


def write_data(file_name, values):
    """
    Writes multiple float values to a text file in a single line, separated by commas.
    
    Parameters:
    - file_name: Name of the text file (e.g., 'output.txt').
    - values: A list of float values.
    """
    with open(file_name, 'w') as file:
        #file.write(", ".join(f"{value:.2f}" for value in values))  # Format and join with commas
        json.dump(values, file, indent=4)  # Save data as a JSON array with indentation

# Example usage





def read_and_plot_discrete(port, baud_rate, timeout,num_samples):
    """
    Reads discrete data samples from an Arduino via serial and plots them.

    Parameters:
    - port: The COM port to which the Arduino is connected (e.g., 'COM3' or '/dev/ttyUSB0').
    - baud_rate: Baud rate for serial communication (default: 9600).
    - timeout: Timeout for serial communication in seconds (default: 1).
    - num_samples: Number of samples to read (default: 50).
    """
    # Open the serial port
    ser = serial.Serial(port, baud_rate, timeout=timeout)
    
    # Data storage
    samples = []
    R_count=0
    print(f"Reading {num_samples} samples from {port}...")


    
    # Read the specified number of samples
    try:
        while(R_count<num_samples):
        
            if ser.in_waiting > 0:  # Check if data is available
                data = ser.readline().decode('utf-8').strip()  # Read and decode a line
                try:
                    samples.append(float(data))  # Convert to float and store
                    R_count=R_count+1 #
                except ValueError:
                    print(f"Invalid data received: {data}")
            
           

            print(samples)
            

    finally:
        ser.close()  # Ensure the serial port is closed
    print(len(samples))
    write_data('data_json.json', samples)

    # Plot the samples
    plt.figure()
    plt.plot(samples, 'o-', label='Arduino Data')  # Discrete points with lines
    plt.xlabel('Sample Number')
    plt.ylabel('Sensor Value')
    plt.title('Discrete Arduino Serial Data')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage:
# Replace 'COM3' with your Arduino's serial port and run the function
# read_and_plot_discrete(port='COM3', baud_rate=9600, num_samples=50)
read_and_plot_discrete(port='COM9', baud_rate=9600,timeout=1, num_samples=500)