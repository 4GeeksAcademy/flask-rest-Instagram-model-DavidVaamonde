"""empty message

Revision ID: ebbb6b1c8ef0
Revises: a5cffa318ac2
Create Date: 2025-03-17 11:06:00.952835

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ebbb6b1c8ef0'
down_revision = 'a5cffa318ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('User',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=120), nullable=False),
    sa.Column('first_name', sa.String(length=120), nullable=False),
    sa.Column('last_name', sa.String(length=120), nullable=False),
    sa.Column('mail', sa.String(length=120), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('first_name'),
    sa.UniqueConstraint('last_name'),
    sa.UniqueConstraint('mail'),
    sa.UniqueConstraint('username')
    )
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key')
    )
    op.drop_table('User')
    # ### end Alembic commands ###
