"""password migration

Revision ID: 92edc9fd3268
Revises: 10b04cffe036
Create Date: 2019-11-26 15:37:53.388820

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92edc9fd3268'
down_revision = '10b04cffe036'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('password_hash', sa.String(length=255), nullable=True))
    op.drop_column('users', 'password_secure')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_secure', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('users', 'password_hash')
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###
