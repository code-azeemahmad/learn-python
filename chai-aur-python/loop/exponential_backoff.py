# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

import time

waitTime = 1
maxRetries = 5
attempts = 0

while attempts < maxRetries:
    print("Attempt:", attempts + 1,", Wait Time:", waitTime)
    time.sleep(waitTime)
    waitTime *= 2
    attempts += 1
