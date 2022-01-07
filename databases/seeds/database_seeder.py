"""Base Database Seeder Module."""
from masoniteorm.seeds import Seeder

from .user_table_seeder import UserTableSeeder
from .categories_table_seeder import CategoriesTableSeeder


class DatabaseSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        self.call(UserTableSeeder)
        # self.call(CategoriesTableSeeder)
