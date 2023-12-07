# HTTP Endpoint Health Monitor

This project is a simple tool to monitor the health of HTTP endpoints specified in a YAML configuration file. It checks the availability of each endpoint every 15 seconds and logs the cumulative availability percentage for each domain to the console.

## Prerequisites
- `yaml` (install using `pip install pyyaml`)
- `requests` library (install using `pip install requests`)

## Usage

1. Clone the repository or download the project files.
2. Install the required dependencies:
    Command: pip install requests

## Configuration File Format

The configuration file (`config.yaml`) follows a YAML format. Each endpoint in the list has the following schema:

- `name` (string, required): A free-text name to describe the HTTP endpoint.
- `url` (string, required): The URL of the HTTP endpoint.
- `method` (string, optional): The HTTP method of the endpoint (default is GET).
- `headers` (dictionary, optional): The HTTP headers to include in the request.
- `body` (string, optional): The HTTP body to include in the request.

3. Create a YAML configuration file (`config.yaml`) with the HTTP endpoints you want to monitor. Here's an example:

    ```yaml
    - name: Endpoint1
      url: https://fetch.com/
      method: GET

    - name: Endpoint2
      url: https://fetch.com/careers
      method: POST
      headers:
        Content-Type: application/json
      body: '{"key1": "value1"}'

    # Add more endpoints as needed
    ```

4. Run the monitoring script:
    Command: python endpoint_monitor.py


5. The program will continuously monitor the specified endpoints, and the availability percentage will be printed to the console after each 15-second test cycle.

6. To stop the monitoring, press `CTRL+C`.

## Tests

To run the unit tests, use the following command:
    python -m unittest -v test_endpoint_monitor.py
