"""CategoriesTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.models.Category import Category
from config.factories import Factory


class CategoriesTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Factory(Category, 20).create()
