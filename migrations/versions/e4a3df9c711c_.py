"""empty message

Revision ID: e4a3df9c711c
Revises: 
Create Date: 2020-11-18 13:05:15.418733

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4a3df9c711c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.VARCHAR(length=80), nullable=False))
    # ### end Alembic commands ###