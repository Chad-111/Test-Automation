import pytest
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    logging.info("Starting test suite")
    exit_code = pytest.main(["-v", "--html=reports/report.html"])
    if exit_code == 0:
        logging.info("All tests passed")
    else:
        logging.error(f"Some tests failed with exit code: {exit_code}")
