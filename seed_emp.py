import os
import json
import logging
import requests

BASE_URL = "https://1ammyafot0.execute-api.us-east-1.amazonaws.com"  # <-- Replace with your actual base URL


def load_data(filename):
    """Load JSON data from a file."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, filename)
    with open(file_path, 'r') as f:
        return json.load(f)


def get_file_path(filename):
    """Get the absolute path to a file in the 'static' folder."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, 'static', filename)


def extract_error_message(exception):
    """Extract JSON or text from HTTPError response."""
    response = exception.response
    if response is not None:
        try:
            return response.json()
        except ValueError:
            return response.text
    return str(exception)


def seed_employees():
    url = f"{BASE_URL}/organization/employee/create"
    employees_data = load_data("employees_two.json")

    created_employees = []

    for i, employee_data in enumerate(employees_data, start=1):
        application_data_str = json.dumps(employee_data)

        image_path = get_file_path("image.jpg")

        with open(image_path, 'rb') as image_file:
            files = {
                'application_data': (None, application_data_str, 'application/json'),
                'candidate_image': ('image.jpg', image_file, 'image/jpeg'),
            }

            try:
                response = requests.post(url, files=files)
                response.raise_for_status()

                response_data = response.json()

                employee_details = {
                    "id": response_data.get("id"),
                    "password": response_data.get("password"),
                    "login_id": response_data.get("login_id"),
                }

                created_employees.append(employee_details)
                logging.info(f"[{i}] ✅ Created: {employee_details}")

            except requests.exceptions.HTTPError as e:
                error_message = extract_error_message(e)
                logging.error(f"[{i}] ❌ HTTP error: {error_message}")
            except requests.exceptions.RequestException as e:
                logging.error(f"[{i}] ❌ Request failed: {str(e)}")

    logging.info(f"✅ Done: {len(created_employees)} created out of {len(employees_data)}")
    return created_employees


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    seed_employees()
