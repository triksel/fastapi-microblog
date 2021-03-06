"""First

Revision ID: 83566f56f64d
Revises: 
Create Date: 2021-06-19 19:37:43.426365

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83566f56f64d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('microblog_post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('text', sa.String(length=350), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_microblog_post_id'), 'microblog_post', ['id'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_microblog_post_id'), table_name='microblog_post')
    op.drop_table('microblog_post')
    # ### end Alembic commands ###
