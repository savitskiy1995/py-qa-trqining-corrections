from model.contact import Contact

def test_edit_contact(app):
    if not app.contact.is_contact_exist():
        app.contact.create_contact(Contact(
            firstname="John",
            lastname="Smith",
            company="Google",
            home_phone="+7999999999",
            email="johnsmith@gmail.com"
        ))
    app.contact.edit_first_contact(Contact(
        firstname="John1",
        lastname="Smith1",
        company="Google1",
        home_phone="+7999999991",
        email="johnsmith@gmail.ru"
    ))