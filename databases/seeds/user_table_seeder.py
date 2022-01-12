"""UserTableSeeder Seeder."""
from masoniteorm.seeds import Seeder
from masonite.facades import Hash

from app.models.User import User


class UserTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        User.create(
            {
                "name": "idmann509",
                "email": "idmann509@gmail.com",
                "password": Hash.make("secret"),
                "phone": "+123456789",
            }
        )
