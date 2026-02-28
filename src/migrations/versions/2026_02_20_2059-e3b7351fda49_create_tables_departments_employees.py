"""create tables departments&employees

Revision ID: e3b7351fda49
Revises: f3b00880faab
Create Date: 2026-02-20 20:59:28.820157

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e3b7351fda49"
down_revision: Union[str, Sequence[str], None] = "f3b00880faab"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "departments",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("description", sa.String(length=300), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )



def downgrade() -> None:
    op.drop_table("departments")

