"""Second

Revision ID: 39c253efcbf4
Revises: 7a92a3e81c1c
Create Date: 2021-10-26 12:55:45.403723

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39c253efcbf4'
down_revision = '7a92a3e81c1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blogs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blogs')
    # ### end Alembic commands ###