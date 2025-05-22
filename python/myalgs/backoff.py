import os
import random
import time

from functools import wraps


def retry_with_backoff(max_retries=5,
                       initial_delay=5,
                       random_range=5):
    """Decorate with exponential backoff."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 1
            while attempt <= max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_retries:
                        delay = initial_delay * (2**(attempt - 1))
                        if random_range == 0:
                            random_variation = 0
                        else:
                            random_variation = random.randint(1, random_range)
                        if random.random() < 0.5:
                            randomized_delay = delay + random_variation
                        else:
                            randomized_delay = delay - random_variation

                        randomized_delay = max(randomized_delay, initial_delay)
                        time.sleep(randomized_delay)
                    else:
                        raise
                    attempt += 1
            return None
        return wrapper
    return decorator



    
