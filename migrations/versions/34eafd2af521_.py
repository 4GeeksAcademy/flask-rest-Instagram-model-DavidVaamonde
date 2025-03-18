"""empty message

Revision ID: 34eafd2af521
Revises: ce6348553768
Create Date: 2025-03-17 12:44:02.348914

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34eafd2af521'
down_revision = 'ce6348553768'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###
