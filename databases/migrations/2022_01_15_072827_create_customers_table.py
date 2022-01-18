"""CreateCustomersTable Migration."""

from masoniteorm.migrations import Migration


class CreateCustomersTable(Migration):
    
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("customers") as table:
            table.increments("customer_id")
            table.string("name")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("customers")
