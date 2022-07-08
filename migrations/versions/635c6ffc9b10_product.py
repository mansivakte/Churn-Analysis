"""product

Revision ID: 635c6ffc9b10
Revises: 7c4fea76a3b2
Create Date: 2022-07-07 15:28:47.280197

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '635c6ffc9b10'
down_revision = '7c4fea76a3b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('order_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('order_status', sa.Integer(), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orderdetails',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('product_price', sa.Integer(), nullable=True),
    sa.Column('product_qty', sa.Integer(), nullable=True),
    sa.Column('total_price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shopholder',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('shopname', sa.String(length=20), nullable=True),
    sa.Column('shopholdername', sa.String(length=40), nullable=True),
    sa.Column('email', sa.String(length=35), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shopholder')
    op.drop_table('orderdetails')
    op.drop_table('order')
    # ### end Alembic commands ###