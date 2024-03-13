from django.test import TestCase
from .forms import SamplesAdder


class SamplesAdderFormTestCase(TestCase):
    def test_form_valid_data(self):
        # Testing proper data in form
        form_data = {
            'part_number': 1111,
            'part_name': 'Sample Name',
            'drawing_number': 'ABC112233',
            'drawing_revision': '11111111ABCDE',
            'client': 'ABCdef',
            'trial_number': '123456789',
            'status': 'Not approved',
            'approval_date': '2024-03-03',
            'storage_place': 'A12345'

        }
        form = SamplesAdder(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        # Test for improper data in form
        form_data = {
            'name': '',  # Name is mandatory
            'approval_date': 'invalid_date_format'  # Wrong data format
        }
        form = SamplesAdder(data=form_data)
        self.assertFalse(form.is_valid())
