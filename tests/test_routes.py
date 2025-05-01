import unittest
from app import create_app


class TestRoutes(unittest.TestCase):
    # def set_up(self):
    #     app = create_app()
    #     client = app.test_client()

    def test_generate(self):
        app = create_app()
        client = app.test_client()
        diff = 0.6
        width = 2
        response = client.get(f'/generate/?diff={diff}&width={width}')
        response_no_headers = client.get(f'/generate/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_no_headers.status_code, 200)

    def test_solve(self):
        arr = [0, 0, 7, 0, 4, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 8, 0, 0, 6,
               0, 4, 1, 0, 0, 0, 9, 0, 0,
               0, 0, 0, 0, 0, 0, 1, 7, 0,
               0, 0, 0, 0, 0, 6, 0, 0, 0,
               0, 0, 8, 7, 0, 0, 2, 0, 0,
               3, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 1, 2, 0, 0, 0, 0,
               8, 6, 0, 0, 7, 0, 0, 0, 5]

        app = create_app()
        client = app.test_client()
        response = client.post(f'/solve', json={'arr': arr})
        self.assertEqual(200, response.status_code)

    def test_validate(self):
        arr = [1, 2, 3]
        app = create_app()
        client = app.test_client()
        response1 = client.post('/validate', json={'arr': arr})

        self.assertEqual(response1.status_code, 200)


if __name__ == '__main__':
    unittest.main()
