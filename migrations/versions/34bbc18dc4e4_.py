"""empty message

Revision ID: 34bbc18dc4e4
Revises: 9e22e09c0d1c
Create Date: 2019-11-24 20:26:50.116809

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '34bbc18dc4e4'
down_revision = '9e22e09c0d1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('live_reviews', 'review_rating',
               existing_type=mysql.INTEGER(display_width=11),
               type_=sa.FLOAT(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('live_reviews', 'review_rating',
               existing_type=sa.FLOAT(),
               type_=mysql.INTEGER(display_width=11),
               existing_nullable=True)
    # ### end Alembic commands ###