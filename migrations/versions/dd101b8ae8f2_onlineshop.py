"""onlineshop

Revision ID: dd101b8ae8f2
Revises: 218e0838dfcf
Create Date: 2020-03-29 16:09:31.681631

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd101b8ae8f2'
down_revision = '218e0838dfcf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('store', sa.Column('onlineshop', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('store', 'onlineshop')
    # ### end Alembic commands ###
