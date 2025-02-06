import pytest
from Hello import app

@pytest.fixture
def client():
    """
    Fixture that creates an instance of the application's client.

    Returns:
        FlaskClient: The client instance.
    """

    return app.test_client()

def test_ping(client):
    """
    Test function to check the '/ping' endpoint.

    Args:
        client (FlaskClient): The client instance.

    Raises:
        AssertionError: If the response status code is not 200 or the
            response message is not as expected.
    """

    response = client.get('/ping')
    assert response.status_code == 200, "The status code was not 200"
    assert response.json == {'message': 'Pinging Model Application!'}, "The message was not as expected"


    def test_predict(client):

        test_data = {'Gender':"Male", 'Married':"Unmarried", 'Credit_History':"Unclear Debts", 'ApplicantIncome': 100000, 'LoanAmount': 2000000}

        response = client.post('/predict', json = test_data)
        assert response.status_code == 200, "The status code was not 200"
        assert response.json == {"loan_approval_status": "Rejected"}, "The message was not as expected"