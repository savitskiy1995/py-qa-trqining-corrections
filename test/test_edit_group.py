from model.group import Group

def test_edit_group(app):
    if not app.group.is_contact_exist():
        app.group.create(Group(name="new_group", header="logo"))
    app.group.edit_group(Group(name="Edit group", header="Edit header"))
