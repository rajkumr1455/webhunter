# WebHunter v1.3

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/webhunter.git
    cd webhunter
    ```

2. Run the setup script:
    ```bash
    chmod +x setup.sh
    ./setup.sh
    ```

3. Install necessary tools via `install_tools.sh`:
    ```bash
    ./install_tools.sh
    ```

## Usage
Run WebHunter with the following command:
```bash
python3 cli.py --target example.com --modules subdomain,graphql --profile full
