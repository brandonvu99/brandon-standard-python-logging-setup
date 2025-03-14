# brandon-standard-python-logging-setup
Just a centralized place to hold my logging configuration for all my scripts.

# Install
## Directly using pip
```
pip install git+https://github.com/brandonvu99/brandon-standard-python-logging-setup.git
```

# Usage
```python
# Contents of minimal_working_example.py
from pathlib import Path

from set_up_standard_logging.set_up_standard_logging import set_up_standard_logging


def main():
  set_up_standard_logging(
      Path("/logs"),
      level=logging.INFO,
      new_log_file_every_run=True,
      log_file_prefix="my-app-logs",
  )
  # Do other work that uses logging...


if __name__ == "__main__":
    main()

```
