"""Chave estrageira na tabela de statistic

Revision ID: 45ab04b00e2d
Revises: 11de2f1242b6
Create Date: 2021-11-12 14:46:31.284280

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45ab04b00e2d'
down_revision = '11de2f1242b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('statistics', schema=None) as batch_op:
        batch_op.add_column(sa.Column('fk_match_statistics', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'matches', ['fk_match_statistics'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('statistics', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('fk_match_statistics')

    # ### end Alembic commands ###
