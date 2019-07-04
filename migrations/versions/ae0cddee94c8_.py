"""empty message

Revision ID: ae0cddee94c8
Revises: 1cf430ba6fcb
Create Date: 2019-07-04 11:47:18.177831

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae0cddee94c8'
down_revision = '1cf430ba6fcb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('site',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('status', sa.Enum('NEW', 'PROCESSING', 'BLOCKED', 'GOOD_SITE', name='sitestatus'), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('whois_data', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('url')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('site')
    # ### end Alembic commands ###
