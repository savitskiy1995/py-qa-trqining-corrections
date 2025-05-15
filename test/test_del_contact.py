from model.contact import Contact


def test_del_contact(app):
    if not app.contact.is_contact_exist():
        app.contact.create_contact(Contact(
            firstname="John",
            lastname="Smith",
            company="Google",
            home_phone="+7999999999",
            email="johnsmith@gmail.com"
        ))
    app.contact.delete_first_contact()