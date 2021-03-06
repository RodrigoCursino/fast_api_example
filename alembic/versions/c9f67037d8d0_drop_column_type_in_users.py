"""Drop column type in users

Revision ID: c9f67037d8d0
Revises: 45ab04b00e2d
Create Date: 2021-11-12 18:36:49.480928

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c9f67037d8d0'
down_revision = '45ab04b00e2d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('type')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('type', mysql.VARCHAR(length=10), nullable=True))

    # ### end Alembic commands ###
