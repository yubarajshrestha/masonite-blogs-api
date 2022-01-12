"""AddUserIdFieldInCategoriestTable Migration."""

from masoniteorm.migrations import Migration


class AddUserIdFieldInCategoriestTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table("categories") as table:
            table.unsigned_integer("user_id").index().nullable()
            table.foreign("user_id").references("id").on("users").on_delete("cascade")

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table("categories") as table:
            table.drop_column("user_id")
