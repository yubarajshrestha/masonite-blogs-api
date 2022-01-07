"""UserTableSeeder Seeder."""
from masoniteorm.seeds import Seeder
from config.factories import Factory
from app.models.User import User
from masonite.facades.Hash import Hash


class UserTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        User.create(
            {
                "name": "John Doe",
                "email": "john@doe.com",
                "password": Hash.make('capslock').decode('utf-8'),
                "phone": "+123456789",
            }
        )
        # Factory(User, 50).create()
