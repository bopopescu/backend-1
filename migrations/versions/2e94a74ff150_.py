"""empty message

Revision ID: 2e94a74ff150
Revises: 787b57ec2026
Create Date: 2019-10-27 15:50:50.596520

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2e94a74ff150'
down_revision = '787b57ec2026'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('live_reviews', 'date_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('live_reviews', sa.Column('date_time', mysql.DATETIME(), nullable=True))
    # ### end Alembic commands ###