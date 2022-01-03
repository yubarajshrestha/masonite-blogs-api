"""AddStatusFieldInBlogsTable Migration."""

from masoniteorm.migrations import Migration


class AddStatusFieldInBlogsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table("blogs") as table:
            table.enum("status", ["draft", "published"]).default("draft")

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table("blogs") as table:
            table.drop_column("status")
