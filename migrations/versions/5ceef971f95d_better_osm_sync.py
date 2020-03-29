"""better osm sync

Revision ID: 5ceef971f95d
Revises: cdad92104ad0
Create Date: 2020-03-27 19:19:29.524659

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ceef971f95d'
down_revision = 'cdad92104ad0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('region', sa.Column('regionalschluessel', sa.String(length=16), nullable=True))
    op.add_column('region', sa.Column('sync_status', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('region', 'sync_status')
    op.drop_column('region', 'regionalschluessel')
    # ### end Alembic commands ###