"""empty message

Revision ID: 79a6d9c2ffda
Revises: a83cfd1be185
Create Date: 2024-04-24 19:13:22.088516

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79a6d9c2ffda'
down_revision = 'a83cfd1be185'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('height', sa.String(length=120), nullable=False),
    sa.Column('mass', sa.String(length=120), nullable=False),
    sa.Column('hair_color', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('character')
    # ### end Alembic commands ###
