import pytest
from fastapi.testclient import TestClient
import glob
import os
import logging

from ..main import app

# Create a client to interact with the app
client = TestClient(app)

# Get the directory of the current test file.
current_dir = os.path.dirname(os.path.abspath(__file__))
# Go up from src/tests to the project root.
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
# Construct the path to the markdown files.
markdown_pattern = os.path.join(project_root, "docs", "examples", "*.md")
markdown_files = glob.glob(markdown_pattern)

# A helper to provide a clear test ID for each file instead of the full path
def get_file_id(filepath):
    return os.path.basename(filepath)

@pytest.mark.parametrize("markdown_file_path", markdown_files, ids=get_file_id)
def test_summarize_endpoint_with_markdown_files(markdown_file_path, caplog):
    """
    Tests the /summarize endpoint by reading content from various markdown files.
    It checks for a successful response, a valid response structure, and logs the result.
    """
    # Set the logging level for the test
    caplog.set_level(logging.INFO)

    # Read the content of the markdown file
    try:
        with open(markdown_file_path, "r", encoding="utf-8") as f:
            text_content = f.read()
    except FileNotFoundError:
        pytest.fail(f"Test file not found: {markdown_file_path}")
    except Exception as e:
        pytest.fail(f"Error reading file {markdown_file_path}: {e}")

    # Ensure content is not empty
    assert text_content.strip(), f"Markdown file is empty: {markdown_file_path}"

    # 2. Define the request payload for the API
    payload = {
        "text": text_content,
        "length": "short",
        "style": "numbered",
        "focus": "costs"  # A generic focus for testing purposes
    }

    # 3. Make the POST request to the /summarize endpoint
    response = client.post("/summarize", json=payload)

    # --- START: ADDED LOGGING ---
    # Log the request and response details
    logging.info(f"\n--- Test for: {os.path.basename(markdown_file_path)} ---")
    logging.info(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        logging.info(f"Summary: {response.json().get('summary', 'N/A')}")
    else:
        logging.error(f"Response Body: {response.text}")
    # --- END: ADDED LOGGING ---

    # 4. Assert the response is successful and has the correct structure
    assert response.status_code == 200, f"API call failed for {markdown_file_path} with status {response.status_code}. Response: {response.text}"

    response_data = response.json()
    assert "summary" in response_data
    assert "meta" in response_data
    assert isinstance(response_data["summary"], str)
    assert len(response_data["summary"]) > 0, "The returned summary should not be empty."