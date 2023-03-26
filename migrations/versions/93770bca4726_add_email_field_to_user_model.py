"""add email field to user model

Revision ID: 93770bca4726
Revises: 521e8e0830de
Create Date: 2023-03-01 11:44:59.487772

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93770bca4726'
down_revision = '521e8e0830de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=255), server_default='', nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('email')

    # ### end Alembic commands ###
