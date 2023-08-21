import unittest
from module.contact_list import ContactList

class TestContactList(unittest.TestCase):
    def setUp(self):
        self.contact_list = ContactList()
        self.contact_list.add_contact('Wolverine', '123-466-7890', 'wolverine@mail.com')   
        self.contact_list.add_contact('Jean', '123-456-7890', 'jean@mail.com')
        self.contact_list.add_contact('Xavier', '123-456-9475', 'xavier@mail.com')


    def test_add_contacts(self):
        self.contact_list.add_contact("Raven", "123-456-7890", "raven@mail.com")
        self.assertEqual(self.contact_list.contacts[-1], {"name": "Raven", "phone_number": "123-456-7890", "email": "raven@mail.com"})

    
    def test_get_contacts(self):
        self.assertEqual(self.contact_list.get_contacts(), 
            [
                {"name": "Jean", "phone_number": "123-456-7890", "email": "jean@mail.com"},
                {"name": "Wolverine", "phone_number": "123-466-7890", "email": "wolverine@mail.com"},
                {"name": "Xavier", "phone_number": "123-456-9475", "email": "xavier@mail.com"}
            ]
        )
    
    def test_remove_contact(self):
        self.contact_list.add_contact('Magneto', '123-456-9475', 'magneto@mail.com')
        self.contact_list.remove_contact('Magneto')
        self.assertNotIn('Magneto', self.contact_list.contacts)
        self.assertRaises(ValueError, self.contact_list.remove_contact, 'Magneto')