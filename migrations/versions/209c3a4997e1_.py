"""empty message

Revision ID: 209c3a4997e1
Revises: 18a961d6e951
Create Date: 2025-03-18 16:06:15.555298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '209c3a4997e1'
down_revision = '18a961d6e951'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'post', ['post_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###
