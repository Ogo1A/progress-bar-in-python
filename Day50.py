import sys
import time

def progressBar(count, total, suffix=''):
    barLength = 60  # Length of the progress bar
    filledLength = int(round(barLength * count / float(total)))

    percent = round(100.0 * count / float(total), 1)
    bar = '=' * filledLength + '-' * (barLength - filledLength)

    sys.stdout.write(f'\r[{bar}] {percent}%...{suffix}')
    sys.stdout.flush()

for i in range(1, 11):  # Iterate from 1 to 10 for full completion
    time.sleep(1)  # Simulate a delay
    progressBar(i, 10)

print("\nDone!")  # Print a new line after the progress bar completes
