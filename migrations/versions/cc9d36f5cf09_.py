"""empty message

Revision ID: cc9d36f5cf09
Revises: 19b995f85dcb
Create Date: 2024-05-31 06:18:50.400071

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc9d36f5cf09'
down_revision = '19b995f85dcb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('room', schema=None) as batch_op:
        batch_op.alter_column('ownerId',
               existing_type=sa.TEXT(),
               type_=sa.String(length=36),
               nullable=False)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('country', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('date_of_birth', sa.DateTime(), nullable=True))
        batch_op.alter_column('username',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=100),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=sa.String(length=100),
               type_=sa.INTEGER(),
               existing_nullable=False)
        batch_op.drop_column('date_of_birth')
        batch_op.drop_column('country')

    with op.batch_alter_table('room', schema=None) as batch_op:
        batch_op.alter_column('ownerId',
               existing_type=sa.String(length=36),
               type_=sa.TEXT(),
               nullable=True)

    # ### end Alembic commands ###