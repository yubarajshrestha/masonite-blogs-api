"""CreateBlogsTable Migration."""

from masoniteorm.migrations import Migration


class CreateBlogsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("blogs") as table:
            table.increments("id")
            table.string("title")
            table.string("slug").unique()
            table.string("excerpt")
            table.text("content")
            table.unsigned_integer("user_id").index()
            table.foreign("user_id").references("id").on("users").on_delete("cascade")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("blogs")
