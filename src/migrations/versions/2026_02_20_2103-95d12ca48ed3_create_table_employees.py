"""create table employees

Revision ID: 95d12ca48ed3
Revises: e3b7351fda49
Create Date: 2026-02-20 21:03:52.388929

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "95d12ca48ed3"
down_revision: Union[str, Sequence[str], None] = "e3b7351fda49"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "employees",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("full_name", sa.String(length=100), nullable=False),
        sa.Column("position", sa.String(length=100), nullable=False),
        sa.Column("salary", sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column("department_id", sa.Integer(), nullable=False),
        sa.Column("hired_at", sa.DateTime(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(
            ["department_id"], ["departments.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
    )



def downgrade() -> None:
    op.drop_table("employees")

