"""empty message

Revision ID: 173dfa296539
Revises: 2042765efe4c
Create Date: 2019-10-17 23:48:57.396228

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '173dfa296539'
down_revision = '2042765efe4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'username',
               existing_type=mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_general_ci', length=120),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'username',
               existing_type=mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_general_ci', length=120),
               nullable=True)
    # ### end Alembic commands ###