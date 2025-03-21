# Advanced Python GitHub Assignment

## Overview
This assignment features an advanced Python script that utilizes command-line argument parsing and logging. Follow the steps below to set up, test, and publish your project on GitHub.

## Python Script: `advanced_assignment.py`

```python
import argparse
import logging

def setup_logging(level: str = "INFO"):
    logging.basicConfig(level=level, format='%(asctime)s - %(levelname)s - %(message)s')

def process_message(message: str) -> str:
    """Convert the message to uppercase."""
    return message.upper()

def main():
    parser = argparse.ArgumentParser(description="Advanced GitHub Assignment Script")
    parser.add_argument(
        "-m", "--message",
        type=str,
        default="Hello, GitHub assignment!",
        help="Message to process"
    )
    parser.add_argument(
        "-l", "--log",
        type=str,
        default="INFO",
        help="Logging level (DEBUG, INFO, WARNING, ERROR)"
    )
    args = parser.parse_args()

    setup_logging(args.log)
    logging.info("Starting the assignment script.")

    result = process_message(args.message)
    logging.info(f"Processed message: {result}")
    print(result)

if __name__ == "__main__":
    main()
```

## Instructions

### 1. Create and Test the Script
- **Save the Code:** Save the above script as `advanced_assignment.py`.
- **Run the Script:** Open your terminal and run:
  ```bash
  python advanced_assignment.py --message "Test Message" --log DEBUG
  ```

### 2. Initialize a Git Repository
- **Open Terminal:** Navigate to your project folder.
- **Initialize Git:** Run the following commands:
  ```bash
  git init
  git add advanced_assignment.py
  git commit -m "Add advanced assignment script with argparse and logging"
  ```

### 3. Set Up the GitHub Repository
- **Create Repository:** Create a new repository on GitHub.
- **Link and Push:**
  ```bash
  git remote add origin https://github.com/yourusername/yourrepo.git
  git branch -M main
  git push -u origin main
  ```

### 4. Finishing Up
- **Verify on GitHub:** Ensure your code is visible in your GitHub repository.
- **Optional:** Add a `README.md` with usage instructions and any additional notes.
- **Iterate:** Continue developing your assignment as needed.
