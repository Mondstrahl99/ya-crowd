"""Тесты для Flask приложения."""
import pytest
from src.app import app

@pytest.fixture
def client():
    """Фикстура для тестового клиента."""
    with app.test_client() as client:
        yield client

class TestApp:
    """Тестовый класс для Flask приложения."""
    
    def test_health_check(self, client):
        """Тест health check endpoint."""
        response = client.get('/health')
        assert response.status_code == 200
        data = response.get_json()
        assert data['status'] == 'healthy'
        assert data['service'] == 'calculator-api'
    
    def test_add_endpoint(self, client):
        """Тест endpoint сложения."""
        response = client.post('/api/v1/add', json={'a': 5, 'b': 3})
        assert response.status_code == 200
        data = response.get_json()
        assert data['operation'] == 'add'
        assert data['result'] == 8
    
    def test_add_endpoint_invalid_input(self, client):
        """Тест endpoint сложения с невалидными данными."""
        response = client.post('/api/v1/add', json={'a': 'invalid', 'b': 3})
        assert response.status_code == 400
    
    def test_subtract_endpoint(self, client):
        """Тест endpoint вычитания."""
        response = client.post('/api/v1/subtract', json={'a': 10, 'b': 4})
        assert response.status_code == 200
        data = response.get_json()
        assert data['operation'] == 'subtract'
        assert data['result'] == 6
    
    def test_multiply_endpoint(self, client):
        """Тест endpoint умножения."""
        response = client.post('/api/v1/multiply', json={'a': 3, 'b': 4})
        assert response.status_code == 200
        data = response.get_json()
        assert data['operation'] == 'multiply'
        assert data['result'] == 12
    
    def test_divide_endpoint(self, client):
        """Тест endpoint деления."""
        response = client.post('/api/v1/divide', json={'a': 10, 'b': 2})
        assert response.status_code == 200
        data = response.get_json()
        assert data['operation'] == 'divide'
        assert data['result'] == 5
    
    def test_divide_by_zero_endpoint(self, client):
        """Тест endpoint деления на ноль."""
        response = client.post('/api/v1/divide', json={'a': 10, 'b': 0})
        assert response.status_code == 400
        data = response.get_json()
        assert 'error' in data
