"""create table tractors,brands

Revision ID: f3b00880faab
Revises:
Create Date: 2026-02-15 16:46:21.474704

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f3b00880faab"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "tractors",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("brand", sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "brands",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("tractor_id", sa.Integer(), nullable=False),
        sa.Column("horse_power", sa.Integer(), nullable=False),
        sa.Column("quantity", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["tractor_id"],
            ["tractors.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )



def downgrade() -> None:

    op.drop_table("brands")
    op.drop_table("tractors")

