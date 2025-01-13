"""Initial

Revision ID: a16098851806
Revises: e1f63e487fee
Create Date: 2025-01-10 13:19:43.584694

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a16098851806'
down_revision: Union[str, None] = 'e1f63e487fee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('guitars')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('guitars',
    sa.Column('article', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.Column('brand_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('title', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['brand_id'], ['brands.id'], name='guitars_brand_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='guitars_pkey')
    )
    # ### end Alembic commands ###
