from model.group import Group


def test_delete_first_group(app):
    if not app.group.is_contact_exist():
        app.group.create(Group(name="new_group", header="logo"))
    app.group.delete_first_group()
