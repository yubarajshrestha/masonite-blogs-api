"""CreateBlogCategoryTable Migration."""

from masoniteorm.migrations import Migration


class CreateBlogCategoryTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("blog_category") as table:
            table.increments("id")
            table.unsigned_integer("blog_id").index()
            table.foreign("blog_id").references("id").on("blogs").on_delete("cascade")
            table.unsigned_integer("category_id").index()
            table.foreign("category_id").references("id").on("categories").on_delete("cascade")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("blog_category")
