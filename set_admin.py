# set_admin.py
from app import app, db, User

with app.app_context():
    admin_user = User.query.filter_by(username='admin').first()
    if admin_user:
        admin_user.is_admin = True
        db.session.commit()
        print("Admin user updated successfully!")
    else:
        print("Admin user not found.")