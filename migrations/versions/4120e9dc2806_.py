"""empty message

Revision ID: 4120e9dc2806
Revises: 
Create Date: 2022-07-12 23:59:32.038698

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4120e9dc2806'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('players',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('wins', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('player_id', sa.Integer(), nullable=False),
    sa.Column('value', sa.Integer(), nullable=False),
    sa.Column('played', sa.Boolean(), nullable=False),
    sa.Column('war', sa.Boolean(), nullable=False),
    sa.Column('image', sa.String(), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['player_id'], ['players.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cards')
    op.drop_table('players')
    # ### end Alembic commands ###
