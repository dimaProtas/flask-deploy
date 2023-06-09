"""updete User model

Revision ID: 8d213c233cf9
Revises: 6902329c725d
Create Date: 2023-03-07 16:06:35.945638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d213c233cf9'
down_revision = '6902329c725d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('email')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.VARCHAR(length=255), server_default=sa.text("('')"), nullable=False))

    # ### end Alembic commands ###
