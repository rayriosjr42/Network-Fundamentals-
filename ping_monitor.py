import os
import time
from datetime import datetime

# Define the target IP or domain to monitor
target = "8.8.8.8"  # You can replace this with any IP or domain (e.g., "google.com")
logfile = "ping_log.txt"  # Log file to store the results

# Start a loop to continuously ping the target
while True:
    try:
        # Ping the target and capture the result (Windows-specific syntax)
        response = os.system(f"ping -n 1 {target} > nul 2>&1")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Open the log file to append results
        with open(logfile, "a") as log:
            if response == 0:
                log.write(f"{timestamp} - {target} is UP\n")
            else:
                log.write(f"{timestamp} - {target} is DOWN\n")

        # Print the result to the console for live feedback
        print(f"{timestamp} - {target} is {'UP' if response == 0 else 'DOWN'}")

        # Pause for 5 seconds before the next ping
        time.sleep(5)

    except KeyboardInterrupt:
        print("\nScript interrupted by user. Exiting...")
        break  # Gracefully exit the loop when interrupted

    except Exception as e:
        print(f"An error occurred: {e}")
        break  # Exit the loop in case of an error
