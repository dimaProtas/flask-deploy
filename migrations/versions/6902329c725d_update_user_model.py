"""update user model

Revision ID: 6902329c725d
Revises: 3cd413cdd6a2
Create Date: 2023-03-03 11:56:30.093009

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6902329c725d'
down_revision = '3cd413cdd6a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('first_name', sa.String(length=100), server_default='', nullable=False))
        batch_op.add_column(sa.Column('last_name', sa.String(length=100), server_default='', nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('last_name')
        batch_op.drop_column('first_name')

    # ### end Alembic commands ###
