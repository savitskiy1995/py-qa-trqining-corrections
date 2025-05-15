from random import randrange

from model.contact import Contact

def test_edit_contact(app, db, check_ui):
    old_contacts = db.get_contact_list_from_db()
    index = randrange(len(old_contacts))
    contact = Contact(
        firstname="Victor",
        lastname="Douglas",
        company="Apple",
        home_phone="+7999999999",
        email="vic_douglas@me.com"
    )
    new_id = old_contacts[index].id
    app.contact.edit_contact_by_id(new_id, contact)
    new_contacts = db.get_contact_list_from_db()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)