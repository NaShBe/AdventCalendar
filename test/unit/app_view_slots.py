from unittest import main, TestCase
from project.adventapp.views import make_slot, get_slot
from django.http import request, response

class TestAppViewSlots(TestCase):

    def test_create_slot(self):
        slot_request = request.HttpRequest()
        slot_response = make_slot(slot_request)
        self.assertEquals(slot_response.status_code, 200)
        self.assertTrue(slot_response.json)

    def test_create_slot_invalid(self):
        pass


if __name__ == "__main__":
    main()

