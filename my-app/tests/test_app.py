"""Интеграционные тесты для API."""
import os
import pytest
import requests

API_URL = os.getenv('API_URL')

class TestIntegrationAPI:
    """Тесты для реального API."""
    
    def test_health_endpoint(self):
        """Тест health check endpoint."""
        
        response = requests.get(f"{API_URL}/health", timeout=5)
        assert response.status_code == 200
        data = response.json()
        assert data['status'] == 'healthy'
    
    def test_add_endpoint(self):
        """Тест endpoint сложения."""
        response = requests.post(
            f"{API_URL}/api/v1/add",
            json={'a': 5, 'b': 3},
            timeout=5
        )
        assert response.status_code == 200
        data = response.json()
        assert data['operation'] == 'add'
        assert data['result'] == 8
    
    def test_divide_endpoint_error(self):
        """Тест ошибки при делении на ноль."""
        response = requests.post(
            f"{API_URL}/api/v1/divide",
            json={'a': 10, 'b': 0},
            timeout=5
        )
        assert response.status_code == 400
        data = response.json()
        assert 'error' in data
