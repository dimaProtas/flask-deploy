"""create Article

Revision ID: 46a40bab9b55
Revises: 56cadf960261
Create Date: 2023-03-07 16:19:00.000180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46a40bab9b55'
down_revision = '56cadf960261'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('articles')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('articles',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=150), nullable=False),
    sa.Column('author', sa.VARCHAR(length=50), nullable=False),
    sa.Column('text', sa.VARCHAR(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('article')
    # ### end Alembic commands ###
