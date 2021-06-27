"""fixing for the customer foreign key

Revision ID: 094136672f79
Revises: bda189d9227c
Create Date: 2021-06-26 20:45:42.262396

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '094136672f79'
down_revision = 'bda189d9227c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('work_orders', 'customer_id',
               existing_type=mysql.VARCHAR(length=80),
               nullable=True)
    op.alter_column('work_orders', 'service_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.drop_index('ix_work_orders_customer_id', table_name='work_orders')
    op.create_foreign_key(None, 'work_orders', 'services', ['service_id'], ['id'])
    op.create_foreign_key(None, 'work_orders', 'customers', ['customer_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'work_orders', type_='foreignkey')
    op.drop_constraint(None, 'work_orders', type_='foreignkey')
    op.create_index('ix_work_orders_customer_id', 'work_orders', ['customer_id'], unique=False)
    op.alter_column('work_orders', 'service_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('work_orders', 'customer_id',
               existing_type=mysql.VARCHAR(length=80),
               nullable=False)
    # ### end Alembic commands ###
