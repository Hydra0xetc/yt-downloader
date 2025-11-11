# Contributing to YtDownloader

First off, thank you for considering contributing to YtDownloader! It's people like you that make open source such a great community.

We welcome any type of contribution, not just code. You can help with:
*   **Reporting a bug**
*   **Discussing the current state of the code**
*   **Submitting a fix**
*   **Proposing new features**

## Getting Started

1.  **Fork the repository** on GitHub.
2.  **Clone your fork** locally:
    ```bash
    git clone https://github.com/your-username/YtDownloader.git
    ```
3.  **Navigate to the project directory**:
    ```bash
    cd YtDownloader/
    ```
4.  **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## How to Contribute

1.  **Create a new branch** for your changes:
    ```bash
    git checkout -b feature/your-feature-name
    ```
    Or for a bug fix:
    ```bash
    git checkout -b fix/bug-description
    ```
2.  **Make your changes** to the code.
3.  **Commit your changes** with a clear and descriptive commit message:
    ```bash
    git commit -m "feat: Add new feature"
    ```
    Or for a bug fix:
    ```bash
    git commit -m "fix: Resolve issue with video parsing"
    ```
4.  **Push your changes** to your forked repository:
    ```bash
    git push origin feature/your-feature-name
    ```
5.  **Open a Pull Request** to the `main` branch of the original repository. Provide a clear title and description for your pull request, explaining the changes you've made and why.

## Code Style

Please try to follow the existing code style. The project uses basic Python conventions. Ensure your code is clean, readable, and well-commented where necessary.

### Error Message Style

For consistency, all error messages printed to the console should follow this specific format. Use the `print_error` or any log message function from `log.py` like `print_warning`, `print_debug` whenever possible.

Here is the reference implementation from `log.py`:
```python
def print_error(message: Any) -> None:
    print(f"{RED}{BOLD}[ERROR] {RESET}{message}", file=sys.stderr)
```

## Reporting Bugs

If you find a bug, please open an issue on GitHub. In your issue, please include:
*   A clear and descriptive title.
*   A detailed description of the bug, including steps to reproduce it.
*   The version of the script you are using.
*   Any error messages or logs.

## Suggesting Enhancements

If you have an idea for a new feature or an enhancement, please open an issue to discuss it. This allows us to coordinate our efforts and prevent duplication of work.

Thank you for your contribution!
