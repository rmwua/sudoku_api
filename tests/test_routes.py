import unittest
from app import create_app


class TestRoutes(unittest.TestCase):
    # def set_up(self):
    #     app = create_app()
    #     client = app.test_client()

    def test_create_standard(self):
        app = create_app()
        client = app.test_client()
        response = client.get('/create_standard')
        self.assertEqual(response.status_code, 200)

    def test_create_level(self):
        app = create_app()
        client = app.test_client()
        for difficulty in [1, 2, 3]:
            response = client.post('/create_level', json={'difficulty': difficulty})
            self.assertEqual(response.status_code, 200)

    def test_create_custom(self):
        app = create_app()
        client = app.test_client()

        custom_sudoku = [1, 2, 3]
        response = client.post('/create_custom', json={'nums': custom_sudoku})
        self.assertEqual(response.status_code, 200)

    def test_solve(self):
        app = create_app()
        client = app.test_client()

        user_sudoku = [1, 2, 3]

        response = client.post('/solve', json={'nums': user_sudoku})
        self.assertEqual(response.status_code, 200)

    def test_verify(self):
        app = create_app()
        client = app.test_client()
        user_sudoku = [1, 2, 3]
        response = client.post('/verify', json={'nums': user_sudoku})
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
