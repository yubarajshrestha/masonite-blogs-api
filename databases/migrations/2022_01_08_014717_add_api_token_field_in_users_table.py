"""AddApiTokenFieldInUsersTable Migration."""

from masoniteorm.migrations import Migration


class AddApiTokenFieldInUsersTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table("users") as table:
            table.string("api_token").nullable()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table("users") as table:
            table.drop_column("api_token")
